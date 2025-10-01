from typing import Dict
import math
import numpy as np
from .helper import decode_cam_sources


def pointcloud2cam(points: np.ndarray, extrin: np.ndarray) -> np.ndarray:
    """
    Project point cloud points to camera coordinate

    Args:
        points:
            np.ndarray with shape (N, 4)
        extrin:
            extrinsics, (4, 4)

    Return:
        points_cam:
            Points in camera coordiante, (4, 4)
    """
    points_cam = np.matmul(points, extrin.T)
    mask = points_cam[:, 2] > 0
    points_cam = points_cam[mask]
    return points_cam


def fisheye_cam2img(pts_on_cam, cam_skew, alpha, cam_intrin):
    """
    Fisheye camera, from camera coordinate to image coordinate

    Args:
        pts_on_cam:

        cam_skew:

        alpha:

        cam_intrin:

    Returns:

    """
    k1, k2, k3, k4 = cam_skew[0], cam_skew[1], cam_skew[2], cam_skew[3]
    xc, yc, zc = pts_on_cam[:, 0], pts_on_cam[:, 1], pts_on_cam[:, 2]
    a, b = xc / (np.abs(zc)), yc / (np.abs(zc))  # N * 1, N * 1
    r = np.array([math.sqrt(a_ ** 2 + b_ ** 2) for a_, b_ in zip(a, b)])  # N * 1
    theta = np.array([math.atan(r_) if zc_ > 0 else math.pi - math.atan(r_) for r_, zc_ in zip(r, zc)])  # N * 1
    theta_d = np.array([theta_ * (1 + k1 * theta_ ** 2 + k2 * theta_ ** 4 + k3 * theta_ ** 6 + k4 * theta_ ** 8) for theta_ in theta])  # N * 1
    scale = np.array([1.0 / r_ if r_ > 1e-8 else 1.0 for r_ in r])
    x_ = np.array([(theta_d_ * scale_) * a_ for theta_d_, scale_, a_ in zip(theta_d, scale, a)]).reshape(-1, 1)
    y_ = np.array([(theta_d_ * scale_) * b_ for theta_d_, scale_, b_ in zip(theta_d, scale, b)]).reshape(-1, 1)
    cam_boxes = np.hstack((x_, y_, np.ones((x_.shape[0], 2))))
    cam_intrin[0][1] = alpha
    img_boxes = np.matmul(cam_boxes, cam_intrin.T)
    return img_boxes[:, :2]


def cam2img(points: np.ndarray, intrin: np.ndarray, type=None, cam_skew=None, alpha=None):
    """
    Project points from camera coordinate to image coordiante

    Args:
        points: (N * 4)
        intrin: (N * 4)
        type: None or str
        cam_skew: (4, )
        alpha: int

    Return:
        pts_in_img: (N, 2)
    """
    if type is None or type == 'Pinhole':
        points_img = np.matmul(points, intrin.T)
        x, y = points_img[0] / points_img[2], points_img[1] / points_img[2]
        pts_in_img = np.stack([x, y], axis=1)
    elif type == 'Fisheye':
        if alpha is None:
            alpha = 0
        pts_in_img = fisheye_cam2img(points, cam_skew, alpha, intrin)
    else:
        raise NotImplementedError
    return pts_in_img


def pointcloud2img(frame_info: Dict, cam_idx: int, points_3d: np.ndarray, img_path=None, res_save_path=None, visual=False):
    """
    Project 3D points on images

    Args:
        frame_info: Dict

        cam_idx: int
            dfsghj
        points_3d: np.ndarray (N, 3)
            ghj

    Return:
        img_pixels: (N, 2)
    """
    cams_info_lst = decode_cam_sources(frame_info)
    pcd_points = np.hstack((points_3d, np.ones((points_3d.shape[0], 1))))  # N * 4
    cam = cams_info_lst[cam_idx]['camera']
    cam2lidar_rt = cam.cam2lidar_rt
    lidar2cam_rt = np.asarray(np.linalg.inv(cam2lidar_rt))
    points_cam = pointcloud2cam(pcd_points, lidar2cam_rt)[:, :3]
    if points_cam.shape[0] == 0:
        return None
    cam_type = cam.camera_type
    img_pixels = []
    if cam_type == 'PinHole':
        for point_cam in points_cam:
            img_pixel = cam._pinhole_3dto2d(point_in_cam=point_cam)
            img_pixels.append(img_pixel)
    elif cam_type == 'Fisheye':
        for point_cam in points_cam:
            img_pixel = cam._fisheye_3dto2d(point_in_cam=point_cam)
            img_pixels.append(img_pixel)
    elif cam_type == 'OmniDirectional':
        for point_cam in points_cam:
            img_pixel = cam._omnidirectional_3dto2d(point_in_cam=point_cam)
            img_pixels.append(img_pixel)

    if visual and img_path is not None:
        import cv2
        img = cv2.imread(img_path)
        h, w = img.shape[0], img.shape[1]
        for (x_, y_) in img_pixels:
            if 0 <= x_ < w and 0 <= y_ < h:
                cv2.circle(img, (int(x_), int(y_)), 1, (0, 0, 255))
        if res_save_path is not None:
            cv2.imwrite(res_save_path, img)
        else:
            print('please identify your visualization result save path')
    return img_pixels
