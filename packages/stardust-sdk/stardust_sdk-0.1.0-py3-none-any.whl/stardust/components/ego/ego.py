import math
import numpy as np
from typing import Optional, Union, Tuple
from scipy.spatial.transform import Rotation


class Ego:
    def __init__(self,
                 heading: Optional[tuple] = None,
                 position: Optional[tuple] = None,
                 longitude: Optional[Union[float, int]] = None,
                 latitude: Optional[Union[float, int]] = None,
                 altitude: Optional[Union[float, int]] = None
                 ):
        """
        Ego

        Args:
            heading:
                quaternion (x, y, z, w)
            position:
                offset (x, y, z)
            longitude:
                the longitude
            latitude:
                the latitude
            altitude:
                the altitude

        Returns:
            Ego instance

        """
        self.heading = heading
        self.position = position
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude

    def __repr__(self):
        return "the ego param"

    @property
    def ego_rt(self) -> np.matrix:
        """
        ego rt matrix
        """
        r = Rotation.from_quat(self.heading).as_matrix()
        rt = np.r_[np.c_[r, np.array(self.position)], np.array([[0, 0, 0, 1]])]
        return np.matrix(rt)

    @property
    def rotate(self) -> np.ndarray:
        """
        ego r matrix
        """
        r = Rotation.from_quat(self.heading).as_matrix()
        return r

    @property
    def to_world_coordinates(self) -> Tuple[float, float, float]:
        """
        Longitude and latitude to the coordinates of the world coordinate system
        """
        wgs84_a = 6378137.0  # major axis of the Earth's ellipsoid, in meters
        wgs84_f = 1 / 298.257223563  # flattening of the Earth's ellipsoid
        wgs84_e2 = wgs84_f * (2 - wgs84_f)  # eccentricity squared of the Earth's ellipsoid
        cos_lat = math.cos(self.latitude * math.pi / 180)
        sin_lat = math.sin(self.latitude * math.pi / 180)
        cos_lon = math.cos(self.longitude * math.pi / 180)
        sin_lon = math.sin(self.longitude * math.pi / 180)
        n = wgs84_a / math.sqrt(1 - wgs84_e2 * sin_lat * sin_lat)
        x = (n + self.altitude) * cos_lat * cos_lon
        y = (n + self.altitude) * cos_lat * sin_lon
        z = (n * (1 - wgs84_e2) + self.altitude) * sin_lat
        return x, y, z
