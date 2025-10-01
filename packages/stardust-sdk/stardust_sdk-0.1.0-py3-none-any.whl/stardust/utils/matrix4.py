import math
from copy import deepcopy
from typing import List, Dict

import open3d as o3d
import numpy as np
from scipy.spatial.transform import Rotation as R


class Matrix4(object):
    def __init__(self, box: tuple):
        self.box = box
        self.te = deepcopy(np.array(self.box).reshape(4, 4))
        self._determinant = np.linalg.det(self.te.T)
        self.sx = np.sqrt(np.sum(self.te[:1, :3].flatten() ** 2))
        self.sy = np.sqrt(np.sum(self.te[1:2, :3].flatten() ** 2))
        self.sz = np.sqrt(np.sum(self.te[2:3, :3].flatten() ** 2))
        if self._determinant < 0:
            self.sx = -self.sx
        else:
            self.sx = self.sx

    def to_position(self):
        return dict(zip('xyz', self.te.T[:3, 3:].flatten().tolist()))

    def to_rotation(self):
        inv_sx = 1 / self.sx
        inv_sy = 1 / self.sy
        inv_sz = 1 / self.sz

        _ = np.reshape([inv_sx, inv_sy, inv_sz], [-1, 1])
        m = np.multiply(self.te[:3, :3], _)

        euler = R.from_matrix(m.T).as_euler("XYZ", degrees=False).tolist()
        return dict(zip('xyz', euler))

    def to_scale(self):
        return {
            "length": self.sx,
            "width": self.sy,
            "height": self.sz
        }

    @property
    def box_info(self):
        return {
            "position": self.to_position(),
            "scale": self.to_scale(),
            "rotation": self.to_rotation()
        }

    @classmethod
    def get_transform_matrix(cls, box: Dict):
        position = box['position']
        scale = box['scale']
        rotation = [box['rotation'][key] for key in ['x', 'y', 'z']]

        # Compute the rotation matrix
        rx, ry, rz = rotation
        cx, cy, cz = np.cos(rx), np.cos(ry), np.cos(rz)
        sx, sy, sz = np.sin(rx), np.sin(ry), np.sin(rz)
        rotation_matrix = np.array([[cy * cz, -cy * sz, sy, 0],
                                    [cx * sz + cz * sx * sy, cx * cz - sx * sy * sz, -cy * sx, 0],
                                    [sx * sz - cx * cz * sy, cx * sz * sx + cz * sy, cx * cy, 0],
                                    [0, 0, 0, 1]])

        # Compute the scaling matrix
        scale_matrix = np.eye(4)
        scale_matrix[0, 0] = scale['length']
        scale_matrix[1, 1] = scale['width']
        scale_matrix[2, 2] = scale['height']

        # Compute the translation matrix
        translation_matrix = np.eye(4)
        translation_matrix[:3, 3] = [position['x'], position['y'], position['z']]

        # Compose the full transform matrix
        transform_matrix = np.matmul(translation_matrix, np.matmul(rotation_matrix, scale_matrix))
        transform_matrix = transform_matrix.T

        # Flatten to a 1D list
        transform_list = transform_matrix.flatten().tolist()

        return transform_list

    @classmethod
    def get_points_matrix(cls, box_info: Dict, rt: np.matrix):
        # Convert point P into homogeneous coordinates
        box_info = [box_info['x'], box_info['y'], box_info['z']]
        p_homogeneous = np.hstack([box_info, 1])
        # Apply the affine transform
        p_homogeneous_transformed = np.dot(rt, p_homogeneous)
        p_transformed = p_homogeneous_transformed[:3] / p_homogeneous_transformed[3]

        # Return the transformed coordinates
        return dict(zip("xyz", p_transformed))

    @classmethod
    def get_3dbox_matrix(cls, box_info: Dict, rt: np.matrix):
        center = [box_info['position']['x'], box_info['position']['y'], box_info['position']['z']]  # Center point
        extent = [box_info['scale']['height'], box_info['scale']['width'], box_info['scale']['depth']]  # Extent per axis
        theta = [box_info['rotation']['x'], box_info['rotation']['y'], box_info['rotation']['z']]  # Euler angles
        # Convert Euler angles to rotation matrix

        r = R.from_euler('xyz', theta)
        rot_mat = r.as_matrix()
        bbox = o3d.geometry.OrientedBoundingBox(center=center, R=rot_mat, extent=extent)
        r1 = np.array(rt)
        bbox.rotate(r1[:3, :3])
        bbox.translate(r1[:3, 3:].reshape(-1))
        euler = R.from_matrix(bbox.R.copy()).as_euler("XYZ", degrees=False).tolist()
        # Package center, dimensions, and Euler angles

        box = {
            'position': {
                'x': bbox.center[0],
                'y': bbox.center[1],
                'z': bbox.center[2]},
            'scale': {
                'height': bbox.extent[0],
                'width': bbox.extent[1],
                'depth': bbox.extent[2]},
            'rotation': {
                'x': euler[0],
                'y': euler[1],
                'z': euler[2],
                '_order': 'XYZ'}}

        return box

    @classmethod
    def euler_to_rotation_matrix(cls, euler_angles):
        roll, pitch, yaw = euler_angles
        x = np.array([[1, 0, 0],
                      [0, np.cos(roll), -np.sin(roll)],
                      [0, np.sin(roll), np.cos(roll)]])
        y = np.array([[np.cos(pitch), 0, np.sin(pitch)],
                      [0, 1, 0],
                      [-np.sin(pitch), 0, np.cos(pitch)]])
        z = np.array([[np.cos(yaw), -np.sin(yaw), 0],
                      [np.sin(yaw), np.cos(yaw), 0],
                      [0, 0, 1]])
        r = np.dot(z, np.dot(y, x))
        return r

    @classmethod
    def get_3dbox_same_frame(cls, box_info, coordinate):
        center = [box_info['position']['x'], box_info['position']['y'], box_info['position']['z'], 1]  # Center point
        theta = [0, 0, box_info['rotation']['z']]  # Euler angles
        # Convert Euler angles to rotation matrix

        center = np.array(center)
        center_new = np.dot(center, coordinate.T).tolist()[0]

        _ = cls.euler_to_rotation_matrix(theta)
        r = np.dot(_, coordinate[:3, :3])

        _, _, rz_new = R.from_matrix(r).as_euler('xyz')

        box = {
            'position': {
                'x': center_new[0],
                'y': center_new[1],
                'z': center_new[2]},
            'scale': box_info['scale'],
            'rotation': {
                'x': 0,
                'y': 0,
                'z': rz_new,
                '_order': 'XYZ'}}

        return box

    @staticmethod
    def to_matrix4d(cx, cy, cz, dx, dy, dz, heading):
        """
        7 number Matrix4
        :param cx:
        :param cy:
        :param cz:
        :param dx: Length in the x direction   width
        :param dy: Length in the y direction   height
        :param dz: Length in the z direction
        :param heading: yaw angle; 0 on the positive x-axis, positive counter-clockwise
        :return:
        """
        alpha, beta, gamma = 0, 0, heading  # TODO: pitch, roll, yaw
        x = math.cos(alpha / 2) * math.sin(beta / 2) * math.cos(gamma / 2) + math.sin(alpha / 2) * math.cos(
            beta / 2) * math.sin(gamma / 2)
        y = math.sin(alpha / 2) * math.cos(beta / 2) * math.cos(gamma / 2) - math.cos(alpha / 2) * math.sin(
            beta / 2) * math.sin(gamma / 2)
        z = -math.sin(alpha / 2) * math.sin(beta / 2) * math.cos(gamma / 2) + math.cos(alpha / 2) * math.cos(
            beta / 2) * math.sin(gamma / 2)
        w = math.cos(alpha / 2) * math.cos(beta / 2) * math.cos(gamma / 2) + math.sin(alpha / 2) * math.sin(
            beta / 2) * math.sin(gamma / 2)

        x2 = x + x
        y2 = y + y
        z2 = z + z

        xx = x * x2
        xy = x * y2
        xz = x * z2

        yy = y * y2
        yz = y * z2
        zz = z * z2

        wx = w * x2
        wy = w * y2
        wz = w * z2

        sx, sy, sz = dy, dx, dz

        te = [0] * 16
        te[0] = (1 - (yy + zz)) * sx
        te[1] = (xy + wz) * sx
        te[2] = (xz - wy) * sx
        te[3] = 0

        te[4] = (xy - wz) * sy
        te[5] = (1 - (xx + zz)) * sy
        te[6] = (yz + wx) * sy
        te[7] = 0

        te[8] = (xz + wy) * sz
        te[9] = (yz - wx) * sz
        te[10] = (1 - (xx + yy)) * sz
        te[11] = 0

        te[12] = cx
        te[13] = cy
        te[14] = cz
        te[15] = 1

        return te


if __name__ == '__main__':
    res = Matrix4((-1.8629903392376739, -0.07255098381334309, 0, 0, 0.180460797718889, -4.633937475284563, 0, 0, 0, 0,
                   1.630792052527909, 0, -11.792962546858156, -12.32071494109367, 0.963595499026534, 1)).box_info
    print(res)
    res1 = Matrix4.get_transform_matrix(res)
    print(res1)
