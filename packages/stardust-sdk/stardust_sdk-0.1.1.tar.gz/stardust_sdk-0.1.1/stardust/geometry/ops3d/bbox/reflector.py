from copy import deepcopy
from matplotlib import pyplot as plt
import numpy as np
import open3d as o3d
from stardust.geometry.ops3d.bbox.structure.bbox_np_ops import points_in_rbbox, rbbox3d_to_bev_corners

"""
    Remove reflector so that the bounding box is closer to the vehicle
"""


def compute_distance(box):
    """
    compute distance from box center to origin
    """
    return np.sqrt(box[0] ** 2 + box[1] ** 2 + box[2] ** 2)


def stardust2kitti(box):
    box[:, -1] = np.pi - box[:, -1]
    return box


def get_rm(heading):
    """
    rotate theta counterclock wise
    """
    cos = np.cos(heading)
    sin = np.sin(heading)
    return np.array([[cos, -sin],
                     [sin, cos]]).astype(np.float64)



# todo
def remove_one_side_up(pts, x1, x2, interval, imagine):

    xprev, xcurr = x1, x1
    pts_num_ratio = []
    count = 0
    while count <= 8:
        count += 1
        xcurr = xprev - interval
        # num of points within xprev and xcurr
        mask = ((pts[:, 0] <= xprev) &
                (pts[:, 0] >= xcurr))
        num = sum(mask)
        if count == 1 and num == 0:
            if imagine:
                x1 -= interval
            break
        if count == 1:
            xprev = xcurr
            prev_num = num
            continue
        ratio = num / prev_num
        pts_num_ratio.append(ratio)
        xprev = xcurr
    for i, r in enumerate(pts_num_ratio):
        if r >= 200:
            x1 -= (i + 1) * interval
            break
    return x1


def remove_one_side_bottom(pts, x1, x2, interval, imagine):
    xprev, xcurr = x2, x2
    pts_num_ratio = []
    count = 0
    while count <= 8:
        count += 1
        xcurr = xprev + interval
        # num of points within xprev and xcurr
        mask = ((pts[:, 0] >= xprev) &
                (pts[:, 0] <= xcurr))
        num = sum(mask)
        if count == 1 and num == 0:
            if imagine:
                x2 += interval
            break
        if count == 1:
            xprev = xcurr
            prev_num = num
            continue
        ratio = num / prev_num
        pts_num_ratio.append(ratio)
        xprev = xcurr
    for i, r in enumerate(pts_num_ratio):
        if r >= 200:
            x2 += (i + 1) * interval
            break
    return x2


# todo
def remove_reflec_bev(pts_bev, x1, x2, interval, imagine):
    """
    Args:
        x1: xmax
        x2: xmin
        interval: the interval of slicing bounding box
        imagine

    """
    x1 = remove_one_side_up(pts_bev, x1, x2, interval, imagine)
    x2 = remove_one_side_bottom(pts_bev, x1, x2, interval, imagine)
    return x1, x2


def exclude_reflector(points: np.ndarray,
                      boxes: np.ndarray,
                      imagine: bool,
                      render_path: str):
    """
    In some training scenario, model will have a higher precision when reflector of vehicles isn't within the bounding box
    This function changes the size of bounding boxes to exclude reflectors
    This function assume there is at least one point in bbox

    Args:
        points:
            point cloud points, (N, 3)
        boxes:
            bounding boxes, (M, 7)
        imagine:
            True means bounding box will imagine there is a reflector manually even though it is invisible from point cloud
            False means bounding box will not imagine there is a reflector manually if it is invisible

    Return:
        New bounding boxes, (M, 7)
    """
    gt_heading = deepcopy(boxes[:, -1])[0]
    kitti_boxes = stardust2kitti(boxes)
    masks = points_in_rbbox(points, kitti_boxes)
    for i in range(kitti_boxes.shape[0]):
        box = kitti_boxes[i]
        box_kittilabel = np.array([box[0], box[1], box[2], box[3], box[4], box[5], box[-1]])
        box_bev_corner = rbbox3d_to_bev_corners(box_kittilabel[np.newaxis, ...])[0].astype(np.float64)
        rm = get_rm(box[-1])
        pts_in_box = points[masks[:, i]]
        # rotate object points so that front of the vehicle heads to the y negative axis
        x, y, z = box[:3]
        pts_in_box -= [x, y, z]
        box_bev_corner -= [x, y]
        # to bev
        pts_in_box_bev = pts_in_box[:, :2]
        # Rotate into vehicle-aligned coordinates
        pts_in_box_bev = pts_in_box_bev @ rm.T
        box_bev_corner = box_bev_corner @ rm.T
        x1, x2 = max(box_bev_corner[:, 0]), min(box_bev_corner[:, 0])
        y1, y2 = max(box_bev_corner[:, 1]), min(box_bev_corner[:, 1])
        newx1, newx2 = remove_reflec_bev(pts_in_box_bev, x1, x2, 0.08, imagine)
        new_car_d = newx1 - newx2
        new_bev_center = np.array([[newx2 + (newx1 - newx2) / 2, 0]])
        # Visualize
        new_bev_corner = np.array([[newx1, y1],
                                   [newx1, y2],
                                   [newx2, y1],
                                   [newx2, y2]])
        render(pts_in_box_bev, box_bev_corner, new_bev_corner, render_path)
        new_bev_center = new_bev_center @ np.linalg.inv(rm).T + [x, y]
        if box[3] < box[4]:
            new_box = [] + new_bev_center.tolist()[0] + [z, new_car_d, box[4], box[5], box[-1]]
        else:
            new_box = [] + new_bev_center.tolist()[0] + [z, box[3], new_car_d, box[5], box[-1]]
        new_box[-1] = gt_heading
        return np.array(new_box)

def order_points(points):
    left_top = points[np.argmin(np.sum(points, axis=1))]
    right_bottom = points[np.argmax(np.sum(points, axis=1))]
    other_points = [point for point in points if (point.tolist() != left_top.tolist() and point.tolist() != right_bottom.tolist())]
    right_top = other_points[0]
    left_bottom = other_points[1]
    ordered_points = np.array([left_top, right_top, right_bottom, left_bottom, left_top])
    return ordered_points

def render(pts_bev, gtbox_bev_corner, procbox_bev_corner, render_path):
    # visualizing
    eval_range = 6
    _, ax = plt.subplots(1, 1, figsize=(10, 10), dpi=500)
    ax.scatter(pts_bev[:, 0], pts_bev[:, 1], c='red', s=0.2)
    gtbox_bev_corner = order_points(gtbox_bev_corner)
    ax.plot(gtbox_bev_corner[:, 0], gtbox_bev_corner[:, 1], linestyle='solid', color='blue')
    procbox_bev_corner = order_points(procbox_bev_corner)
    ax.plot(procbox_bev_corner[:, 0], procbox_bev_corner[:, 1], linestyle='solid', color='green')
    ax.set_xlim(-eval_range - 3, eval_range + 3)
    ax.set_ylim(-eval_range - 3, eval_range + 3)
    plt.axis('off')

    plt.savefig(f"{render_path}/demo.png")
    plt.close()


if __name__ == '__main__':
    gt_boxes = np.array([[-2.113077501102503, -5.521042369327457, 1.0185785336759907, 2.0715079066265627, 4.550000000000131, 1.696969696969697, 2.7185993154604535]])
    pcd_path = 'box_ops/1693197324100.pcd'
    pcd = o3d.io.read_point_cloud(pcd_path)
    pcd_points = np.asarray(pcd.points)
    new_box = exclude_reflector(pcd_points, gt_boxes, imagine=False)
