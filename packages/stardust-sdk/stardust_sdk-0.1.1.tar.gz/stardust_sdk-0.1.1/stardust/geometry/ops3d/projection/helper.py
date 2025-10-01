"""
    This contains all helper function for lidar to image projection
"""
from typing import List, Dict

import numpy as np

from scipy.spatial.transform import Rotation as R
from stardust.components import Camera


def get_extrin(param):
    """
    get transform matrix
    """
    cam2lidar = np.identity(4)
    rotation = list(param['heading'])
    rotation = R.from_quat(rotation).as_matrix()
    translation = np.array(list(param['position']))
    cam2lidar[:3, :3] = rotation
    cam2lidar[:3, 3] = translation

    lidar2cam = np.linalg.inv(cam2lidar)

    return lidar2cam


def get_intrin(param):
    intrin = np.array([[param['intrinsic'][0], 0.0, param['intrinsic'][2], 0.0],
                       [0.0, param['intrinsic'][1], param['intrinsic'][3], 0.0],
                       [0.0, 0.0, 1.0, 0.0]])
    return intrin


def get_radial(param):
    return np.array([v for v in param['radial']])


def get_cam_type(param):
    return param['camera_type']


def decode_cam_sources(frame_info: Dict) -> List:
    """
    Decode extrin, intrin, img width and height from frames info

    Args:
        frame_info: Dict

    Return:
        param_info: List 
    """
    imgs_info = frame_info.image
    param_info = []
    for i, img_info in enumerate(imgs_info):
        cam_param = img_info.camera_param
        heading = cam_param.heading
        position = cam_param.position
        intrin = cam_param.intrinsic
        radial = cam_param.radial
        tangential = cam_param.tangential
        cam_type = cam_param.camera_type
        cam = Camera(camera_type=cam_type,
                     heading=heading,
                     position=position,
                     intrinsic=intrin,
                     radial=radial,
                     tangential=tangential)
        param_dict = dict()
        param_dict['img_width'] = img_info.width
        param_dict['img_height'] = img_info.height
        param_dict['camera'] = cam
        param_info.append(param_dict)
    return param_info