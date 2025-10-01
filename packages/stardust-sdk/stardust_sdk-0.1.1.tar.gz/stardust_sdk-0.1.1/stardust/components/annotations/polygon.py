from typing import List, Union, Sequence
import numpy as np
from shapely.geometry import Polygon as SPolygon
from .point import Point
from .base_annotation import AnnotationType, AnnotationObject
from .line import Line
from .box import Box2D


class Polygon(Line, AnnotationObject, SPolygon):
    def __init__(self,
                 points: Union[List[Point], np.ndarray, Sequence],
                 **kwargs) -> None:
        """
        This class defines the concept of 2d geometry Polygon

        Args:
            points:
                A list composed of Point objects or a Sequence composed of numbers

        Returns:
            Polygon instance

        Examples:
            .. code-block:: python

                polygon = Polygon([(0,0), (1,1), (2,2), (3,3)])
        """
        if not len(points) > 2:
            raise ValueError("Invalid number length of points")
        if isinstance(points[0], Point):
            self.shapely_polygon = SPolygon([[point.x, point.y] for point in points])
        else:
            assert np.array(points).shape[1] == 2
            self.shapely_polygon = SPolygon([[point[0], point[1]] for point in points])

        Line.__init__(self, points=points)
        AnnotationObject.__init__(self, **kwargs)

    @property
    def area(self) -> float:
        """
        Returns: float
            the area of current polygon instance
        """
        return self.shapely_polygon.area

    @property
    def points_num(self) -> float:
        """
        Returns: float
             the points num of current polygon instance
        """
        return len(self.points)

    @property
    def bounding_box(self):
        """
        Returns: float
            box2d obj, the box3d outer the current polygon
        """
        bounds = self.shapely_polygon.bounds
        return Box2D(np.array([bounds[0], bounds[1]]), np.array([bounds[2], bounds[3]]))

    @staticmethod
    def gen_polygon(slot, children_lst, parent_id, label_kind):
        """
        generate the Polygon obj

        Args:
            slot:
                rosetta slot
            children_lst:
                rosetta children
            parent_id:
                Upper floor ID

        Returns:
            a Polygon instance
        """
        children_lst = children_lst if children_lst else {}
        parent_id = parent_id if parent_id else ""
        label_kind = label_kind if label_kind else ""
        polygon = Polygon(
            points=np.asarray([[round(vertice['x'], 2), round(vertice['y'], 2)] for vertice in slot['vertices']]),
            parent=parent_id,
            id=slot['id'],
            label=label_kind,
            children=children_lst
        )
        return polygon
