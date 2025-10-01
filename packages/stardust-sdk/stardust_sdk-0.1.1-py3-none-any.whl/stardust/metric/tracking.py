import collections
import os
import json
from typing import Dict, List, Generator

import numpy as np
from scipy.optimize import linear_sum_assignment

from stardust.components.annotations.box3d import Box3D
from stardust.components.annotations.point3d import Point3D
from stardust.components.annotations.box import Box2D
from stardust.components.annotations.point import Point
from stardust.metric.object_detection import BoxIou2D, BoxIou3D


class TrackingData:
    def __init__(self, track_id: int, box_type: str, obj_info: List):
        """
        Define a tracking object

        Args:
            track_id: int
                tracking id of object
            box_type: str
                type of object, which should be chosen from '2D' and '3D'
            obj_info: List
                info of box, [x, y, z, l, w, h, ry] for box 3d and [x, y, w, h] for box 2d

        Returns:
            TrackingData object

        Examples:
            .. code-block:: python

                from stardust.metric.tracking import TrackingData
                t_data = TrackingData(0, '3D', [1, 2, 3, 4.5, 1.8, 1.5, 0.1])
                t_data = TrackingData(0, '2D', [1, 2, 4.5, 1.8])

        """
        if box_type is None or box_type not in ['2D', '3D']:
            raise ValueError(f"Got invalid box_type {box_type}")
        self.track_id = track_id
        if box_type == '2D':
            if len(obj_info) != 4:
                raise ValueError(f"The input {box_type} box should be [x, y, w, h]")

            self.x = obj_info[0]
            self.y = obj_info[1]
            self.w = obj_info[2]
            self.h = obj_info[3]
        elif box_type == '3D':
            if len(obj_info) != 7:
                raise ValueError(f"The input {box_type} box should be [x, y, z, l, w, h, ry]")

            self.x = obj_info[0]
            self.y = obj_info[1]
            self.z = obj_info[2]
            self.l = obj_info[3]
            self.w = obj_info[4]
            self.h = obj_info[5]
            self.yaw = obj_info[6]
        self.valid = False
        self.tracker = None


