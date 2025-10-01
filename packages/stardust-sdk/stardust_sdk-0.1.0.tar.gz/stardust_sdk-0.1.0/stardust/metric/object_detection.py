import os
import math
import json
from typing import List, Generator

import numpy as np
from scipy.spatial import ConvexHull

from stardust.components.annotations.box import Box2D
from stardust.components.annotations.box3d import Box3D
from stardust.components.annotations.point import Point
from stardust.components.annotations.polygon import Polygon
from .utils import euclidean_distance, bounding_box, intersection_box, box_corners_bev


class BoxIou2D:
    def __repr__(self):
        description = 'Calculate IoU with 2D boxes'
        return description

    def _intersection_over_union(self, box1: Box2D, box2: Box2D):

        """
        Compute IntersectionOverUnion of box1 and box2

        Args:
            box1: Box2D

            box2: Box2D

        Returns:
            float

        Examples:
            .. code-block:: python

                from stardust.metric.object_detection import BoxIou2D
                from stardust.components.annotations.box import Box2D
                metric = BoxIou2D()
                box1 = Box2D(center=[473.07, 395.93], size=[38.65, 28.67])
                box2 = Box2D(center=[473.07, 395.93], size=[38.65, 28.67])
                IoU = metric._intersection_over_union(box1, box2)
        """
        InterBox = intersection_box(box1, box2)

        IoU = InterBox.area / (box1.area + box2.area - InterBox.area + 1e-6)
        return IoU

    def _generalized_intersection_over_union(self, box1: Box2D, box2: Box2D):
        """
        Compute GeneralizedIntersectionOverUnion of box1 and box2

        Args:
            box1: Box2D

            box2: Box2D

        Returns:
            float

        Examples:
            .. code-block:: python

                from stardust.metric.object_detection import BoxIou2D
                from stardust.components.annotations.box import Box2D
                metric = BoxIou2D()
                box1 = Box2D(center=[473.07, 395.93], size=[38.65, 28.67])
                box2 = Box2D(center=[473.07, 395.93], size=[38.65, 28.67])
                IoU = metric._generalized_intersection_over_union(box1, box2)
        """
        BoundBox = bounding_box(box1, box2)
        InterBox = intersection_box(box1, box2)
        union_area = box1.area + box2.area - InterBox.area
        GIoU = InterBox.area / \
               (union_area - (BoundBox.area - union_area) / BoundBox.area + 1e-6)
        return GIoU

    def _distance_intersection_over_union(self, box1: Box2D, box2: Box2D):
        """
        Compute DistanceIntersectionOverUnion of box1 and box2

        Args:
            box1: Box2D

            box2: Box2D

        Returns:
            float

        Examples:
            .. code-block:: python

                from stardust.metric.object_detection import BoxIou2D
                from stardust.components.annotations.box import Box2D
                metric = BoxIou2D()
                box1 = Box2D(center=[473.07, 395.93], size=[38.65, 28.67])
                box2 = Box2D(center=[473.07, 395.93], size=[38.65, 28.67])
                IoU = metric._distance_intersection_over_union(box1, box2)
        """
        BoundBox = bounding_box(box1, box2)
        BoundDiagonalDistance = euclidean_distance(Point(BoundBox.p1.x, BoundBox.p1.y), Point(
            BoundBox.p2.x, BoundBox.p2.y))
        center_distance = euclidean_distance(box1.center, box2.center)
        DIoU = self._intersection_over_union(
            box1, box2) - (center_distance ** 2) / (BoundDiagonalDistance ** 2)
        return DIoU

    def _complete_intersection_over_union(self, box1: Box2D, box2: Box2D):
        """
        Compute CompleteIntersectionOverUnion of box1 and box2

        Args:
            box1: Box2D

            box2: Box2D

        Returns:
            float

        Examples:
            .. code-block:: python

                from stardust.metric.object_detection import BoxIou2D
                from stardust.components.annotations.box import Box2D
                metric = BoxIou2D()
                box1 = Box2D(center=[473.07, 395.93], size=[38.65, 28.67])
                box2 = Box2D(center=[473.07, 395.93], size=[38.65, 28.67])
                IoU = metric._complete_intersection_over_union(box1, box2)
        """
        v = 4 / (math.pi ** 2) * (math.atan(box2.width / box2.height) -
                                  math.atan(box1.width / box1.height)) ** 2
        IoU = self._intersection_over_union(box1, box2)
        alpha = v / (1 - IoU + v)
        CIoU = self._distance_intersection_over_union(box1, box2) - alpha * v
        return CIoU

    def compute_IoU(self, box1: Box2D, box2: Box2D, IoU_mode: str):

        """
        Computing IoU with the given IoU compute method

        Args:
            box1: Box2D

            box2: Box2D

            IoU_mode: str
                The method to compute IoU, IoU_mode should be chosen from 'IoU', 'GIoU', 'DIoU' and 'CIoU'

        Returns:
            float:
                IoU of box1 and box2

        Examples:
            .. code-block:: python

                from stardust.metric.object_detection import BoxIou2D
                from stardust.components.annotations.box import Box2D
                metric = BoxIou2D()
                box1 = Box2D(center=[473.07, 395.93], size=[38.65, 28.67])
                box2 = Box2D(center=[473.07, 395.93], size=[38.65, 28.67])
                IoU = metric.compute_IoU(box1, box2, 'IoU')
        """
        if IoU_mode not in ['IoU', 'GIoU', 'DIoU', 'CIoU']:
            raise ValueError(
                "Got an invalid IoU_mode, IoU_mode should be in ['IoU', 'GIoU', 'DIoU', 'CIoU']")

        if IoU_mode == 'IoU':
            return self._intersection_over_union(box1, box2)

        elif IoU_mode == 'GIoU':
            return self._generalized_intersection_over_union(box1, box2)

        elif IoU_mode == 'DIoU':
            return self._distance_intersection_over_union(box1, box2)

        elif IoU_mode == 'CIoU':
            return self._complete_intersection_over_union(box1, box2)


