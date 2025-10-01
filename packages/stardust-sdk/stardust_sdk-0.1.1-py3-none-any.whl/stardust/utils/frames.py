import os
import re
import math
import numpy as np
from numpy.linalg import norm
from typing import Optional, Union

from stardust.components.ego import Ego


class Vector(np.ndarray):
    def __new__(cls, x=0, y=0, z=0):
        obj = np.array([x, y, z]).view(cls)
        return obj

    def sub(self, other):
        return self - other

    def add(self, other):
        return self + other

    def distance_to_squared(self, other):
        return np.sum((self - other) ** 2)


class Line:
    def __init__(self, start, end):
        self.start = Vector(*start)
        self.end = Vector(*end)

    def clone(self):
        return Line3(self.start, self.end)

    def delta(self):
        return self.end.sub(self.start)


class Plane:
    def __init__(self, normal, constant):
        self.normal = normal  # Surface normal
        self.constant = constant  # Distance from origin to any point on the plane

    def clone(self):
        return Plane(np.copy(self.normal), self.constant)

    def apply_matrix4(self, matrix):
        # Extract the 3x3 normal matrix and compute its inverse transpose
        normal_matrix = np.linalg.inv(matrix[:3, :3]).T
        # Transform and normalize the normal vector
        transformed_normal = normal_matrix @ self.normal
        # Select a point on the plane (along the normal at the stored distance)
        point_on_plane = self.normal * -self.constant
        # Update normal vector
        self.normal = transformed_normal / np.linalg.norm(transformed_normal)
        # Promote the point to homogeneous coordinates
        point_on_plane_homogeneous = np.append(point_on_plane, 1.0)
        # Transform the point
        transformed_point_homogeneous = matrix @ point_on_plane_homogeneous
        # Update the distance from the origin to the plane
        self.constant = -np.dot(self.normal, transformed_point_homogeneous[:3])

        return self

    def distance_to_point(self, point):
        return np.dot(self.normal, point) + self.constant

    def intersect_line(self, line, direction):
        # Compute dot product between the plane normal and line direction
        denominator = np.dot(self.normal, direction)
        if denominator == 0:
            if self.distance_to_point(line.start) == 0:
                return line.start
            return None
        k = -(np.dot(line.start, self.normal) + self.constant) / denominator
        if k < 0 or k > 1:
            return None
        return line.start + direction * k

    def __str__(self):
        return f'normal:{self.normal},constant:{self.constant}'


# Default to True for non-slot structures (inputs have no children)
def empty(slot: dict) -> bool:
    if slot['type'] == 'slotChildren':
        return not slot['slotsChildren']
    elif slot['type'] == 'childrenOnly':
        return not slot['childrenOnly']
    elif slot['type'] == 'slot':
        return not slot['slots']
    else:
        return True


def frame_name(file_name: str, frame_number: Optional[int] = None) -> str:
    timestamp_pattern = r'_\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}[+-]\d{2}:\d{2}'
    file_name = os.path.splitext(file_name)[0]
    if frame_number is not None:
        new_file_name = f'{re.sub(timestamp_pattern, "", file_name)}_{str(frame_number).rjust(4, "0")}.json'
    else:
        new_file_name = f'{re.sub(timestamp_pattern, "", file_name)}.json'
    # return new_file_name.replace('Downloads', 'Desktop')
    return new_file_name


def frame_key(key: str) -> dict:
    if key == 'slotChildren':
        return {'slotsChildren': []}
    elif key == 'childrenOnly':
        return {'childrenOnly': []}
    elif key == 'slot':
        return {'slots': []}


def slot_structure(slot: dict) -> dict:
    type_ = slot['type']
    _ = {
        'key': slot['key'],
        'label': slot['label'],
        'type': type_,
    }
    if slot.get("teamId", None):
        _['teamId'] = slot.get("teamId")

    if not type_ == 'input':
        _.update(frame_key(type_))
    else:
        try:
            _['input'] = {'type': slot['input']['type']}
        except KeyError:
            _['input'] = {'type': slot['inputSpecification']['type']}
    return _


def binary_search(lst: list, target: int) -> tuple:
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


def inter_polate_number(left_index: int, right_index: int, target: int, right, left):
    return left + ((right - left) / (right_index - left_index)) * (target - left_index)


def angle_closer_to(left_rotation: float, right_rotation: float):
    if left_rotation - right_rotation > math.pi:
        return right_rotation + 2 * math.pi
    if left_rotation - right_rotation < -math.pi:
        return right_rotation - 2 * math.pi
    return right_rotation


def get_world(coordinate: dict):
    ego_heading = coordinate["egoHeading"]
    ego_position = coordinate["ego"]
    ego = Ego(
        heading=(ego_heading['x'], ego_heading['y'], ego_heading['z'], ego_heading['w']),
        position=(ego_position['x'], ego_position['y'], ego_position['z'])
    )
    return ego.ego_rt


def point3d_to_world(point3d: list, coordinate: dict, overturn: bool = False):
    assert coordinate, 'coordinate must not be empty'
    world = get_world(coordinate)
    matrix = np.array([[point['x'], point['y'], point['z'], 1] for point in point3d])
    if overturn:
        point3ds_world = np.dot(matrix, world.I)  # Transform to the sensor coordinate system
    else:
        point3ds_world = np.dot(matrix, world)  # Transform to the global coordinate system
    point3ds_world = point3ds_world[:, :3] / point3ds_world[:, 3]
    return [dict(zip('xyz', point)) for point in point3ds_world.tolist()]


def box3d_to_world(box3d: list, coordinate: dict, overturn: bool = False):
    assert coordinate, 'coordinate must not be empty'
    world = get_world(coordinate)
    matrix = np.array(box3d).reshape(4, 4).T
    if overturn:
        point3ds_world = np.dot(matrix, world.I)  # Transform to the sensor coordinate system
    else:
        point3ds_world = np.dot(matrix, world)  # Transform to the global coordinate system
    return np.array(point3ds_world.T).flatten().tolist()


def make_rotation_z(theta: float):
    # Build a 4x4 rotation matrix around the Z axis
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [c, -s, 0, 0],
        [s, c, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def point_angle(point: dict):
    x, _, z = point.values()
    angle = np.arccos(np.abs(x) / np.sqrt(x ** 2 + z ** 2))
    return angle * (z / np.abs(z))


def check_point_in_camera(point: dict, theta_length: float) -> bool:
    angle = point_angle(point)
    min_z, max_z = 0.5, 100
    if -max_z < point['z'] < min_z:
        return False
    if point['z'] > max_z or point['z'] < -max_z:
        return False
    if theta_length * 2 < np.pi:
        return np.pi - theta_length < angle * 2 < np.pi + theta_length
    else:
        return np.pi - angle * 2 <= theta_length


if __name__ == '__main__':
    name = [
        0.08573903915964579,
        -1.385659579033742,
        0,
        0,
        2.0921314438311733,
        0.1294526754651037,
        0,
        0,
        0,
        0,
        1.268364013474737,
        0,
        -3.058281007163033,
        2.165372077096646,
        1.6431105252136202,
        1
    ]
    coord = {
        "ego": {
            "x": 2.1812003147458467,
            "y": -0.19653660649169938,
            "z": -0.10265531758175112
        },
        "egoHeading": {
            "x": -0.0115017067585349,
            "y": 0.0016873531021340058,
            "z": -0.014199167104915787,
            "w": 0.9998316094396476
        }
    }
    res = box3d_to_world(name, coord)
    print(res)
