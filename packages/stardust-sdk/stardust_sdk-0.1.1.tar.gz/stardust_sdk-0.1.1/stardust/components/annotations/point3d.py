import numpy as np

from .base_annotation import NumberFiled


class Point3D:
    x: NumberFiled('x')
    y: NumberFiled('y')
    z: NumberFiled('z')

    def __init__(self, x, y, z):
        """
        This class defines the concept of 3d geometry point

        Args:
            x: a float number
            y: a float number
            z: a float number

        Returns:
            Point3D instance

        Examples:
            .. code-block:: python

                p = Point(11.12, 345.43, 46,78)
        """
        self.x = x
        self.y = y
        self.z = z

    def to_array(self) -> np.array:
        return np.array([self.x, self.y, self.z])
