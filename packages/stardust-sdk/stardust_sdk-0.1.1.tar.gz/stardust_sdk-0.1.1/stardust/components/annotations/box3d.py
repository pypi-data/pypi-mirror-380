from typing import Union, Sequence, Dict
from scipy.spatial.transform import Rotation

import numpy as np
import open3d as o3d

from .base_annotation import AnnotationObject
from .point3d import Point3D
from stardust.utils.matrix4 import Matrix4


class Box3D(AnnotationObject):
    def __init__(self,
                 center: Union[Point3D, Sequence],
                 size: Union[Point3D, Sequence],
                 rotation: Sequence,
                 rotation_order="XYZ",
                 **kwargs
                 ) -> None:
        """
        This class defines the structure of 3d geometry box.

        Args:
            center:
                like: [4.133927784395542, -3.777526126541506, 0.7891658530222055] or Point3D obj
            size:
                like [7.298632312111001, 2.192134290714646, 1.9819562591803783], Iterable， extent in x, y and z direction or Point3D obj
            rotation:
                like [0, 0, -1.5713694508648803], Iterable
            rotation_order:
                default to be XYZ

        Returns:
            Box3D instance

        Examples:
            .. code-block:: python

                box = Box3D(Point3D(4.13, -3.77, 0.78),Point3D(1, 5, 1),[0, 0, -1.57])

                box.volume

                >>> output:
                >>> 5
        """
        # Currently only supports XYZ order
        assert len(rotation) == 3
        self._set_val("center", center)
        self._set_val("size", size)

        if volume := self._verify_is_box():
            self.volume = volume
        else:
            raise ValueError("Insufficient inputs to form a 3D box")
        self.rotation = rotation
        self.rotation_order = rotation_order

        AnnotationObject.__init__(self, **kwargs)

    def _set_val(self, key, value):
        if isinstance(value, Sequence):
            assert len(value) == 3
            self.__dict__[key] = list(value)
        elif isinstance(value, Point3D):
            self.__dict__[key] = [value.x, value.y, value.z]
        else:
            raise TypeError('Unsupported data type')

    def _verify_is_box(self) -> Union[bool, float]:
        """
        To verify if the input can form a 3D box

        Returns: bool/float
        """
        volume = self.size[0] * self.size[1] * self.size[2]
        # Ensure the oriented bounding box volume is positive
        if volume > 0:
            return volume
        else:
            return False

    @property
    def vertices(self) -> np.array:
        """
        The 8 vertices of the current 3D frame object

        Returns:
            np.array, the points from box3d

        Examples:
            .. code-block:: python

                box.vertices

                >>> output:

                >>> np.array([[ 1.63421476 -3.2760934   0.28916585]
                 [ 1.63364163 -4.27609323  0.28916585]
                 [ 6.63421394 -3.27895902  0.28916585]
                 [ 1.63421476 -3.2760934   1.28916585]
                 [ 6.63364081 -4.27895885  1.28916585]
                 [ 6.63421394 -3.27895902  1.28916585]
                 [ 1.63364163 -4.27609323  1.28916585]
                 [ 6.63364081 -4.27895885  0.28916585]])
        """
        obb = o3d.geometry.OrientedBoundingBox()
        center = self.center
        size = self.size
        rotation = self.rotation
        obb.center = np.array([center.x, center.y, center.z]) if isinstance(center, Point3D) else center
        obb.extent = np.array([size.x, size.y, size.z]) if isinstance(size, Point3D) else size
        obb.R = Rotation.from_euler(self.rotation_order, rotation).as_matrix()
        return np.array(obb.get_box_points())

    @staticmethod
    def gen_box3d(slot, children_lst: Dict = None, parent_id: str = None, label_kind: str = None, team_id: int = None):
        """
        generate the Box3D obj

        Args:
            slot:
                rosetta slot
            children_lst:
                rosetta children
            parent_id:
                Upper floor ID

        Returns:
                a Box3D instance
        """
        if not slot.get("box", None):
            return
        box = Matrix4(slot['box']).box_info
        children_lst = children_lst if children_lst else {}
        parent_id = parent_id if parent_id else ""
        label_kind = label_kind if label_kind else ""
        box3d = Box3D(
            id=slot['id'],
            center=[(p := box['position'])['x'], p['y'], p['z']],
            size=[(s := box['scale'])['height'], s['width'], s['depth'] if s.get('depth') else s.get('length')],
            rotation=[(r := box['position'])['x'], r['y'], r['z']],
            rotation_order="XYZ",
            parent=parent_id,
            label=label_kind,
            children=children_lst,
            team_id=team_id
        )

        return box3d
