from copy import deepcopy
import numpy as np

from stardust.geometry.ops3d.bbox.structure.bbox_np_ops import rbbox3d_to_bev_corners

"""
    Implementation of corner align from paper https://arxiv.org/abs/2101.06586
"""


def rotation_matrix(heading):
    rm = np.array([[np.cos(heading), -np.sin(heading)],
                   [np.sin(heading), np.cos(heading)]])
    return rm


def corner_align(box_3d: np.ndarray, align_size: np.ndarray):
    """
    Implementation of corner align from paper https://arxiv.org/abs/2101.06586
    Align shape based on original box: box_3d and new size: align_size

    Args:
        box_3d:
            box in stardust coordiante, (x, y, z, ..., heading)
        align_size:
            new size, (length on x axis, length on y axis, ..)

    Return:
        Aligned bounding box
    """
    box3d_x, box3d_y, heading = box_3d[0], box_3d[1], box_3d[-1]
    kitti_box3d = deepcopy(box_3d)
    kitti_box3d[-1] = np.pi - kitti_box3d[-1]
    rm_heading = rotation_matrix(kitti_box3d[-1])
    bev_corners = rbbox3d_to_bev_corners(kitti_box3d[np.newaxis, ...])[0]
    align_w, align_l, _ = align_size  # length on x axis, length on y axis
    corner_d = np.linalg.norm(bev_corners, axis=1)
    closest_id = np.argmin(corner_d)
    # transform bev box center to origin
    bev_corners_origin = bev_corners - np.array([box3d_x, box3d_y])
    # rotate
    bev_corners_origin = (bev_corners_origin @ rm_heading.T).astype(np.float32)  # inverse of rm(heading)
    fixed_corner = bev_corners_origin[closest_id]
    fixed_x, fixed_y = fixed_corner
    # loop through the rest three corners
    center_x, center_y = 0, 0
    for i in range(len(bev_corners_origin)):
        if i != closest_id:
            x, y = bev_corners_origin[i]
            if abs(x - fixed_x) < 1e-3:
                if y > fixed_y:
                    center_y = fixed_y + (align_l / 2)
                else:
                    center_y = fixed_y - (align_l / 2)
            if abs(y - fixed_y) < 1e-3:
                if x > fixed_x:
                    center_x = fixed_x + (align_w / 2)
                else:
                    center_x = fixed_x - (align_w / 2)
    new_center = np.array([center_x, center_y])
    new_center = (np.linalg.inv(rm_heading) @ new_center.T)[[1, 0]]
    new_center += np.array([box3d_x, box3d_y])
    box_3d[:2] = new_center
    box_3d[3:6] = align_size
    return box_3d


if __name__ == '__main__':
    box = np.array([138.49, 24.68, 1.88, 9.86, 3.21, 3.56, -1.0692230703881558])
    align_size = np.array([12.73, 3.62, 3.77])
    aligned_box = corner_align(box, align_size)
    print(aligned_box)
