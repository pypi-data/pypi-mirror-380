import numpy as np

from stardust.geometry.ops3d.projection.helper import decode_cam_sources
from stardust.geometry.ops3d.projection.project2img import fisheye_cam2img


def get_img_points(obj_points,
                   num_cameras,
                   img_infos,
                   input_type=None,
                   box_coor=None):
    """

    Args:
        obj_points:
            points of object
        num_cameras:
            number of cameras
        imgInfos: List

        box_coor: input identifier,
            its value is not None when input is box coordinates

    Returns:

    """
    res = {}
    for i in range(num_cameras):
        box = obj_points
        imgs_info = decode_cam_sources(img_infos[i])
        transform_matrix = imgs_info['lidar2cam']
        intrinsic = imgs_info['intrin']
        skew = imgs_info['radial']
        cam_type = imgs_info['cam_type']
        w, h = imgs_info['img_width'], imgs_info['img_height']
        if box_coor != None:
            box = box_coor  # Input already represents 3D box coordinates
        boxes = np.hstack((box, np.ones((box.shape[0], 1))))  # N * 4
        cam_boxes = np.matmul(boxes, transform_matrix.T)
        points_num = cam_boxes.shape[0]
        mask = cam_boxes[:, 2] > 0
        cam_boxes = cam_boxes[mask]
        points_num_after_mask = cam_boxes.shape[0]
        points_occluded = points_num - points_num_after_mask
        if cam_boxes.shape[0] <= 0:
            continue
        if cam_type != 'Fisheye':
            cam_boxes = np.matmul(cam_boxes, intrinsic.T)
            if np.any((np.abs(cam_boxes[:, 2]) < 1)):
                continue
            x, y = cam_boxes[:, 0] / (cam_boxes[:, 2] + 1e-20), cam_boxes[:, 1] / (cam_boxes[:, 2] + 1e-20)
        else:
            cam_in_img = fisheye_cam2img(cam_boxes, skew, 0, intrinsic)
            x = cam_in_img[:, 0]
            y = cam_in_img[:, 1]
        res[i] = (x, y, h, w, points_occluded)
    return res
