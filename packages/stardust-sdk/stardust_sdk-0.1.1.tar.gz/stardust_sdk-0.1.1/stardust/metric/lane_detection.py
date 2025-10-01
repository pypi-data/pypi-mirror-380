import math
import json
import os
from typing import List, Union, Generator

import cv2
import numpy as np
from scipy.optimize import linear_sum_assignment

from stardust.components.annotations.point import Point
from stardust.components.annotations.point3d import Point3D


class LaneIoU2D:
    def __repr__(self):
        description = 'Calculate IOU of lanes'
        return description

    def _drawlane(self, lane: List, img_size: tuple, line_width: int):
        img = np.zeros(img_size, dtype=np.uint8)

        for p1, p2 in zip(lane[:-1], lane[1:]):
            cv2.line(img,
                     (int(p1[0]), int(p1[1])),
                     (int(p2[0]), int(p2[1])),
                     color=(255, 255, 255),
                     thickness=line_width)
        return img

    def _intersection_over_union_lane_2d(self, gt_lanes: List[Point], pd_lanes: List[Point], img_size: tuple):
        """
        Compute IntersectionOverUnion of two 2d lanes

        Args:
            gt_lanes: List[Point]
                The ground true of lanes
            pd_lanes: List[Point]
                The prediction of lanes
            img_size: tuple
                height and width of origin data

        Returns:
            np.ndarray: 
                IoU of 2D lanes

        Examples:
            .. code-block:: python

                from stardust.metric.lane_detection import LaneIoU2D
                metric = LaneIoU2D()
                gt_lanes = [Point(1, 1), Point(2, 2), Point(3, 3)]
                pd_lanes = [Point(1, 1), Point(2, 2), Point(3, 3)]
                img_size = [256, 512]
                IOU = metric._intersection_over_union_lane_2d(gt_lanes, pd_lanes, img_size)
        """
        gtlane = [self._drawlane(lane.points.tolist(), img_size=img_size, line_width=10) > 0 for lane in list(gt_lanes.values())]
        predlane = [self._drawlane(lane.points.tolist(), img_size=img_size, line_width=19) > 0 for lane in list(pd_lanes.values())]
        IoUs = np.zeros((len(gtlane), len(predlane)))
        for i, x in enumerate(gtlane):
            for j, y in enumerate(predlane):
                IoUs[i, j] = (x & y).sum() / ((x | y).sum() + 1e-6)
        return IoUs

    def _keypoints_metric(self, gt_points: List[Point], pred_points: List[Point], dist_threshold: float):
        """
        Compute KeypointsMetric of two 2d lanes

        Args:
            gt_lanes: List[Point]
                The ground truth of points
            predlane: List[Point]
                The prediction of points
            dist_threshold: float
                The dist threshold of tp points

        Returns:
            int: 
                keypoint metric of lanes

        Examples:
            .. code-block:: python

                from stardust.metric.lane_detection import LaneIoU2D
                metric = LaneIoU2D()
                gt_lanes = [Point(1, 1), Point(2, 2), Point(3, 3)]
                pd_lanes = [Point(1, 1), Point(2, 2), Point(3, 3)]
                tp = metric.KeypointsMetric(gt_lanes, pd_lanes, 3)
        """
        point_distance = np.zeros((len(pred_points), len(gt_points)))
        # TODO: replace with vectorized matrix operations
        for row, pred_point in enumerate(pred_points):
            pred_pt = np.array([pred_point[0], pred_point[1]])
            for col, gt_point in enumerate(gt_points):
                gt_pt = np.array([gt_point[0], gt_point[1]])
                point_distance[row][col] = np.linalg.norm(gt_pt - pred_pt)
        dist_list = []
        for row in range(point_distance.shape[0]):
            ind = np.argpartition(point_distance[row], -2)[:2]
            nearest_points0, nearest_points1 = gt_points[ind[0]], gt_points[ind[1]]
            gt_p0_x, gt_p0_y, gt_p1_x, gt_p1_y = nearest_points0[0], nearest_points0[1], nearest_points1[0], nearest_points1[1]
            if gt_p1_x != gt_p0_x:
                k = (gt_p1_y - gt_p0_y) / (gt_p1_x - gt_p0_x)
                b = gt_p1_y - k * gt_p1_x
                A, B, C = k, -1, b
            else:
                A, B, C = 1, 0, -gt_p1_x
            pred_p_x, pred_p_y = pred_points[row][0], pred_points[row][1]
            dist = abs(A * pred_p_x + B * pred_p_y + C) / math.sqrt(A ** 2 + B ** 2)
            dist_list.append(dist)
        tp = int(np.sum(np.where(np.array(dist_list) < dist_threshold, True, False)))
        return tp

    # def IntersectionOverUnion3DLane(self, gtlane: List[Point3D], predlane: List[Point3D]):
    #     pass

    # todo
    def compute(self, gt_lanes: Union[List[Point], List[Point3D]], pd_lanes: Union[List[Point], List[Point3D]], IoU_thr: float, kpt_thr: float, img_size: tuple, lane_type: str):
        """
        Compute metric of lanes

        Args:
            gt_lanes: List[Point]
                The ground truth of lanes
            pd_lane: List[Point]
                The prediction of lanes
            IoU_thr: float
                The IoU threshold of tp lanes
            kpt_thr: float
                The dist threshold of tp points
            img_size: tuple
                height and width of origin data
            lane_type: str
                which type of lane to compute metric, only support '2D' for now

        Returns:
            Tuple: 
                metric of lane_gt, lane_pd, lane_tp, kpt_pd, kpt_tp

        Examples:
            .. code-block:: python

                from stardust.metric.lane_detection import LaneIoU2D
                metric = LaneIoU2D()
                gt_lanes = [Point(1, 1), Point(2, 2), Point(3, 3)]
                pd_lanes = [Point(1, 1), Point(2, 2), Point(3, 3)]
                lane_gt, lane_pd, lane_tp, kpt_pd, kpt_tp = laneIOU.compute(gt_lanes, pd_lanes, 0.5, (256, 512), '2D)
        """
        if lane_type == '2D':
            img_size = (1280, 800)
            lane_gt = len(gt_lanes)
            lane_pd = len(pd_lanes)
            kpt_pd = 0
            IOU = self._intersection_over_union_lane_2d(gt_lanes=gt_lanes, pd_lanes=pd_lanes, img_size=img_size)
            row_ind, col_ind = linear_sum_assignment(1 - IOU)
            kpt_tp = 0
            lane_tp = int((IOU[row_ind, col_ind] > IoU_thr).sum())
            for row, col in zip(row_ind, col_ind):
                if IOU[row, col] > IoU_thr:
                    gt_points = list(gt_lanes.values())[row].points.tolist()
                    pd_points = list(pd_lanes.values())[col].points.tolist()
                    kpt_pd += len(pd_points)
                    pt_tp = self._keypoints_metric(gt_points, pd_points, kpt_thr)
                    kpt_tp += pt_tp

            return lane_gt, lane_pd, lane_tp, kpt_pd, kpt_tp
        # else:
        #     IOU = self.IntersectionOverUnion3DLane(gt_lanes, pd_lanes)
        # return metric


