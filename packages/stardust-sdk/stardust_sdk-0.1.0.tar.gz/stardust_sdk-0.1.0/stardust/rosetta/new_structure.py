import numpy as np

from stardust.utils.frames import *
from stardust.utils.matrix4 import *


class Slot:
    attr_map = {
        'input': 'input',
        'point': 'point',
        'line': 'vertices',
        'splines': 'vertices',
        'polygon': 'vertices',
        'box2d': 'plane',
        'cuboid': 'vertices',
        'point3d': 'point',
        'line3d': 'points',
        'polygon3d': 'points',
        'box3d': 'matrix',

        'point3d_world': 'point',
        'line3d_world': 'points',
        'polygon3d_world': 'points',
        'box3d_world': 'matrix',
    }

    @classmethod
    def preposition(cls, data, frame_number, attachment):
        cls.target = frame_number
        cls.attachment = attachment
        if data.get('input'):
            cls.data = data['input']
        else:
            cls.data = data
        cls.time_series = cls.data.get('timeSeries', {})
        if cls.time_series:
            cls.frame_list = np.array(list(cls.time_series.keys()), dtype=int).tolist()

    def __init__(self, data, frame_number, attachment=None):
        self.preposition(data, frame_number, attachment)
        for n in ['id', 'label', 'teamId',  'source', 'coordinate']:
            if data.get(n):
                setattr(self, n, data[n])
        self.type = data['type']
        if data.get('coordinate', '') == 'world':
            self.type = f'{self.type}_world'
        commonality_result = self.commonality(self.type)
        if callable(commonality_result):
            if isinstance(commonality_result()(), bool):
                self.label = True
            setattr(self, self.attr_map[self.type], commonality_result()())
        else:
            if isinstance(commonality_result, bool):
                self.label = True
            setattr(self, self.attr_map[self.type], commonality_result)
        self.type = data['type']

    def commonality(self, key):
        if self.time_series:
            temp = str(self.frame_list[-1])
            # Interpolate toward earlier frames
            if self.target < self.frame_list[0]:
                return True
            # Interpolate forward when last state is "appear"
            if self.time_series[temp]['type'] == 'appear' and self.target > self.frame_list[-1]:
                if key == 'box3d':
                    setattr(self, 'box', self.time_series[temp]['value'])
                    return Matrix4(tuple(self.time_series[temp]['value'])).box_info
                elif key == 'input':
                    return {'value': self.time_series[temp]['value']}
                elif key == 'point3d_world':
                    return self.point3d_one_now([self.time_series[temp]['value']], self.frame_list[-1])[0]
                elif key in ['line3d_world', 'polygon3d_world']:
                    return self.point3d_one_now(self.time_series[temp]['value'], self.frame_list[-1])
                elif key == 'box3d_world':
                    box3d_world = self.box3d_one_now(self.time_series[temp]['value'], self.frame_list[-1])
                    setattr(self, 'box', box3d_world)
                    return Matrix4(tuple(box3d_world)).box_info
                return self.time_series[temp]['value']
            # Interpolate forward when last state is "disappear"
            elif self.time_series[temp]['type'] == 'disappear' and self.target > self.frame_list[-1]:
                return True
            else:
                # Return value directly if frame exists
                if self.target in self.frame_list:
                    if self.time_series[str(self.target)]['type'] == "disappear":
                        return True
                    input_value = self.time_series[str(self.target)].get("value")
                    if key in ['box3d', 'teamId', 'box3d_world']:
                        setattr(self, 'box', input_value)
                        return Matrix4(tuple(input_value)).box_info
                    elif key == 'input':
                        return {'value': input_value,
                                'teamId': self.time_series[str(self.target)].get("teamId")
                                }
                    return input_value
                else:
                    return self.slot_factory
        else:
            return True

    def slot_factory(self):
        return {
            'input': self.input_time_series,
            'point': self.point_time_series,
            'line': self.line_time_series,
            'splines': self.line_time_series,
            'polygon': self.line_time_series,
            'box2d': self.box2d_time_series,
            'cuboid': self.cuboid_time_series,
            'point3d': self.point3d_time_series,
            'line3d': self.line3d_time_series,
            'polygon3d': self.line3d_time_series,
            'box3d': self.box3d_time_series,
            'point3d_world': self.point3d_world_time_series,
            'line3d_world': self.line3d_world_time_series,
            'polygon3d_world': self.line3d_world_time_series,
            'box3d_world': self.box3d_world_time_series,

        }[self.type]

    @staticmethod
    def _lerp_factor(left_index: int, right_index: int, target: int) -> float:
        denominator = right_index - left_index
        if denominator == 0:
            return 0.0
        return (target - left_index) / denominator

    @staticmethod
    def _lerp_dict(left_dict: dict, right_dict: dict, keys: tuple, factor: float) -> dict:
        left_vec = np.array([left_dict[key] for key in keys], dtype=float)
        right_vec = np.array([right_dict[key] for key in keys], dtype=float)
        blended = left_vec + (right_vec - left_vec) * factor
        return {key: float(value) for key, value in zip(keys, blended)}

    @staticmethod
    def _lerp_point_list(left_points: list, right_points: list, keys: tuple, factor: float) -> list:
        left_arr = np.array([[point[key] for key in keys] for point in left_points], dtype=float)
        right_arr = np.array([[point[key] for key in keys] for point in right_points], dtype=float)
        blended = left_arr + (right_arr - left_arr) * factor
        return [
            {key: float(value) for key, value in zip(keys, row)}
            for row in blended
        ]

    def input_time_series(self):
        left, right = binary_search(self.frame_list, self.target)
        if self.time_series[str(left)]['type'] == 'appear':
            return {'value': self.time_series[str(left)]['value']}
        return True

    def l_or_r(self, left: int, right: int):
        return (left, right, self.target), self.time_series[str(left)]['value'], self.time_series[str(right)]['value']

    # 2D point
    def point_time_series(self):
        left, right = binary_search(self.frame_list, self.target)
        if self.time_series[str(left)]['type'] == 'appear':
            if self.time_series[str(right)]['type'] == 'appear':
                temp, l, r = self.l_or_r(left, right)
                factor = self._lerp_factor(*temp)
                return self._lerp_dict(l, r, ('x', 'y'), factor)
            return self.time_series[str(left)]['value']
        return True

    # 2D line, curve, or polygon
    def line_time_series(self):
        left, right = binary_search(self.frame_list, self.target)
        if self.time_series[str(left)]['type'] == 'appear':
            if self.time_series[str(right)]['type'] == 'appear':
                temp, l, r = self.l_or_r(left, right)
                if len(l) == len(r):
                    factor = self._lerp_factor(*temp)
                    return self._lerp_point_list(l, r, ('x', 'y'), factor)
                return l
            return self.time_series[str(left)]['value']
        return True

    # 2D bounding box
    def box2d_time_series(self):
        left, right = binary_search(self.frame_list, self.target)
        if self.time_series[str(left)]['type'] == 'appear':
            if self.time_series[str(right)]['type'] == 'appear':
                temp, l, r = self.l_or_r(left, right)
                factor = self._lerp_factor(*temp)
                corners = ('topLeft', 'topRight', 'bottomLeft', 'bottomRight')
                return {
                    corner: self._lerp_dict(l[corner], r[corner], ('x', 'y'), factor)
                    for corner in corners
                }
            return self.time_series[str(left)]['value']
        return True

    # 2D projection of cuboid
    def cuboid_time_series(self):
        left, right = binary_search(self.frame_list, self.target)
        if self.time_series[str(left)]['type'] == 'appear':
            if self.time_series[str(right)]['type'] == 'appear':
                temp, l, r = self.l_or_r(left, right)
                factor = self._lerp_factor(*temp)
                faces = ('front', 'back')
                corners = ('topLeft', 'topRight', 'bottomLeft', 'bottomRight')
                return {
                    face: {
                        corner: self._lerp_dict(l[face][corner], r[face][corner], ('x', 'y'), factor)
                        for corner in corners
                    }
                    for face in faces
                }
            return self.time_series[str(left)]['value']
        return True

    # 3D point
    def point3d_time_series(self):
        left, right = binary_search(self.frame_list, self.target)
        if self.time_series[str(left)]['type'] == 'appear':
            if self.time_series[str(right)]['type'] == 'appear':
                temp, l, r = self.l_or_r(left, right)
                factor = self._lerp_factor(*temp)
                return self._lerp_dict(l, r, ('x', 'y', 'z'), factor)
            return self.time_series[str(left)]['value']
        return True

    # 3D line or polygon
    def line3d_time_series(self):
        left, right = binary_search(self.frame_list, self.target)
        if self.time_series[str(left)]['type'] == 'appear':
            if self.time_series[str(right)]['type'] == 'appear':
                temp, l, r = self.l_or_r(left, right)
                if len(l) == len(r):
                    factor = self._lerp_factor(*temp)
                    return self._lerp_point_list(l, r, ('x', 'y', 'z'), factor)
                return l
            return self.time_series[str(left)]['value']
        return True

    @staticmethod
    def matrix(temp: tuple, left: dict, right: dict):
        return {
            'position': {
                'x': inter_polate_number(*temp, left['position']['x'], right['position']['x']),
                'y': inter_polate_number(*temp, left['position']['y'], right['position']['y']),
                'z': inter_polate_number(*temp, left['position']['z'], right['position']['z'])
            },
            'scale': {
                'length': inter_polate_number(*temp, left['scale']['length'], right['scale']['length']),
                'width': inter_polate_number(*temp, left['scale']['width'], right['scale']['width']),
                'height': inter_polate_number(*temp, left['scale']['height'], right['scale']['height'])
            },
            'rotation': {
                'x': inter_polate_number(*temp, left['rotation']['x'],
                                         angle_closer_to(left['rotation']['x'], right['rotation']['x'])),
                'y': inter_polate_number(*temp, left['rotation']['y'],
                                         angle_closer_to(left['rotation']['y'], right['rotation']['y'])),
                'z': inter_polate_number(*temp, left['rotation']['z'],
                                         angle_closer_to(left['rotation']['z'], right['rotation']['z'])),
                '_order': 'XYZ'
            }
        }

    # 3D bounding box
    def box3d_time_series(self):
        left, right = binary_search(self.frame_list, self.target)
        if self.time_series[str(left)]['type'] == 'appear':
            if self.time_series[str(right)]['type'] == 'appear':
                temp, l, r = self.l_or_r(left, right)
                l_box, r_box = Matrix4(tuple(l)).box_info, Matrix4(tuple(r)).box_info
                matrix = self.matrix(temp, l_box, r_box)
                setattr(self, 'box', Matrix4.get_transform_matrix(matrix))
                return matrix
            setattr(self, 'box', self.time_series[str(left)]['value'])
            return Matrix4(tuple(self.time_series[str(left)]['value'])).box_info
        return True

    def point3d_one_now(self, value: list, frame: int):
        value = point3d_to_world(value, self.attachment[frame].get('coordinate', []))
        return point3d_to_world(value, self.attachment[self.target].get('coordinate', []), overturn=True)

    def point3d_world(self, left: int, right: int):
        temp, l, r = self.l_or_r(left, right)
        l_ = point3d_to_world(l, self.attachment[left].get('coordinate', []))
        r_ = point3d_to_world(r, self.attachment[right].get('coordinate', []))
        return temp, l_, r_

    def point3d_now(self, temp: tuple, left: dict, right: dict):
        point3d_world = [[inter_polate_number(*temp, left[n][i], right[n][i]) for i in ['x', 'y', 'z']]
                         for n in range(len(right))]
        return point3d_to_world(point3d_world, self.attachment[self.target].get('coordinate', []), overturn=True)

    # 3D point (world coordinates)
    def point3d_world_time_series(self):
        left, right = binary_search(self.frame_list, self.target)
        if self.time_series[str(left)]['type'] == 'appear':
            if self.time_series[str(right)]['type'] == 'appear':
                temp, l_world, r_world = self.point3d_world(left, right)
                return self.point3d_now(temp, l_world, r_world)[0]
            return self.point3d_one_now([self.time_series[left]['value']], self.target)[0]
        return True

    # 3D line or polygon (world coordinates)
    def line3d_world_time_series(self):
        left, right = binary_search(self.frame_list, self.target)
        if self.time_series[str(left)]['type'] == 'appear':
            if self.time_series[str(right)]['type'] == 'appear':
                temp, l_world, r_world = self.point3d_world(left, right)
                if len(l_world) == len(r_world):
                    return self.point3d_now(temp, l_world, r_world)
                point3d_world = [[l_world[n][i] for i in ['x', 'y', 'z']] for n in range(len(l_world))]
                return point3d_to_world(point3d_world, self.attachment[self.target].get('coordinate', []),
                                        overturn=True)
            return self.point3d_one_now([self.time_series[left]['value']], self.target)
        return True

    def box3d_one_now(self, value: list, frame: int):
        value = box3d_to_world(value, self.attachment[frame].get('coordinate', []))
        return box3d_to_world(value, self.attachment[self.target].get('coordinate', []), overturn=True)

    def box3d_world(self, left: int, right: int):
        temp, l, r = self.l_or_r(left, right)
        l_ = box3d_to_world(l, self.attachment[left].get('coordinate', []))
        r_ = box3d_to_world(r, self.attachment[right].get('coordinate', []))
        return temp, l_, r_

    # 3D bounding box (world coordinates)
    def box3d_world_time_series(self):
        left, right = binary_search(self.frame_list, self.target)
        if self.time_series[str(left)]['type'] == 'appear':
            if self.time_series[str(right)]['type'] == 'appear':
                temp, l_world, r_world = self.box3d_world(left, right)
                l_world_box, r_world_box = Matrix4(tuple(l_world)).box_info, Matrix4(tuple(r_world)).box_info
                matrix = self.matrix(temp, l_world_box, r_world_box)
                box = box3d_to_world(Matrix4.get_transform_matrix(matrix),
                                     self.attachment[self.target].get('coordinate', []), overturn=True)
                setattr(self, 'box', box)
                return Matrix4(tuple(box)).box_info
            box3d_world = self.box3d_one_now(self.time_series[left]['value'], self.target)
            setattr(self, 'box', box3d_world)
            return Matrix4(tuple(box3d_world)).box_info
        return True


if __name__ == '__main__':
    pass