class BoxIou3D:
    def __repr__(self):
        description = 'Calculate IoU with 3D boxes'
        return description

    def _intersection_over_union(self, box1: Box3D, box2: Box3D):
        """
        Compute IntersectionOverUnion of box1 and box2

        Args:
            box1: Box3D

            box2: Box3D

        Returns:
            float

        Examples:
            .. code-block:: python

                from stardust.metric.object_detection import BoxIou3D
                from stardust.components.annotations.box3d import Box3D
                metric = BoxIou3D()
                box1 = Box3D(center = [4.13, -3.77, 0.78], size=[1, 5, 1], rotation=[0, 0, -1.57], rotation_order="XYZ")
                box2 = Box3D(center = [4.13, -3.77, 0.78], size=[1, 5, 1], rotation=[0, 0, -1.57], rotation_order="XYZ")
                IoU = metric._intersection_over_union(box1, box2)
        """

        reca, recb = box_corners_bev(box1), box_corners_bev(box2)
        ha, hb = box1.size[2], box2.size[2]
        za, zb = box1.center[2], box2.center[2]
        overlap_height = max(
            0, min((za + ha / 2) - (zb - hb / 2), (zb + hb / 2) - (za - ha / 2)))

        IntersectionArea = intersection_box(reca, recb).area * overlap_height
        UnionArea = box1.size[0] * box1.size[1] * ha + \
                    box2.size[0] * box2.size[1] * hb - IntersectionArea
        return IntersectionArea / UnionArea

    def _generalized_intersection_over_union(self, box1: Box3D, box2: Box3D):

        """
        Compute GeneralizedIntersectionOverUnion of box1 and box2

        Args:
            box1: Box3D

            box2: Box3D


        Returns:
            float

        Examples:
            .. code-block:: python

                from stardust.metric.object_detection import BoxIou3D
                from stardust.components.annotations.box3d import Box3D
                metric = BoxIou3D()
                box1 = Box3D(center = [4.13, -3.77, 0.78], size=[1, 5, 1], rotation=[0, 0, -1.57], rotation_order="XYZ")
                box2 = Box3D(center = [4.13, -3.77, 0.78], size=[1, 5, 1], rotation=[0, 0, -1.57], rotation_order="XYZ")
                IoU = metric._generalized_intersection_over_union(box1, box2)
        """
        boxa_corners, boxb_corners = box_corners_bev(box1), box_corners_bev(box2)
        reca = Box2D(Point(boxa_corners[0]), Point(boxa_corners[1]), Point(
            boxa_corners[2]), Point(boxa_corners[3]))
        recb = Box2D(Point(boxb_corners[0]), Point(boxb_corners[1]), Point(
            boxb_corners[2]), Point(boxb_corners[3]))
        ha, hb = box1.size.z, box2.size.z
        za, zb = box1.center.z, box2.center.z
        overlap_height = max(
            0, min((za + ha / 2) - (zb - hb / 2), (zb + hb / 2) - (za - ha / 2)))
        union_height = max((za + ha / 2) - (zb - hb / 2),
                           (zb + hb / 2) - (za - ha / 2))
        intersection_volume = intersection_box(reca, recb).area * overlap_height
        union_volume = box1.size.x * box1.size.y * ha + \
                       box2.size.x * box2.size.y * hb - intersection_volume
        all_corners = np.vstack((boxa_corners, boxb_corners))
        convexHull_area = ConvexHull(all_corners)
        convex_corners = all_corners[convexHull_area.vertices]
        convex_corners = list(map(Point, convex_corners))
        convex_area = Polygon(convex_corners).area
        convexHull_volume = convex_area * union_height
        return intersection_volume / union_volume - (convexHull_volume - union_volume) / convexHull_volume

    def compute_IoU(self, box1: Box3D, box2: Box3D, IoU_mode):
        """
        Computing IoU with the target IoU mode

        Args:
            box1: Box3D

            box2: Box3D

            IoU_mode: str
                The method to compute IoU, IoU_mode should be chosen from 'IoU' and 'GIoU'

        Returns:
            float:
                IoU of box1 and box2

        Examples:
            .. code-block:: python

                from stardust.metric.object_detection import BoxIou3D
                from stardust.components.annotations.box3e import Box3D
                metric = BoxIou3D()
                box1 = Box3D(center = [4.13, -3.77, 0.78], size=[1, 5, 1], rotation=[0, 0, -1.57], rotation_order="XYZ")
                box2 = Box3D(center = [4.13, -3.77, 0.78], size=[1, 5, 1], rotation=[0, 0, -1.57], rotation_order="XYZ")
                IoU = metric.compute_IoU(box1, box2, 'IoU')
        """
        if IoU_mode not in ['IoU', 'GIoU']:
            raise ValueError(
                "Got an invalid IoU_mode, IoU_mode should be in ['IoU', 'GIoU']")

        if IoU_mode == 'IoU':
            return self._intersection_over_union(box1, box2)

        elif IoU_mode == 'GIoU':
            return self._generalized_intersection_over_union(box1, box2)


