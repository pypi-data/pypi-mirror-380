from copy import deepcopy
import numpy as np
from stardust.rosetta.frame_tools import UtilityCategory, FrameCapture
from stardust.utils.matrix4 import Matrix4


class Slot(UtilityCategory):
    """slot"""
    attr_map = {
        'box3d': 'matrix',
        'polygon3d': 'points',
        'line3d': 'points',
        'point3d': 'point',
        'box2d': 'plane',
        'line': 'vertices',
        'splines': 'vertices',
        'polygon': 'vertices',
        'point': 'point',
        'cuboid': 'vertices',
        'box3d_world': 'matrix',
        'polygon3d_world': 'points',
        'line3d_world': 'points',
        'point3d_world': 'point'
    }

    def __init__(self, data, frame_number, capture):
        super().__init__(data)
        slot_map = {
            'box3d': self.box3d_time_series,
            'polygon3d': self.points_time_series,
            'line3d': self.points_time_series,
            'point3d': self.point3d_time_series,
            'box2d': self.box2d_time_series,
            'line': self.line_time_series,
            'splines': self.line_time_series,
            'polygon': self.line_time_series,
            'point': self.point_time_series,
            'cuboid': self.cuboid_time_series,
            'box3d_world': self.box3d_time_series_world,
            'polygon3d_world': self.points_time_series_world,
            'line3d_world': self.points_time_series_world,
            'point3d_world': self.point3d_time_series_world
        }
        self.id = data['id']
        self.capture = capture
        if data.get('source'):
            self.source = data['source']
        data_type = data['type']
        if data_type in ['box3d', 'polygon3d', 'line3d', 'point3d'] and data.get('coordinate') == 'world':
            slot_map[f'{data_type}_world'](self.attr_map[data_type], data['timeSeries'], frame_number)
        else:
            slot_map[data_type](self.attr_map[data_type], data['timeSeries'], frame_number)

    def box3d_time_series(self, data_type, time_series_dict, frame_number):
        time_series_dict = deepcopy(time_series_dict)
        if not time_series_dict:
            return []
        frame_list = list(time_series_dict.keys())
        time_series_record = {}
        closest_down, closest_up = self.find_closest_values(frame_list, frame_number)
        if closest_down:
            if str(frame_number) in frame_list:
                if time_series_dict[str(frame_number)]['type'] == 'appear':
                    if None in time_series_dict[str(frame_number)]['value']:
                        pass
                    else:
                        self.box = deepcopy(time_series_dict[str(frame_number)]['value'])
                        Matrix4.box = time_series_dict[str(frame_number)]['value']
                        time_series_record[frame_number] = Matrix4().box_info

            elif time_series_dict[closest_down]['type'] == 'appear' and (
                    time_series_dict[closest_up]['type'] == 'disappear' if closest_up else True):
                self.box = deepcopy(time_series_dict[closest_down]['value'])
                Matrix4.box = time_series_dict[closest_down]['value']
                time_series_record[frame_number] = Matrix4().box_info

            elif time_series_dict[closest_down]['type'] == 'appear' and time_series_dict[closest_up][
                'type'] == 'appear':
                Matrix4.box = time_series_dict[closest_down]['value']
                rM = Matrix4().box_info
                Matrix4.box = time_series_dict[closest_up]['value']
                lM = Matrix4().box_info
                _frame = [closest_down, closest_up, frame_number]
                box = {
                    'position': {
                        'x': self.capture.inter_polate_number(*_frame, lM['position']['x'], rM['position']['x']),
                        'y': self.capture.inter_polate_number(*_frame, lM['position']['y'], rM['position']['y']),
                        'z': self.capture.inter_polate_number(*_frame, lM['position']['z'], rM['position']['z'])},
                    'rotation': {
                        'x': self.capture.inter_polate_number(*_frame, lM['rotation']['x'],
                                                              self.capture.angle_closer_to(lM['rotation']['x'],
                                                                                           rM['rotation']['x'])),
                        'y': self.capture.inter_polate_number(*_frame, lM['rotation']['y'],
                                                              self.capture.angle_closer_to(lM['rotation']['y'],
                                                                                           rM['rotation']['y'])),
                        'z': self.capture.inter_polate_number(*_frame, lM['rotation']['z'],
                                                              self.capture.angle_closer_to(lM['rotation']['z'],
                                                                                           rM['rotation']['z'])),
                        '_order': 'XYZ'},
                    'scale': {
                        'height': self.capture.inter_polate_number(*_frame, lM['scale']['height'],
                                                                   rM['scale']['height']),
                        'width': self.capture.inter_polate_number(*_frame, lM['scale']['width'], rM['scale']['width']),
                        'depth': self.capture.inter_polate_number(*_frame, lM['scale']['depth'], rM['scale']['depth'])}
                }
                time_series_record[frame_number] = box
                self.box = Matrix4.get_transform_matrix(box)
        setattr(self, data_type, time_series_record[frame_number] if time_series_record.get(frame_number) else [])

    def box3d_time_series_world(self, data_type, time_series_dict, frame_number):
        time_series_dict = deepcopy(time_series_dict)
        if not time_series_dict:
            return []
        frame_list = list(time_series_dict.keys())
        time_series_record = {}
        closest_down, closest_up = self.find_closest_values(frame_list, frame_number)
        if closest_down:
            if str(frame_number) in frame_list:
                if time_series_dict[str(frame_number)]['type'] == 'appear':
                    if None in time_series_dict[str(frame_number)]['value']:
                        pass
                    else:
                        self.box = deepcopy(time_series_dict[str(frame_number)]['value'])
                        Matrix4.box = time_series_dict[str(frame_number)]['value']
                        time_series_record[frame_number] = Matrix4().box_info

            elif time_series_dict[closest_down]['type'] == 'appear' and (
                    time_series_dict[closest_up]['type'] == 'disappear' if closest_up else True):

                down_coordinate = self.capture.get_world(self.capture.attachment[int(closest_down)].get('coordinate'))
                frame_coordinate = self.capture.get_world(self.capture.attachment[frame_number].get('coordinate'))
                Matrix4.box = time_series_dict[closest_down]['value']
                rM = Matrix4.get_3dbox_same_frame(Matrix4().box_info, down_coordinate)
                frame = Matrix4.get_3dbox_same_frame(rM, np.linalg.inv(frame_coordinate))

                time_series_record[frame_number] = frame
                self.box = Matrix4.get_transform_matrix(frame)


            elif time_series_dict[closest_down]['type'] == 'appear' and time_series_dict[closest_up][
                'type'] == 'appear':
                down_coordinate = self.capture.get_world(self.capture.attachment[int(closest_down)].get('coordinate'))
                up_coordinate = self.capture.get_world(self.capture.attachment[int(closest_up)].get('coordinate'))
                Matrix4.box = time_series_dict[closest_down]['value']
                rM = Matrix4.get_3dbox_matrix(Matrix4().box_info, down_coordinate)
                Matrix4.box = time_series_dict[closest_up]['value']
                lM = Matrix4.get_3dbox_matrix(Matrix4().box_info, up_coordinate)
                _frame = [closest_down, closest_up, frame_number]
                box = {
                    'position': {
                        'x': self.capture.inter_polate_number(*_frame, lM['position']['x'], rM['position']['x']),
                        'y': self.capture.inter_polate_number(*_frame, lM['position']['y'], rM['position']['y']),
                        'z': self.capture.inter_polate_number(*_frame, lM['position']['z'], rM['position']['z'])},
                    'rotation': {
                        'x': self.capture.inter_polate_number(*_frame, lM['rotation']['x'],
                                                              self.capture.angle_closer_to(lM['rotation']['x'],
                                                                                           rM['rotation']['x'])),
                        'y': self.capture.inter_polate_number(*_frame, lM['rotation']['y'],
                                                              self.capture.angle_closer_to(lM['rotation']['y'],
                                                                                           rM['rotation']['y'])),
                        'z': self.capture.inter_polate_number(*_frame, lM['rotation']['z'],
                                                              self.capture.angle_closer_to(lM['rotation']['z'],
                                                                                           rM['rotation']['z'])),
                        '_order': 'XYZ'},
                    'scale': {
                        'height': self.capture.inter_polate_number(*_frame, lM['scale']['height'],
                                                                   rM['scale']['height']),
                        'width': self.capture.inter_polate_number(*_frame, lM['scale']['width'], rM['scale']['width']),
                        'depth': self.capture.inter_polate_number(*_frame, lM['scale']['depth'], rM['scale']['depth'])}
                }
                frame = Matrix4.get_3dbox_matrix(box, self.capture.get_world(
                    self.capture.attachment[frame_number].get('coordinate')).I)
                time_series_record[frame_number] = frame
                self.box = Matrix4.get_transform_matrix(frame)
        setattr(self, data_type, time_series_record[frame_number] if time_series_record.get(frame_number) else [])

    def points_time_series_world(self, data_type, time_series_dict, frame_number):
        time_series_dict = deepcopy(time_series_dict)
        if not time_series_dict:
            return []
        frame_list = list(time_series_dict.keys())
        time_series_record = {}
        closest_down, closest_up = self.find_closest_values(frame_list, frame_number)
        if closest_down:
            if str(frame_number) in frame_list:
                if time_series_dict[str(frame_number)]['type'] == 'appear':
                    time_series_record[frame_number] = time_series_dict[str(frame_number)]['value']
            elif time_series_dict[closest_down]['type'] == 'appear' and (
                    time_series_dict[closest_up]['type'] == 'disappear' if closest_up else True):
                frame_coordinate = self.capture.get_world(self.capture.attachment[frame_number].get('coordinate'))
                down_coordinate = self.capture.get_world(self.capture.attachment[int(closest_down)].get('coordinate'))

                points = []
                for s in time_series_dict[closest_down]['value']:
                    rM = Matrix4.get_points_matrix(s, down_coordinate)
                    points.append(Matrix4.get_points_matrix(rM, np.linalg.inv(frame_coordinate)))
                time_series_record[frame_number] = points
            elif time_series_dict[closest_down]['type'] == 'appear' and time_series_dict[closest_up][
                'type'] == 'appear':
                down_coordinate = self.capture.get_world(self.capture.attachment[int(closest_down)].get('coordinate'))
                up_coordinate = self.capture.get_world(self.capture.attachment[int(closest_up)].get('coordinate'))
                rM = time_series_dict[closest_down]['value']
                lM = time_series_dict[closest_up]['value']
                _frame = [closest_down, closest_up, frame_number]
                points = []
                for s in range(len(rM)):
                    rM_points = Matrix4.get_points_matrix(rM[s], down_coordinate)
                    lM_points = Matrix4.get_points_matrix(lM[s], up_coordinate)
                    frame_points = {
                        'x': self.capture.inter_polate_number(*_frame, lM_points['x'], rM_points['x']),
                        'y': self.capture.inter_polate_number(*_frame, lM_points['y'], rM_points['y']),
                        'z': self.capture.inter_polate_number(*_frame, lM_points['z'], rM_points['z'])}
                    points.append(Matrix4.get_points_matrix(frame_points, self.capture.get_world(
                        self.capture.attachment[frame_number].get('coordinate')).I))
                time_series_record[frame_number] = points
        setattr(self, data_type, time_series_record[frame_number] if time_series_record.get(frame_number) else [])

    def point3d_time_series_world(self, data_type, time_series_dict, frame_number):
        time_series_dict = deepcopy(time_series_dict)
        if not time_series_dict:
            return []
        frame_list = list(time_series_dict.keys())
        time_series_record = {}
        closest_down, closest_up = self.find_closest_values(frame_list, frame_number)
        if closest_down:
            if str(frame_number) in frame_list:
                if time_series_dict[str(frame_number)]['type'] == 'appear':
                    time_series_record[frame_number] = time_series_dict[str(frame_number)]['value']
            elif time_series_dict[closest_down]['type'] == 'appear' and (
                    time_series_dict[closest_up]['type'] == 'disappear' if closest_up else True):
                frame_coordinate = self.capture.get_world(self.capture.attachment[frame_number].get('coordinate')).I
                down_coordinate = self.capture.get_world(self.capture.attachment[int(closest_down)].get('coordinate'))
                rM = Matrix4.get_points_matrix(time_series_dict[closest_down]['value'], frame_coordinate)
                time_series_record[frame_number] = Matrix4.get_points_matrix(rM, down_coordinate)
            elif time_series_dict[closest_down]['type'] == 'appear' and time_series_dict[closest_up][
                'type'] == 'appear':
                down_coordinate = self.capture.get_world(self.capture.attachment[int(closest_down)].get('coordinate'))
                up_coordinate = self.capture.get_world(self.capture.attachment[int(closest_up)].get('coordinate'))
                rM = time_series_dict[closest_down]['value']
                lM = time_series_dict[closest_up]['value']
                _frame = [closest_down, closest_up, frame_number]

                rM_points = Matrix4.get_points_matrix(rM, down_coordinate)
                lM_points = Matrix4.get_points_matrix(lM, up_coordinate)
                time_series_record[frame_number] = {
                    'x': self.capture.inter_polate_number(*_frame, lM_points['x'], rM_points['x']),
                    'y': self.capture.inter_polate_number(*_frame, lM_points['y'], rM_points['y']),
                    'z': self.capture.inter_polate_number(*_frame, lM_points['z'], rM_points['z'])}
        setattr(self, data_type, time_series_record[frame_number] if time_series_record.get(frame_number) else [])

    def box2d_time_series(self, data_type, time_series_dict, frame_number):
        time_series_dict = deepcopy(time_series_dict)
        if not time_series_dict:
            return []
        frame_list = list(time_series_dict.keys())
        time_series_record = {}
        closest_down, closest_up = self.find_closest_values(frame_list, frame_number)
        if closest_down:
            if str(frame_number) in frame_list:
                if time_series_dict[str(frame_number)]['type'] == 'appear':
                    time_series_record[frame_number] = time_series_dict[str(frame_number)]['value']
            elif time_series_dict[closest_down]['type'] == 'appear' and (
                    time_series_dict[closest_up]['type'] == 'disappear' if closest_up else True):
                time_series_record[frame_number] = time_series_dict[closest_down]['value']

            elif time_series_dict[closest_down]['type'] == 'appear' and time_series_dict[closest_up][
                'type'] == 'appear':
                rM = time_series_dict[closest_down]['value']
                lM = time_series_dict[closest_up]['value']
                _frame = [closest_down, closest_up, frame_number]
                Matrix = {
                    'bottomLeft': {
                        'x': self.capture.inter_polate_number(*_frame, lM['bottomLeft']['x'], rM['bottomLeft']['x']),
                        'y': self.capture.inter_polate_number(*_frame, lM['bottomLeft']['y'],
                                                              rM['bottomLeft']['y'])},
                    'bottomRight': {
                        'x': self.capture.inter_polate_number(*_frame, lM['bottomRight']['x'], rM['bottomRight']['x']),
                        'y': self.capture.inter_polate_number(*_frame, lM['bottomRight']['y'], rM['bottomRight']['y'])},
                    'topLeft': {
                        'x': self.capture.inter_polate_number(*_frame, lM['topLeft']['x'], rM['topLeft']['x']),
                        'y': self.capture.inter_polate_number(*_frame, lM['topLeft']['y'], rM['topLeft']['y'])},
                    'topRight': {
                        'x': self.capture.inter_polate_number(*_frame, lM['topRight']['x'], rM['topRight']['x']),
                        'y': self.capture.inter_polate_number(*_frame, lM['topRight']['y'], rM['topRight']['y'])}
                }
                time_series_record[frame_number] = Matrix
        setattr(self, data_type, time_series_record[frame_number] if time_series_record.get(frame_number) else [])

    def vertices_time_series(self, data_type, time_series_dict, frame_number):
        time_series_dict = deepcopy(time_series_dict)
        if not time_series_dict:
            return []
        frame_list = list(time_series_dict.keys())
        time_series_record = {}
        closest_down, closest_up = self.find_closest_values(frame_list, frame_number)
        if closest_down:
            if str(frame_number) in frame_list:
                if time_series_dict[str(frame_number)]['type'] == 'appear':
                    time_series_record[frame_number] = time_series_dict[str(frame_number)]['value']
            elif time_series_dict[closest_down]['type'] == 'appear' and (
                    time_series_dict[closest_up]['type'] == 'disappear' if closest_up else True):
                time_series_record[frame_number] = time_series_dict[closest_down]['value']

            elif time_series_dict[closest_down]['type'] == 'appear' and time_series_dict[closest_up][
                'type'] == 'appear':
                rM = time_series_dict[closest_down]['value']
                lM = time_series_dict[closest_up]['value']
                _frame = [closest_down, closest_up, frame_number]
                vertices = []
                for s in range(len(rM)):
                    vertices.append({
                        'x': self.capture.inter_polate_number(*_frame, lM[s]['x'], rM[s]['x']),
                        'y': self.capture.inter_polate_number(*_frame, lM[s]['y'], rM[s]['y'])})
                time_series_record[frame_number] = vertices
        setattr(self, data_type, time_series_record[frame_number] if time_series_record.get(frame_number) else [])

    def points_time_series(self, data_type, time_series_dict, frame_number):
        time_series_dict = deepcopy(time_series_dict)
        if not time_series_dict:
            return []
        frame_list = list(time_series_dict.keys())
        time_series_record = {}
        closest_down, closest_up = self.find_closest_values(frame_list, frame_number)
        if closest_down:
            if str(frame_number) in frame_list:
                if time_series_dict[str(frame_number)]['type'] == 'appear':
                    time_series_record[frame_number] = time_series_dict[str(frame_number)]['value']
            elif time_series_dict[closest_down]['type'] == 'appear' and (
                    time_series_dict[closest_up]['type'] == 'disappear' if closest_up else True):
                time_series_record[frame_number] = time_series_dict[closest_down]['value']
            elif time_series_dict[closest_down]['type'] == 'appear' and time_series_dict[closest_up][
                'type'] == 'appear':
                rM = time_series_dict[closest_down]['value']
                lM = time_series_dict[closest_up]['value']
                _frame = [closest_down, closest_up, frame_number]
                points = []
                for s in range(len(rM)):
                    points.append({
                        'x': self.capture.inter_polate_number(*_frame, lM[s]['x'], rM[s]['x']),
                        'y': self.capture.inter_polate_number(*_frame, lM[s]['y'], rM[s]['y']),
                        'z': self.capture.inter_polate_number(*_frame, lM[s]['z'], rM[s]['z'])})
                time_series_record[frame_number] = points
        setattr(self, data_type, time_series_record[frame_number] if time_series_record.get(frame_number) else [])

    def point3d_time_series(self, data_type, time_series_dict, frame_number):
        time_series_dict = deepcopy(time_series_dict)
        if not time_series_dict:
            return []
        frame_list = list(time_series_dict.keys())
        time_series_record = {}
        closest_down, closest_up = self.find_closest_values(frame_list, frame_number)
        if closest_down:
            if str(frame_number) in frame_list:
                if time_series_dict[str(frame_number)]['type'] == 'appear':
                    time_series_record[frame_number] = time_series_dict[str(frame_number)]['value']
            elif time_series_dict[closest_down]['type'] == 'appear' and (
                    time_series_dict[closest_up]['type'] == 'disappear' if closest_up else True):
                time_series_record[frame_number] = time_series_dict[closest_down]['value']
            elif time_series_dict[closest_down]['type'] == 'appear' and time_series_dict[closest_up][
                'type'] == 'appear':
                rM = time_series_dict[closest_down]['value']
                lM = time_series_dict[closest_up]['value']
                _frame = [closest_down, closest_up, frame_number]
                time_series_record[frame_number] = {
                    'x': self.capture.inter_polate_number(*_frame, lM['x'], rM['x']),
                    'y': self.capture.inter_polate_number(*_frame, lM['y'], rM['y']),
                    'z': self.capture.inter_polate_number(*_frame, lM['z'], rM['z'])}
        setattr(self, data_type, time_series_record[frame_number] if time_series_record.get(frame_number) else [])

    def line_time_series(self, data_type, time_series_dict, frame_number):
        time_series_dict = deepcopy(time_series_dict)
        if not time_series_dict:
            return []
        frame_list = list(time_series_dict.keys())
        time_series_record = {}
        closest_down, closest_up = self.find_closest_values(frame_list, frame_number)
        if closest_down:
            if str(frame_number) in frame_list:
                if time_series_dict[str(frame_number)]['type'] == 'appear':
                    time_series_record[frame_number] = time_series_dict[str(frame_number)]['value']
            elif time_series_dict[closest_down]['type'] == 'appear' and (
                    time_series_dict[closest_up]['type'] == 'disappear' if closest_up else True):
                time_series_record[frame_number] = time_series_dict[closest_down]['value']

            elif time_series_dict[closest_down]['type'] == 'appear' and time_series_dict[closest_up][
                'type'] == 'appear':
                rM = time_series_dict[closest_down]['value']
                lM = time_series_dict[closest_up]['value']
                _frame = [closest_down, closest_up, frame_number]
                points = []
                if len(rM) == len(lM):
                    for s in range(len(rM)):
                        points.append({
                            'x': self.capture.inter_polate_number(*_frame, lM[s]['x'], rM[s]['x']),
                            'y': self.capture.inter_polate_number(*_frame, lM[s]['y'], rM[s]['y']),
                        })
                    time_series_record[frame_number] = points
                else:
                    time_series_record[frame_number] = rM
        setattr(self, data_type, time_series_record[frame_number] if time_series_record.get(frame_number) else [])

    def point_time_series(self, data_type, time_series_dict, frame_number):
        time_series_dict = deepcopy(time_series_dict)
        if not time_series_dict:
            return []
        frame_list = list(time_series_dict.keys())
        time_series_record = {}
        closest_down, closest_up = self.find_closest_values(frame_list, frame_number)
        if closest_down:
            if str(frame_number) in frame_list:
                if time_series_dict[str(frame_number)]['type'] == 'appear':
                    time_series_record[frame_number] = time_series_dict[str(frame_number)]['value']
            elif time_series_dict[closest_down]['type'] == 'appear' and (
                    time_series_dict[closest_up]['type'] == 'disappear' if closest_up else True):
                time_series_record[frame_number] = time_series_dict[closest_down]['value']

            elif time_series_dict[closest_down]['type'] == 'appear' and time_series_dict[closest_up][
                'type'] == 'appear':
                rM = time_series_dict[closest_down]['value']
                lM = time_series_dict[closest_up]['value']

                _frame = [closest_down, closest_up, frame_number]
                time_series_record[frame_number] = {
                    'x': self.capture.inter_polate_number(*_frame, lM['x'], rM['x']),
                    'y': self.capture.inter_polate_number(*_frame, lM['y'], rM['y'])}
        setattr(self, data_type, time_series_record[frame_number] if time_series_record.get(frame_number) else [])

    def cuboid_time_series(self, data_type, time_series_dict, frame_number):
        time_series_dict = deepcopy(time_series_dict)
        if not time_series_dict:
            return []
        frame_list = list(time_series_dict.keys())
        time_series_record = {}
        closest_down, closest_up = self.find_closest_values(frame_list, frame_number)
        if closest_down:
            if str(frame_number) in frame_list:
                if time_series_dict[str(frame_number)]['type'] == 'appear':
                    time_series_record[frame_number] = time_series_dict[str(frame_number)]['value']
            elif time_series_dict[closest_down]['type'] == 'appear' and (
                    time_series_dict[closest_up]['type'] == 'disappear' if closest_up else True):
                time_series_record[frame_number] = time_series_dict[closest_down]['value']

            elif time_series_dict[closest_down]['type'] == 'appear' and time_series_dict[closest_up][
                'type'] == 'appear':
                rM = time_series_dict[closest_down]['value']
                lM = time_series_dict[closest_up]['value']
                _frame = [closest_down, closest_up, frame_number]
                Matrix = {
                    'front': {
                        'bottomLeft': {
                            'x': self.capture.inter_polate_number(*_frame, lM['front']['bottomLeft']['x'],
                                                                  rM['front']['bottomLeft']['x']),
                            'y': self.capture.inter_polate_number(*_frame, lM['front']['bottomLeft']['y'],
                                                                  rM['front']['bottomLeft']['y'])},
                        'bottomRight': {
                            'x': self.capture.inter_polate_number(*_frame, lM['front']['bottomRight']['x'],
                                                                  rM['front']['bottomRight']['x']),
                            'y': self.capture.inter_polate_number(*_frame, lM['front']['bottomRight']['y'],
                                                                  rM['front']['bottomRight']['y'])},
                        'topLeft': {
                            'x': self.capture.inter_polate_number(*_frame, lM['front']['topLeft']['x'],
                                                                  rM['front']['topLeft']['x']),
                            'y': self.capture.inter_polate_number(*_frame, lM['front']['topLeft']['y'],
                                                                  rM['front']['topLeft']['y'])},
                        'topRight': {
                            'x': self.capture.inter_polate_number(*_frame, lM['front']['topRight']['x'],
                                                                  rM['front']['topRight']['x']),
                            'y': self.capture.inter_polate_number(*_frame, lM['front']['topRight']['y'],
                                                                  rM['front']['topRight']['y'])}},
                    'back': {
                        'bottomLeft': {
                            'x': self.capture.inter_polate_number(*_frame, lM['back']['bottomLeft']['x'],
                                                                  rM['back']['bottomLeft']['x']),
                            'y': self.capture.inter_polate_number(*_frame, lM['back']['bottomLeft']['y'],
                                                                  rM['back']['bottomLeft']['y'])},
                        'bottomRight': {
                            'x': self.capture.inter_polate_number(*_frame, lM['back']['bottomRight']['x'],
                                                                  rM['back']['bottomRight']['x']),
                            'y': self.capture.inter_polate_number(*_frame, lM['back']['bottomRight']['y'],
                                                                  rM['back']['bottomRight']['y'])},
                        'topLeft': {
                            'x': self.capture.inter_polate_number(*_frame, lM['back']['topLeft']['x'],
                                                                  rM['back']['topLeft']['x']),
                            'y': self.capture.inter_polate_number(*_frame, lM['back']['topLeft']['y'],
                                                                  rM['back']['topLeft']['y'])},
                        'topRight': {
                            'x': self.capture.inter_polate_number(*_frame, lM['back']['topRight']['x'],
                                                                  rM['back']['topRight']['x']),
                            'y': self.capture.inter_polate_number(*_frame, lM['back']['topRight']['y'],
                                                                  rM['back']['topRight']['y'])}},
                }
                time_series_record[frame_number] = Matrix
        setattr(self, data_type, time_series_record[frame_number] if time_series_record.get(frame_number) else [])


