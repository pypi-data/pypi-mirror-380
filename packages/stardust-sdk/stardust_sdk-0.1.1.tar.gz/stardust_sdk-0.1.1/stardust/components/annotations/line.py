from enum import Enum
from typing import List, Union, Sequence

import numpy as np

from .point import Point
from .base_annotation import AnnotationObject


class InterpolationEnum(Enum):
    Straight = "line"
    BSpline = "b-spline"
    Spline = "spline"


class Line(AnnotationObject):
    def __init__(self,
                 points: Union[List[Point], np.array, Sequence],
                 interpolation=InterpolationEnum.Straight.value,
                 **kwargs) -> None:
        """
        This class defines the structure of 2d line.

        Args:
            points:
                A list composed of Point objects or a Sequence composed of numbers
            interpolation:
                Filled line between points, default straight line

        Returns:
            Line instance

        Examples:
            .. code-block:: python

                line = Line([(0,0), (1,1), (2,2), (3,3)])
        """
        assert len(points) >= 2
        if isinstance(points[0], Point):
            self.points = [[point.x, point.y] for point in points]
        else:
            assert np.asarray(points).shape[1] == 2
            self.points = points
        if interpolation not in [member.value for member in InterpolationEnum]:
            raise ValueError("your input interpolation is illegal！")
        self.interpolation = interpolation
        AnnotationObject.__init__(self, **kwargs)

    @staticmethod
    def gen_line(slot, children_lst=None, parent_id=None, label_kind=None, **kwargs):
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
                a Line instance
        """
        children_lst = children_lst if children_lst else {}
        parent_id = parent_id if parent_id else ""
        label_kind = label_kind if label_kind else ""
        points = np.array([[point['x'], point['y']] for point in slot['vertices']])
        line = Line(
            id=slot['id'],
            points=points,
            parent=parent_id,
            label=label_kind,
            children=children_lst,
            team_id=kwargs.get("team_id", None)
        )
        return line
