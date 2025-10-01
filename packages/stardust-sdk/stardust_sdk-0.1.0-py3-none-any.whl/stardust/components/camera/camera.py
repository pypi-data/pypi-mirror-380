from enum import Enum
from typing import Optional
from scipy.spatial.transform import Rotation
import numpy as np
from typing import Dict
import math
import open3d as o3d


class CameraType(Enum):
    PinHole = "PinHole"
    Fisheye = "Fisheye"
    OmniDirectional = "OmniDirectional"

    @classmethod
    def camera_type_list(cls) -> list:
        return [_.value for _ in CameraType]


class Camera:
    def __init__(self,
                 camera_type: str,
                 heading: Optional[tuple] = None,
                 position: Optional[tuple] = None,
                 intrinsic: Optional[tuple] = None,
                 radial: Optional[tuple] = None,
                 tangential: Optional[tuple] = None,
                 fov: Optional[int] = None,
                 skew: Optional[int] = 0,
                 projection: Optional[tuple] = None,
                 name: str = None
                 ):
        """
        camera object

        Args:
            camera_type:
                Pinholes, fish eyes, panoramic views
            heading:
                quaternion (x, y, z, w)
            position:
                offset (x, y, z)
            intrinsic:
                camera parameter (fx, fy, cx, cy) or (fx, fy, c, d, e, cx, cy)
            radial:
                radial distortion (k1...)
            tangential:
                tangential distortion (p1...)
            fov:
                camera range (angle system)
            projection:
                panoramic camera parameters (p0...)

        Returns:
            Camera inatance

        Examples:
            .. code-block:: python

                cam = Camera(
                    'PinHole',
                    heading=(0.4351436321314605, -0.4677553765588058, 0.5492505771794342, -0.5386824023335351),
                    position=(1.5601294, -0.37986112, 1.3333596),
                    intrinsic=(1846.008599353862, 1857.930995475229, 1948.09353722228, 1078.768188621484),
                    radial=(0, 0, 0, 0),
                    tangential=(0, 0)
                )

        """
        camera_type_list = CameraType.camera_type_list()
        assert camera_type in camera_type_list, f'camera_type is one of "{" ".join(camera_type_list)}"'
        self.camera_type = camera_type
        self.heading = heading
        self.position = position
        self.intrinsic = intrinsic
        self.name = name
        if camera_type == CameraType.OmniDirectional.value:
            assert len(self.intrinsic) == 7, 'intrinsic is fx, fy, c, d, e, cx, cy'
        else:
            assert len(self.intrinsic) == 4, 'intrinsic is fx, fy, cx, cy'
        self.radial = radial
        self.tangential = tangential
        self.fov = fov
        self.projection = projection
        self.skew = skew

    def __repr__(self):
        return "the camera param"

    @property
    def rotated_vector(self):
        """
            Extract the x, y, and z components of the rotated vector
        """
        additional_rotation = R.from_quat(self.heading)
        # Create a vector initially aligned with the x-axis
        vector = np.array([1.0, 0.0, 0.0])
        rotated_vector = additional_rotation.apply(vector)
        return rotated_vector

    @property
    def cam2lidar_rt(self) -> np.matrix:
        """
        Camera rt matrix relative to radar
        """
        r = Rotation.from_quat(self.heading).as_matrix()
        rt = np.r_[np.c_[r, np.array(self.position)], np.array([[0, 0, 0, 1]])]
        return np.matrix(rt)

    @property
    def intrinsic_matrix(self) -> Optional[np.ndarray]:
        """
        Internal parameter matrix of pinhole and fisheye cameras
        """
        if self.camera_type != CameraType.OmniDirectional.value:
            fx, fy, cx, cy = self.intrinsic
            return np.array([
                [fx, 0, cx],
                [0, fy, cy],
                [0, 0, 1]])
        else:
            return None

    @property
    def _radial(self) -> tuple:
        """
        Transverse distortion
        """
        assert len(self.radial) <= 6, 'The radial distortion of this model only supports k1-k6 at present'
        _ = {f'k{num}': item for num, item in enumerate(self.radial, start=1)}
        k1 = _.get('k1', 0)
        k2 = _.get('k2', 0)
        k3 = _.get('k3', 0)
        k4 = _.get('k4', 0)
        k5 = _.get('k5', 0)
        k6 = _.get('k6', 0)
        return k1, k2, k3, k4, k5, k6

    def _pinhole_3dto2d(self, **kwargs) -> tuple:
        """
        opencv pinhole camera pixel coordinates
        """
        x, y, z = kwargs['point_in_cam']
        fx, fy, cx, cy = self.intrinsic
        k1, k2, k3, k4, k5, k6 = self._radial
        p1, p2 = self.tangential
        u, v = x / z, y / z
        r2 = u ** 2 + v ** 2
        r4 = r2 ** 2
        r6 = r2 * r4
        radial = (1 + k1 * r2 + k2 * r4 + k3 * r6) / (1 + k4 * r2 + k5 * r4 + k6 * r6)
        u = u * radial + 2 * p1 * v * u + p2 * (r2 + 2 * u ** 2)
        v = v * radial + 2 * p2 * v * u + p1 * (r2 + 2 * v ** 2)
        return u * fx + cx, v * fy + cy

    # opencv
    def _fisheye_3dto2d(self, **kwargs) -> tuple:
        """
        opencv fisheye camera pixel coordinates
        """
        x, y, z = kwargs['point_in_cam']
        fx, fy, cx, cy = self.intrinsic
        k1, k2, k3, k4, k5, k6 = self._radial
        alpha = self.skew
        a = x / abs(z)
        b = y / abs(z)
        r2 = a ** 2 + b ** 2
        r = math.sqrt(r2)
        theta = math.atan(r) if z > 0 else math.pi - math.atan(r)

        theta2 = theta ** 2
        theta4 = theta2 ** 2
        theta6 = theta2 * theta4
        theta8 = theta4 ** 2

        theta_d = theta * (1.0 + k1 * theta2 + k2 * theta4 + k3 * theta6 + k4 * theta8)
        scale = 1.0 / r if r > 1e-8 else 1.0

        u, v = theta_d * scale * a, theta_d * scale * b
        return fx * (u + alpha * v) + cx, fy * v + cy

    # kb8
    def _fisheye2_3dto2d(self, **kwargs) -> tuple:
        """
        kb8 fisheye camera pixel coordinates
        """
        x, y, z = kwargs['point_in_cam']
        fx, fy, cx, cy = self.intrinsic
        k1, k2, k3, k4, k5, k6 = self._radial
        alpha = self.skew
        a = x / abs(z)
        b = y / abs(z)
        r2 = a ** 2 + b ** 2
        r = math.sqrt(r2)
        theta = math.atan(r) if z > 0 else math.pi - math.atan(r)

        theta2 = theta ** 2
        theta4 = theta2 ** 2
        theta6 = theta2 * theta4
        theta8 = theta4 ** 2

        theta_d = theta * (1.0 + k1 * theta2 + k2 * theta4 + k3 * theta6 + k4 * theta8)
        scale = 1.0 / r if r > 1e-8 else 1.0

        u, v = theta_d * scale * a, theta_d * scale * b
        return fx * (u + alpha * v) + cx, fy * v + cy

    def _omnidirectional_3dto2d(self, **kwargs) -> tuple:
        """
        opencv omnidirectional camera pixel coordinates
        """
        x, y, z = kwargs['point_in_cam']
        fx, fy, c, d, e, cx, cy = self.intrinsic
        norm = math.sqrt(x * x + y * y)
        theta = math.atan2(-z, norm)
        theta_i, rho = 1, 0
        for pi in self.projection:
            rho += theta_i * pi
            theta_i *= theta
        inv_norm = 1 / norm
        xn1, xn2 = x * inv_norm * rho, y * inv_norm * rho
        return xn1 * c + xn2 * d + cx, xn1 * e + xn2 + cy

    def get_pixel_coordinate(self, point_in_cam: tuple) -> tuple:
        """
        Convert point cloud points to pixel coordinates

        Args:
            point_in_cam: (x, y, z)
                The coordinates of points in the camera coordinate system
        """
        if self.camera_type == CameraType.PinHole.value:
            return self._pinhole_3dto2d(point_in_cam=point_in_cam)
        elif self.camera_type == CameraType.Fisheye.value:
            return self._fisheye_3dto2d(point_in_cam=point_in_cam)
        else:
            return self._omnidirectional_3dto2d(point_in_cam=point_in_cam)

    @staticmethod
    def gen_camera(camera: Dict):
        """
        generate the Camera obj

        Args:
            camera: Dict
                camera data
        Returns:
            obj: Camera
        """

        def _temp_cam(data: Dict):
            if not data:
                return
            if isinstance(data, Dict):
                return tuple(data.values())
            return data

        camera_type = _temp_cam(camera.get("type"))
        assert isinstance(camera_type, str)
        return Camera(camera_type=_temp_cam(camera.get("type")),
                      heading=_temp_cam(camera.get("heading", None)),
                      position=_temp_cam(camera.get("position", None)),
                      intrinsic=_temp_cam(camera.get("intrinsic", None)),
                      radial=_temp_cam(camera.get("radial", None)),
                      tangential=_temp_cam(camera.get("tangential", None)),
                      fov=_temp_cam(camera.get("fov", None)),
                      projection=_temp_cam(camera.get("projection", None))
                      )


