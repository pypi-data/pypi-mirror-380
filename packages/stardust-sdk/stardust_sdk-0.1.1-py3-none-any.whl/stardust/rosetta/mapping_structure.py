import numpy as np

from stardust.utils.frames import *
from stardust.utils.matrix4 import *


class SlotMapping:
    attr_map = {
        'point': 'point',
        'line': 'vertices',
        'splines': 'vertices',
        'polygon': 'vertices',
        'box2d': 'plane',
        'cuboid': 'vertices',
    }

    @classmethod
    def preposition(cls, data, father, frame_number, image_source):
        cls.target = frame_number
        cls.father = father
        cls.camera, cls.width, cls.height = image_source[data['source']].values()
        cls.time_series = data.get('timeSeries', {})
        if cls.time_series:
            cls.frame_list = np.array(list(cls.time_series.keys()), dtype=int).tolist()

    def __init__(self, data, father, frame_number, image_source):
        self.preposition(data, father, frame_number, image_source)
        for n in ['id', 'label', 'teamId', 'source', 'coordinate']:
            if data.get(n):
                setattr(self, n, data[n])
        self.type = data['type']
        commonality_result = self.commonality()
        if callable(commonality_result):
            if isinstance(commonality_result()(), bool):
                self.label = True
            setattr(self, self.attr_map[self.type], commonality_result()())
        else:
            if isinstance(commonality_result, bool):
                self.label = True
            setattr(self, self.attr_map[self.type], commonality_result)

    def commonality(self):
        if self.time_series and self.target in self.frame_list:
            if self.time_series[str(self.target)]['type'] == "disappear":
                return True
            else:
                input_value = self.time_series[str(self.target)].get("value")
                return input_value
        else:
            if isinstance(self.father.label, bool):
                return True
            else:
                return self.slot_factory

    def slot_factory(self):
        return {
            'point': self.point_mapping,
            'line': self.line_mapping,
            'splines': self.line_mapping,
            'polygon': self.line_mapping,
            'box2d': self.box2d_mapping,
            'cuboid': self.cuboid_mapping,
        }[self.type]

    def camera_indicator_info(self, pint_cloud_map_scope=None):
        """
            Camera coverage information
        """
        vx, vy, vz = self.camera.rotated_vector

        angle_x = np.arctan2(vy, vz) + (np.pi if vz < 0 else 0)
        angle_y = np.arctan2(vx, vz) + (np.pi if vy < 0 else 0)
        angle_z = np.arctan2(vy, vx) + (np.pi if vx < 0 else 0)

        adjustable_width = self.width * (pint_cloud_map_scope if pint_cloud_map_scope else 1)
        fx = self.camera.intrinsic[0]
        fx_with_width_proportion = fx / self.width
        _ = np.arctan(adjustable_width / 2 / fx / fx_with_width_proportion)

        result = {
            'position': self.camera.position,
            'rotation': dict(zip('xyz', (angle_x, angle_y, angle_z))),
            'thetaStart': np.pi / 2 - _,
            'thetaLength': 2 * _,
        }

        if self.camera.fov:
            theta_length = np.deg2rad(fov)
            result['thetaStart'] -= (theta_length - result['thetaLength']) / 2
            result['thetaLength'] = theta_length

        return result

    def point_in_camera(self, point):
        vector3d = np.array([point['x'], point['y'], point['z'], 1])
        return dict(zip('xyz', np.array(np.dot(self.camera.cam2lidar_rt.I, vector3d))[0, :3]))

    def pixel_coordinate(self, point):
        return dict(zip('xy', self.camera.get_pixel_coordinate(point)))

    # 2D point
    def point_mapping(self):
        father_data = self.father['point']
        son_data = self.point_in_camera(father_data)
        if son_data['z'] < 0 and (self.camera.fov is None or self.camera.fov < 180):
            return True
        return self.pixel_coordinate(son_data)

    def intersection(self, point1, point2, translation, plane1, plane2):
        v1, v2 = Vector(*point1).sub(translation), Vector(*point2).sub(translation)
        line = Line(v1, v2)
        direction = line.delta()
        result1 = intersect1 = plane1.intersect_line(line.clone(), direction)
        result2 = intersect2 = plane2.intersect_line(line.clone(), direction)
        if not intersect1 and not intersect2:
            return None
        if not intersect2 or result1.distance_to_squared(v1) < result2.distance_to_squared(v1):
            return self.point_in_camera(result1.add(translation))
        return self.point_in_camera(result2.add(translation))

    # 2D line, curve, or polygon
    def line_mapping(self):
        father_data = self.father['points']
        if not father_data:
            return True
        position, rotation, theta_start, theta_length = self.camera_indicator_info().values()
        plane = Plane(np.array([0, np.pi, 0]), 0)
        plane1 = plane.clone().apply_matrix4(make_rotation_z(theta_start + rotation['z']))
        plane2 = plane.clone().apply_matrix4(make_rotation_z(theta_start + theta_length + rotation['z']))
        filtered_points = [self.point_in_camera(p) for p in father_data if p['z'] != 0]  # Drop z == 0 points
        pairs = [(a, b) for a, b in zip(filtered_points, filtered_points[1:])]
        result = []
        for num, (pre, cur) in enumerate(pairs):
            pre_in, cur_in = check_point_in_camera(pre, theta_length), check_point_in_camera(cur, theta_length)
            if pre_in and cur_in:
                if num == 0:
                    result.append(self.pixel_coordinate(pre))
                result.append(self.pixel_coordinate(cur))
            elif not pre_in and cur_in:
                result.append(self.pixel_coordinate(self.intersection(pre, cur, Vector(*position), plane1, plane2)))
            elif pre_in and not cur_in:
                result.append(self.pixel_coordinate(self.intersection(pre, cur, Vector(*position), plane1, plane2)))
                break
        if not result:
            return True
        return result

    # 2D box
    def box2d_mapping(self):
        father_data = self.father['matrix']
        pass

    # 2D projection of a cuboid
    def cuboid_mapping(self):
        father_data = self.father['matrix']
        pass


if __name__ == '__main__':
    import numpy as np

    # Create a vector
    # vector = np.array([1, 2, 3, 1])  # Use a 4D vector (homogeneous coordinate) for 4x4 transforms
    #
    # # Create an identity matrix representing no transformation
    # matrix = np.matrix([[0.9995910729860709, 0.02835473731726321, 0.003700767248111604, 2.1812003147458467],
    #                     [-0.02843236707957861, 0.9993321887903348, 0.022951621942053253, -0.19653660649169938],
    #                     [-0.003047508623086898, -0.023047457976702046, 0.9997297271622989, -0.10265531758175112],
    #                     [0.0, 0.0, 0.0, 1.0]])
    #
    # transformed_vector = dict(zip('xyz', np.array(np.dot(matrix.I, vector))[0, :3]))
    # print(f"Transformed Vector: {transformed_vector}")
    # transformed_vector = np.dot(vector, matrix.I.T)
    # print(f"Transformed Vector: {transformed_vector}")
    # np.dot(matrix.I, vector) == np.dot(vector, matrix.I.T)
