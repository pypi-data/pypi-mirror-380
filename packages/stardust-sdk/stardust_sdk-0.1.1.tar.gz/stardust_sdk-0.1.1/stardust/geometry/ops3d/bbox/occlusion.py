from typing import List

import numpy as np
import open3d as o3d
from scipy.spatial import ConvexHull
from shapely.geometry import Polygon

from .proj_helper import get_img_points
from stardust.geometry.ops3d.bbox.structure.bbox_np_ops import points_in_rbbox



def obj_occluded_check(points: np.ndarray,
                       img_info: List,
                       save_bboxes: np.ndarray,
                       save_labels: np.ndarray,
                       save_scores: np.ndarray,
                       area_thr=0.7
                       ):
    """
    Check if lidar objects are occluded on img

    Args:
        points:
            point cloud points
        img_info:
            list of dicts contain img and cam info, you can get this through func: ./utils/projection/helper/decode_img_sources
        save_bboxes:
            bounding boxes
        save_labels:
            labels
        save_scores:
            conf scores
        area_thr:
            threshold for occlusion decision

    Return:
        occlusion mask, True means it is occluded
    """
    num_camera = len(img_info)
    box_mask = np.full((save_bboxes.shape[0],), True, dtype=bool)
    # Track distance from origin for each box
    box_distance = np.sqrt(np.sum(save_bboxes[:, :3] ** 2, axis=1))
    save_bboxes_withd = np.hstack((save_bboxes, box_distance.reshape(save_bboxes.shape[0], 1)))  # N * 4
    # Sort boxes by their distance to the origin
    sorted_indices = np.argsort(save_bboxes_withd[:, -1])
    save_bboxes_withd = save_bboxes_withd[sorted_indices]
    save_bboxes = save_bboxes_withd[:, :-1]
    save_labels = save_labels[sorted_indices]
    save_scores = save_scores[sorted_indices]
    points_mask = points_in_rbbox(points, save_bboxes)
    # Maintain polygons already projected per image
    img_bbox = {i: [] for i in range(num_camera)}
    model_car = o3d.io.read_point_cloud('./car_model_modified.pcd')
    model_car = np.asarray(model_car.points)
    l_model_car = np.max(model_car[:, 0]) - np.min(model_car[:, 0])
    w_model_car = np.max(model_car[:, 1]) - np.min(model_car[:, 1])
    h_model_car = np.max(model_car[:, 2]) - np.min(model_car[:, 2])
    for m in range(points_mask.shape[1]):
        obj_pts = points[points_mask[:, m]]
        if len(obj_pts) <= 200:
            box_mask[m] = False
            continue
        obj_box = save_bboxes[m].tolist()
        x, y, z, width, length, height, ry = obj_box
        scale = np.array([length / l_model_car, width / w_model_car, height / h_model_car])
        model_car_scaled = model_car * scale
        gamma = - np.pi / 2 - ry
        rm = np.array([[np.cos(gamma), -np.sin(gamma), 0],
                       [np.sin(gamma), np.cos(gamma), 0],
                       [0, 0, 1]])
        model_car_scaled = np.matmul(model_car_scaled, rm.T)
        model_car_scaled[:, [0, 1, 2]] = model_car_scaled[:, [0, 1, 2]] + np.array([x, y, z])
        obj_pts_backup, obj_pts = obj_pts, model_car_scaled
        points_proj_res = get_img_points(obj_pts, num_camera, img_info)
        points_proj_res_backup = get_img_points(obj_pts_backup, num_camera, img_info)
        camera_mask = []  # Track visibility per camera
        for i, (x, y, h, w, occluded_pts) in points_proj_res.items():
            # Iterate cameras and check if the projection stays in frame
            proj_pixels = []
            for x_, y_ in zip(x, y):
                if 0 <= x_ < w and 0 <= y_ < h:
                    proj_pixels.append([x_, y_])
            proj_pixels = np.array(proj_pixels)  # object pixels on image
            if i in points_proj_res_backup:
                proj_pixels_backup = []
                val = points_proj_res_backup[i]
                x, y, h, w = val[0], val[1], val[2], val[3]
                for x_, y_ in zip(x, y):
                    if 0 <= x_ < w and 0 <= y_ < h:
                        proj_pixels_backup.append([x_, y_])
                proj_pixels_backup = np.array(proj_pixels_backup)  # object pixels on image
            if occluded_pts == 0:
                # Projection fully visible with no occlusion samples
                hull = ConvexHull(proj_pixels)
                hull1 = hull.vertices.tolist()  # Close polygon by returning to the first vertex
                hull1.append(hull1[0])
                poly_vertices = proj_pixels[hull1, :]
                obj_2d_cur = Polygon(poly_vertices)
                hull_backup = ConvexHull(proj_pixels_backup)
                hull1 = hull_backup.vertices.tolist()  # Close polygon by returning to the first vertex
                hull1.append(hull1[0])
                poly_vertices = proj_pixels_backup[hull1, :]
                obj_2d_cur_backup = Polygon(poly_vertices)
                # Compare observed area against the scaled model area first
                if obj_2d_cur_backup.area / obj_2d_cur.area <= (1 - area_thr):
                    camera_mask.append(False)
                masked = True  # Track whether the box is occluded
                if img_bbox[i]:
                    # Another closer box is already tracked; compute IoU
                    whole_union = None
                    for obj_2d_pre in img_bbox[i]:
                        if (obj_2d_pre).intersection(obj_2d_cur).area > 0:
                            if whole_union is None:
                                whole_union = (obj_2d_pre).intersection(obj_2d_cur)
                            else:
                                whole_union = whole_union.union((obj_2d_pre).intersection(obj_2d_cur))
                    if whole_union is not None:
                        masked_area = whole_union.area / (obj_2d_cur).area
                        if masked_area >= area_thr:
                            masked = False
                    camera_mask.append(masked)
                    img_bbox[i].append(obj_2d_cur)
                else:
                    img_bbox[i].append(obj_2d_cur)
                    camera_mask.append(masked)
                # Truncated projection path
            else:
                if len(proj_pixels) >= 3:
                    hull = ConvexHull(proj_pixels)
                    hull1 = hull.vertices.tolist()  # Close polygon by returning to the first vertex
                    hull1.append(hull1[0])
                    poly_vertices = proj_pixels[hull1, :]
                    obj_2d_cur = Polygon(poly_vertices)
                    iou_flag = True
                    masked = True  # Track whether the box is occluded
                    if img_bbox[i]:
                        # Another closer box is already tracked; compute IoU
                        for obj_2d_pre in img_bbox[i]:
                            intersect = (obj_2d_pre).intersection(obj_2d_cur).area
                            union = (obj_2d_pre).union(obj_2d_cur).area
                            masked_area = intersect / (obj_2d_cur).area
                            if masked_area >= area_thr:
                                masked = False
                                break
                        camera_mask.append(masked)
                        img_bbox[i].append(obj_2d_cur)
                        iou_flag = False
                    else:
                        img_bbox[i].append(obj_2d_cur)
                    if iou_flag:
                        if (1 - area_thr) * obj_pts.shape[0] > occluded_pts:
                            camera_mask.append(True)
                        else:
                            camera_mask.append(False)
                else:
                    camera_mask.append(False)
        camera_mask = np.any(camera_mask)
        if not camera_mask:
            box_mask[m] = False
    return box_mask