class Input(UtilityCategory):
    """input"""

    def __init__(self, data, frame_number):
        super().__init__(data)
        self.key = data['key']
        self.target = frame_number
        if data['input'].get('timeSeries'):
            _ = data['input']
            self.frame_list = np.array(list(_['timeSeries'].keys()), dtype=int).tolist()
            temp = str(self.frame_list[-1])
            if _['timeSeries'][temp]['type'] == 'appear' and self.target >= self.frame_list[-1]:
                self.input = {
                    'type': _['type'],
                    'value': _['timeSeries'][temp]['value']
                }
                if (a := _['timeSeries'][temp].get("teamId", None)):
                    self.input['teamId'] = a
            elif _['timeSeries'][temp]['type'] == 'disappear' and self.target >= self.frame_list[-1]:
                self.input = {
                    'type': _['type'],
                }
            else:
                if self.target in self.frame_list:
                    input_value = _['timeSeries'][str(self.target)].get("value")
                    self.input = {
                        'type': _['type'],
                        'value': input_value if input_value else ""
                    }
                    if (a := _['timeSeries'][temp].get("teamId", None)):
                        self.input['teamId'] = a
                else:
                    self.input = self.time_series(_)
        else:
            self.input = data['input']

    def time_series(self, time_series_dict):
        left, right = FrameCapture.binary_search(self.frame_list, self.target)
        if time_series_dict['timeSeries'][str(left)]['type'] == 'appear':
            return {
                'type': time_series_dict['type'],
                'value': time_series_dict['timeSeries'][str(left)]['value']
            }
        else:
            return {
                'type': time_series_dict['type']}