IoUMode = {
    '2D': BoxIou2D(),
    '3D': BoxIou3D()}


def compute_metric_single_frame(gt_boxes: List, pd_boxes: List, IoU_thr: float, box_type: str, IoU_mode: str):
    """
    Computing metric of all objects in a single frame

    Args:
        gt_boxes: List
            Box list of ground truth, each box should be a Box-like object(Box2D or Box3d)
        pd_boxes: List
            Box list of predictions, each box should be a Box-like object(Box2D or Box3d)
        IoU_thr: float
            The iou threshold of tp boxes
        box_type: str
            Choose which type of objects to be computed, box_type should be chosen from '2D' and '3D'
        IoU_mode: str
            Choose which IoU compute method to be used
    Returns:
        Tuple: metric of gt, pd, tp, recall, precision and f1
    """
    gt = len(gt_boxes)
    pd = len(pd_boxes)
    tp = 0
    for box_id in list(gt_boxes.keys()):
        if box_id in pd_boxes:
            IoU = IoUMode[box_type].compute_IoU(
                gt_boxes[box_id], pd_boxes[box_id], IoU_mode)

            if IoU >= IoU_thr:
                tp += 1
    recall = float('nan') if gt == 0 else tp / gt
    precision = float('nan') if pd == 0 else tp / pd
    f1 = float('nan') if recall + precision == 0 else 2 * \
                                                      recall * precision / (recall + precision)
    return gt, pd, tp, recall, precision, f1