if __name__ == '__main__':
    info = {
        'position': {
            'x': 19.617147983589785,
            'y': -0.3571670183003431,
            'z': 0.2083393465328241},
        'scale': {
            'height': 4.793909959547556,
            'width': 2.0032044225562577,
            'depth': 1.5418855556278792},
        'rotation': {
            'x': 0.0,
            'y': 0.0,
            'z': -1.5731558280731583}
    }
    path = '/Users/stardust/Desktop/1681532060081818.pcd'
    points = o3d.io.read_point_cloud(path)
    center = [info['position']['x'], info['position']['y'], info['position']['z']]  # Center coordinates
    extent = [info['scale']['width'], info['scale']['height'], info['scale']['depth']]  # Extent along each axis
    theta = info['rotation']['z']
    rot_mat = np.array([[np.cos(theta), -np.sin(theta), 0],
                        [np.sin(theta), np.cos(theta), 0],
                        [0, 0, 1]])
    bbox = o3d.geometry.OrientedBoundingBox(center=center, R=rot_mat, extent=extent)
    _ = bbox.get_point_indices_within_bounding_box(points.points)
    _len = len(_)
    _ = np.array([np.asarray(points.points)[p] for p in _])
    matrix = np.c_[_, np.array([1] * _len)]
    cam = Camera(
        'PinHole',
        heading=(0.4351436321314605, -0.4677553765588058, 0.5492505771794342, -0.5386824023335351),
        position=(1.5601294, -0.37986112, 1.3333596),
        intrinsic=(1846.008599353862, 1857.930995475229, 1948.09353722228, 1078.768188621484),
        radial=(0, 0, 0, 0),
        tangential=(0, 0)
    )

    import cv2 as cv

    image_path = '/Users/stardust/Desktop/1681532060061245.jpg'
    img = cv.imread(image_path)
    point_size = 1
    point_color = (0, 0, 255)  # BGR
    thickness = 4  # Accepts 0, 4, or 8

    for points in np.dot(matrix, cam.cam2lidar_rt.I.T).tolist():
        point = np.array(cam.get_pixel_coordinate(points[:3]), int)
        cv.circle(img, point, point_size, point_color, thickness)

    cv.namedWindow("image")
    cv.imshow('image', img)
    cv.waitKey(10000)  # Display for 10 seconds
    cv.destroyAllWindows()

    from pathlib import Path

    for file in Path("your_directory").glob("*.json"):
        print(file.name)
