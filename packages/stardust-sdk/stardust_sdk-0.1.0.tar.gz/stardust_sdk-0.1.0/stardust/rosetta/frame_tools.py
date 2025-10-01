"""
Common helpers for frame decomposition.
"""
import json
import math
from stardust.components.ego.ego import Ego


class FrameCapture:
    sequence_type_list = ["IMAGE_SEQUENCE", "IMAGE_SET_SEQUENCE", "POINTCLOUD_SEQUENCE",
                          "POINTCLOUD_SET_SEQUENCE"]
    slot_type_list = ['box3d', 'box2d', 'cuboid', 'polygon3d', 'point3d', 'line3d', 'line', 'splines', 'point',
                      'polygon']
    slot_attr_list = ['matrix', 'plane', 'vertices', 'points', 'point']

    def __init__(self, path):
        with open(path) as fp:
            _ = json.load(fp)
            record = _['taskParams']['record']
            self.attachment_type = record['attachmentType']
            assert self.attachment_type in self.sequence_type_list
            self.projectId = _['projectId']
            self.datasetId = _['datasetId']
            self.poolId = _['poolId']
            self.taskId = _['taskId']
            self.status = _['status']
            self.attachment = record['attachment']
            self.attachment_length = len(record['attachment'])
            self.metadata = record.get('metadata', None)
            self.operators = _['taskParams']['operators']
            self.annotations = _['result']['annotations']

    @staticmethod
    def get_annotation_struct(annotation, annotation_type):
        return {
            "key": annotation['key'],
            "label": annotation['label'],
            "type": annotation['type'],
            annotation_type: []
        }

    @staticmethod
    def inter_polate_number(left_index, right_index, target, right, left):
        return left + ((right - left) / (int(right_index) - int(left_index))) * (target - int(left_index))

    @staticmethod
    def angle_closer_to(left_rotation, right_rotation):
        if left_rotation - right_rotation > math.pi:
            return right_rotation + 2 * math.pi
        if left_rotation - right_rotation < -math.pi:
            return right_rotation - 2 * math.pi
        return right_rotation

    @staticmethod
    def get_slot_structure(example):
        for _ in FrameCapture.slot_attr_list:
            if hasattr(example, _) and eval(f'example.{_}'):
                return True
            else:
                continue
        return False

    @staticmethod
    def binary_search(lst, target):
        left = 0
        right = len(lst) - 1

        while left <= right:
            mid = (left + right) // 2
            if lst[mid] == target:
                return mid
            elif lst[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return lst[left - 1], lst[left]

    @staticmethod
    def get_world(coordinate):
        ego_heading = coordinate["egoHeading"]
        ego_position = coordinate["ego"]
        ego = Ego(
            heading=(ego_heading['x'], ego_heading['y'], ego_heading['z'], ego_heading['w']),
            position=(ego_position['x'], ego_position['y'], ego_position['z'])
        )
        return ego.ego_rt


class UtilityCategory(object):
    """Shared fields"""

    def __init__(self, data):
        self.label = data['label']
        self.type = data['type']

    @staticmethod
    def get_index(frame_list, count):
        for i in frame_list:
            if count < int(i):
                return frame_list.index(i)

    @staticmethod
    def find_closest_values(numbers, target):
        closest_down = None
        closest_up = None

        for number in numbers:
            if int(number) <= target:
                closest_down = number  # Update closest lower value
            else:
                closest_up = number  # Update closest upper value
                break  # Stop once the upper bound is found

        return closest_down, closest_up