IoUMode = {
    '2D': LaneIoU2D()
}


def compute_metric_single_frame(gt_lanes: List, pd_lanes: List, IoU_thr: float, kpt_thr: float, img_size: tuple, lane_type: str):
    """
    Compute metric of all lanes of single frame

    Args:
        gt_lanes: List
           The ground truth of lanes 
        pr_lane: List
           The prediction of lanes 
        IoU_thr: float
            The IoU threshold of tp lanes
        kpt_thr: float
            The dist threshold of tp points
        img_size: tuple
            height and width of origin data
        lane_type: str
            which type of lane to compute metric, only support '2D' for now

    Returns:
        metric: tuple
    """
    if lane_type == '2D':
        assert img_size

    laneIOU = IoUMode[lane_type]
    lane_gt, lane_pd, lane_tp, kpt_pd, kpt_tp = laneIOU.compute(gt_lanes, pd_lanes, IoU_thr, kpt_thr, img_size, lane_type)
    return lane_gt, lane_pd, lane_tp, kpt_pd, kpt_tp


def compute_metric(data: Generator, IoU_thr=0.5, kpt_thr=3, save_path=None):
    """
    Compute metric of lanes

    Args:
        data: Generator
            A generator object to get all information from all frames
        IoU_thr: float
            The IoU threshold of tp lanes
        kpt_thr: float
            The dist threshold of tp points
        save_path: str
            Local path to save metric results

    Returns:Tuple
        The first one represents the metric of every single frame and the second represents the metric of all frames

    Examples:
        .. code-block:: python

            from stardust.metric.lane_detection import compute_metric
            from stardust.rosetta.rosetta_data import RosettaData

            project_id = 856
            json_datas = read_rosetta(project_id=project_id,
                                    input_path=input_path,
                                    )
            metric = compute_metric(json_datas, 0.5, 3, 'local/')
    """
    total_lane_gt_2d = total_lane_pd_2d = total_lane_tp_2d = total_kpt_pd_2d = total_kpt_tp_2d = 0
    metric_output = {}
    for task_id, json_data in enumerate(data):
        gts_2d = json_data.annotation.line_lst
        pds_2d = json_data.prediction.line_lst
        img_size = (json_data.media.image.height, json_data.media.image.width)
        lane_gt, lane_pd, lane_tp, kpt_pd, kpt_tp = compute_metric_single_frame(gts_2d, pds_2d, IoU_thr, kpt_thr, img_size, '2D')
        lane_recall = float('nan') if lane_gt == 0 else lane_tp / lane_gt
        lane_precision = float('nan') if lane_pd == 0 else lane_tp / lane_pd
        lane_f1 = float('nan') if lane_recall + lane_precision == 0 else 2 * lane_recall * lane_precision / (lane_recall + lane_precision)
        kpt_accuracy = float('nan') if kpt_pd == 0 else kpt_tp / kpt_pd
        metric_output[task_id] = dict(lane_gt=lane_gt, lane_pd=lane_pd, lane_tp=lane_tp, lane_recall=lane_recall, lane_precision=lane_precision, lane_f1=lane_f1, kpt_pd=kpt_pd, kpt_tp=kpt_tp,
                                      kpt_accuracy=kpt_accuracy)
        total_lane_gt_2d += lane_gt
        total_lane_pd_2d += lane_pd
        total_lane_tp_2d += lane_tp
        total_kpt_pd_2d += kpt_pd
        total_kpt_tp_2d += kpt_tp

    total_lane_recall_2d = float('nan') if total_lane_gt_2d == 0 else total_lane_tp_2d / total_lane_gt_2d
    total_lane_precision_2d = float('nan') if total_lane_pd_2d == 0 else total_lane_tp_2d / total_lane_pd_2d
    total_lane_f1_2d = float('nan') if total_lane_recall_2d + total_lane_precision_2d == 0 else 2 * total_lane_recall_2d * total_lane_precision_2d / (total_lane_recall_2d + total_lane_precision_2d)

    total_kpt_accuracy_2d = float('nan') if total_kpt_pd_2d == 0 else total_kpt_tp_2d / total_kpt_pd_2d

    metric_total = dict(total_lane_gt_2d=total_lane_gt_2d, total_lane_pd_2d=total_lane_pd_2d, total_lane_tp_2d=total_lane_tp_2d, total_lane_recall_2d=total_lane_recall_2d,
                        total_lane_precision_2d=total_lane_precision_2d, total_lane_f1_2d=total_lane_f1_2d, total_kpt_pd_2d=total_kpt_pd_2d, total_kpt_tp_2d=total_kpt_tp_2d,
                        total_kpt_accuracy_2d=total_kpt_accuracy_2d)

    if save_path is not None:
        os.makedirs(os.path.join(save_path, 'metric', 'lane_detection'), exist_ok=True)
        with open(os.path.join(save_path, 'metric', 'lane_detection', 'metric_by_task_id.json'), 'w') as f:
            json.dump(metric_output, f)
        with open(os.path.join(save_path, 'metric', 'lane_detection', 'metric_summary.json'), 'w') as f:
            json.dump(metric_total, f)
    # return metric_output, metric_total