class TrackingMetric:
    def __repr__(self):
        description = 'Calculate tracking metric'
        return description

    def __init__(self, trajectory_gt: List, trajectory_pd: List, IoU_thr: float, metric_tyoe: str) -> None:
        """
        Define a TrackMetric object and prepare metric data

        Args:
            trajectory_gt: List
                trajectory of annotation
            trajectory_pd: List
                trajectory of prediction
            IoU_thr: float
                The iou threshold of tp boxes
            metric_tyoe: str
                type of input object, which should be chosen from '2D' and '3D'

        Returns:
            TrackingMetric obj

        """
        self.trajectory_gt = trajectory_gt
        self.trajectory_pd = trajectory_pd
        self.IoU_thr = IoU_thr
        self.metric_tyoe = metric_tyoe
        self.gt = 0
        self.pd = 0
        for frame_id in trajectory_gt:
            self.gt += len(trajectory_gt[frame_id])
        for frame_id in trajectory_pd:
            self.pd += len(trajectory_pd[frame_id])
        self.tp = 0
        self.id_switches = 0
        self.MOTA = 0
        self.ious = []

    def compute(self):
        """
        compute tracking metric

        Args:

        Returns:
            Dict
        """
        max_cost = 1e9
        self.seq_trajectories = collections.defaultdict(list)

        for f in range(len(self.trajectory_gt)):
            g = self.trajectory_gt[f]
            t = self.trajectory_pd[f]
            cost_matrix_iou = []
            iou = np.zeros((len(g), len(t)))
            for gi, gg in enumerate(g):
                gg.tracker = -1
                cost_row_iou = []
                for ti, tt in enumerate(t):
                    if self.metric_tyoe == '3D':
                        pred_bbox = Box3D(Point3D(tt.x, tt.y, tt.z), Point3D(tt.l, tt.w, tt.h), [0, 0, tt.yaw])
                        gt_bbox = Box3D(Point3D(gg.x, gg.y, gg.z), Point3D(gg.l, gg.w, gg.h), [0, 0, gg.yaw])
                        iou[gi][ti] = BoxIou3D().compute_IoU(gt_bbox, pred_bbox, 'IoU')
                    else:
                        pred_bbox = Box2D(center=Point(tt.x, tt.y), size=[tt.w, tt.h])
                        gt_bbox = Box2D(center=Point(gg.x, gg.y), size=[gg.w, gg.h])
                        iou[gi][ti] = BoxIou2D().compute_IoU(gt_bbox, pred_bbox, 'IoU')
                    if iou[gi][ti] >= self.IoU_thr:
                        cost_row_iou.append(1 - iou[gi][ti])
                    else:
                        cost_row_iou.append(max_cost)

                self.seq_trajectories[gg.track_id].append(-1)
                cost_matrix_iou.append(cost_row_iou)

            if len(g) == 0:
                cost_matrix_iou = [[]]
            row_inds, col_inds = linear_sum_assignment(cost_matrix_iou)
            for row, col in zip(row_inds, col_inds):
                c_iou = float(cost_matrix_iou[row][col])
                if c_iou < max_cost:
                    self.ious.append(1 - c_iou)
                    g[row].tracker = t[col].track_id
                    t[col].valid = True
                    self.tp += 1
                    self.seq_trajectories[g[row].track_id][-1] = t[col].track_id
                else:
                    g[row].tracker = -1
        self.fn = self.gt - self.tp
        self.fp = self.pd - self.tp
        for g in self.seq_trajectories.values():
            last_id = g[0]
            for f in range(1, len(g)):
                if last_id != g[f] and last_id != -1 and g[f] != -1 and g[f - 1] != -1:
                    self.id_switches += 1

        if self.gt == 0:
            self.MOTA = float('-inf')
        else:
            self.MOTA = 1 - (self.fn + self.fp + self.id_switches) / float(self.gt)
        self.recall = float('nan') if self.gt == 0 else self.tp / self.gt
        self.precision = float('nan') if self.pd == 0 else self.tp / self.pd
        self.f1 = float('nan') if self.recall + self.precision == 0 else 2 * self.recall * self.precision / (self.recall + self.precision)

        self.miou = sum(self.ious) / len(self.ious) if len(self.ious) else 0
        self.map07 = len([x for x in self.ious if x >= 0.7]) / self.pd if self.pd != 0 else 0
        self.map08 = len([x for x in self.ious if x >= 0.8]) / self.pd if self.pd != 0 else 0
        self.map09 = len([x for x in self.ious if x >= 0.9]) / self.pd if self.pd != 0 else 0
        metric = dict(gt=self.gt, pd=self.pd, tp=self.tp, recall=self.recall, precision=[self.map07, self.map08, self.map09], f1=self.f1, miou=self.miou, idsw=self.id_switches, MOTA=self.MOTA)
        return metric