def compute_metric(data: Generator, IoU_thr: float, IoU_mode: str, save_path: str):
    """
    Computing IoU of all objects in all frames

    Args:
        data (Generator):
            A generator object to get all information from all frames
        IoU_thr: float
            The iou threshold of tp boxes
        IoU_mode: str
            Which IoU compute method to be used
        save_path: str
            Local path to save metric results

    Returns:
        Tuple:
            The metric of dataset which include two dict, the first represents metric of every single frame and the second represents metric of all frames

    Examples:
        .. code-block:: python

            from stardust.metric.object_detection import compute_metric
            from stardust.rosetta.rosetta_data import RosettaData
            project_id = 856
            Data(project_id, 'top', input_path, True).export()
            json_datas = read_rosetta(project_id=project_id,
                                    input_path=input_path,
                                    )
            metric = compute_metric(json_datas, 0.5, 'IoU', 'local/')
    """
    total_gt_2d = total_pd_2d = total_tp_2d = 0
    total_gt_3d = total_pd_3d = total_tp_3d = 0

    metric_output = {}

    for task_id, json_data in enumerate(data):
        gts_2d = json_data.annotation.box2d_lst
        pds_2d = json_data.prediction.box2d_lst

        gts_3d = json_data.annotation.box3d_lst
        pds_3d = json_data.prediction.box3d_lst

        gt_2d, pd_2d, tp_2d, recall_2d, precision_2d, f1_2d = compute_metric_single_frame(
            gts_2d, pds_2d, IoU_thr, '2D', IoU_mode)
        metric_output[task_id] = dict(gt_2d=gt_2d, pd_2d=pd_2d, tp_2d=tp_2d,
                                      recall_2d=recall_2d, precision_2d=precision_2d, f1_2d=f1_2d)
        total_gt_2d += gt_2d
        total_pd_2d += pd_2d
        total_tp_2d += tp_2d

        gt_3d, pd_3d, tp_3d, recall_3d, precision_3d, f1_3d = compute_metric_single_frame(
            gts_3d, pds_3d, IoU_thr, '3D', IoU_mode)
        metric_output[task_id].update(dict(
            gt_3d=gt_3d, pd_3d=pd_3d, tp_3d=tp_3d, recall_3d=recall_3d, precision_3d=precision_3d, f1_3d=f1_3d))
        total_gt_3d += gt_3d
        total_pd_3d += pd_3d
        total_tp_3d += tp_3d

    total_recall_2d = float(
        'nan') if total_gt_2d == 0 else total_tp_2d / total_gt_2d
    total_precision_2d = float(
        'nan') if total_pd_2d == 0 else total_tp_2d / total_pd_2d
    total_f1_2d = float('nan') if total_recall_2d + total_precision_2d == 0 else 2 * \
                                                                                 total_recall_2d * total_precision_2d / \
                                                                                 (total_recall_2d + total_precision_2d)

    total_recall_3d = float(
        'nan') if total_gt_3d == 0 else total_tp_3d / total_gt_3d
    total_precision_3d = float(
        'nan') if total_pd_3d == 0 else total_tp_3d / total_pd_3d
    total_f1_3d = float('nan') if total_recall_3d + total_precision_3d == 0 else 2 * \
                                                                                 total_recall_3d * total_precision_3d / \
                                                                                 (total_recall_3d + total_precision_3d)

    metric_total = dict(gt_2d=total_gt_2d, pd_2d=total_pd_2d, tp_2d=total_tp_2d,
                        recall_2d=total_recall_2d, precision_2d=total_precision_2d, f1_2d=total_f1_2d)
    metric_total.update(dict(gt_3d=total_gt_3d, pd_3d=total_pd_3d, tp_3d=total_tp_3d,
                             recall_3d=total_recall_3d, precision_3d=total_precision_3d, f1_3d=total_f1_3d))
    if save_path:
        os.makedirs(os.path.join(save_path, 'metric', 'object_detection'), exist_ok=True)
        with open(os.path.join(save_path, 'metric', 'object_detection', 'metric_by_task_id.json'), 'w') as f:
            json.dump(metric_output, f)
        with open(os.path.join(save_path, 'metric', 'object_detection', 'metric_summary.json'), 'w') as f:
            json.dump(metric_total, f)

    # return metric_output, metric_total