def compute_metric(data: Generator = None, IoU_thr: float = None, metric_types: List = None, save_path: str = None):
    """
    Computing IoU of all objects in all frames

    Args:
        data: Generator
            A generator object to get all information from all frames
        IoU_thr: float
            The iou threshold of tp boxes
        metric_types: List
            which type of box to compute metric, which can be chosen from ['2D'], ['3D'] and ['2D', '3D']
        save_path: str
            Local path to save metric results

    Returns:
        metric: List
            The metric of dataset which include two dict,
            the first represents metric of every single frame and the second represents metric of all frames

    Examples:
        .. code-block:: python

            from stardust.metric.tracking import compute_metric
            project_id = 856
            Export(project_id, 'top', input_path, True).export()
            json_datas = read_rosetta(project_id=project_id,
                                    input_path=input_path,
                                    )
            metric = compute_metric(json_datas, 0.5, ['2D', '3D'], 'local/')
    """
    assert data
    assert IoU_thr
    assert metric_types and metric_types in [['2D'], ['3D'], ['2D', '3D']]
    task_dict = collections.defaultdict(dict)

    for json_data in data:
        task_info = json_data.task_info
        task_id = str(task_info.task_id)
        frame_num = str(task_info.frame_num)
        task_dict[task_id][frame_num] = json_data
    metric_output = collections.defaultdict(dict)
    metric_total = {}
    for metric_type in metric_types:
        total_gt = total_pd = total_tp = total_idsw = 0
        if metric_type == '3D':
            for task_id in task_dict:
                task_info = sorted(task_dict[task_id].items(), key=lambda x: x[0])
                trajectory_gt = collections.defaultdict(list)
                trajectory_pd = collections.defaultdict(list)
                for frame_id in range(len(task_info)):
                    gts = task_info[frame_id][1].annotation.box3d_lst
                    pds = task_info[frame_id][1].prediction.box3d_lst
                    for obj_id, obj_info in gts.items():
                        x, y, z = obj_info.center
                        l, w, h = obj_info.size
                        ry = obj_info.rotation[-1]
                        t_data = TrackingData(obj_id, metric_type, [x, y, z, l, w, h, ry])
                        trajectory_gt[frame_id].append(t_data)

                    for obj_id, obj_info in pds.items():
                        x, y, z = obj_info.center
                        l, w, h = obj_info.size
                        ry = obj_info.rotation[-1]
                        t_data = TrackingData(obj_id, metric_type, [x, y, z, l, w, h, ry])
                        trajectory_pd[frame_id].append(t_data)

                metric_output[task_id][metric_type] = TrackingMetric(trajectory_gt, trajectory_pd, IoU_thr, metric_type).compute()
                total_gt += metric_output[task_id]['gt']
                total_pd += metric_output[task_id]['pd']
                total_tp += metric_output[task_id]['tp']
                total_idsw += metric_output[task_id]['idsw']

        if metric_type == '2D':
            for task_id in task_dict:
                task_info = sorted(task_dict[task_id].items(), key=lambda x: x[0])
                trajectory_gt = collections.defaultdict(list)
                trajectory_pd = collections.defaultdict(list)
                for frame_id in range(len(task_info)):
                    gts = task_info[frame_id][1].annotation.box2d_lst
                    pds = task_info[frame_id][1].prediction.box2d_lst
                    for obj_id, obj_info in gts.items():
                        x, y = obj_info.center
                        w, h = obj_info.size
                        t_data = TrackingData(obj_id, metric_type, [x, y, w, h])
                        trajectory_gt[frame_id].append(t_data)

                    for obj_id, obj_info in pds.items():
                        x, y = obj_info.center
                        w, h = obj_info.size
                        t_data = TrackingData(obj_id, metric_type, [x, y, w, h])
                        trajectory_pd[frame_id].append(t_data)

                metric_output[task_id] = TrackingMetric(trajectory_gt, trajectory_pd, IoU_thr, metric_type).compute()
                total_gt += metric_output[task_id]['gt']
                total_pd += metric_output[task_id]['pd']
                total_tp += metric_output[task_id]['tp']
                total_idsw += metric_output[task_id]['idsw']
        total_fn = total_gt - total_tp
        total_fp = total_pd - total_tp
        total_recall = float('nan') if total_gt == 0 else total_tp / total_gt
        total_precision = float('nan') if total_pd == 0 else total_tp / total_pd
        total_f1 = float('nan') if total_recall + total_precision == 0 else 2 * total_recall * total_precision / (total_recall + total_precision)
        total_MOTA = float('nan') if total_gt == 0 else 1 - (total_fn + total_fp + total_idsw) / float(total_gt)
        metric_total[metric_type] = dict(gt=total_gt, pd=total_pd, tp=total_tp, recall=total_recall, precision=total_precision, f1=total_f1, MOTA=total_MOTA, idsw=total_idsw)

    if save_path:
        os.makedirs(os.path.join(save_path, 'metric', 'tracking'), exist_ok=True)
        with open(os.path.join(save_path, 'metric', 'tracking', 'metric_by_task_id.json'), 'w') as f:
            json.dump(metric_output, f)
        with open(os.path.join(save_path, 'metric', 'tracking', 'metric_summary.json'), 'w') as f:
            json.dump(metric_total, f)
    return [metric_output, metric_total]
