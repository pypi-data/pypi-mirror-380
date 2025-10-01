from enum import Enum
from typing import TypeVar
import numpy as np

_T = TypeVar('_T')


class AnnotationObject:
    def __init__(self, **kwargs) -> None:
        _allow = ["id", "label", "children", "score", "parent", "label_kind", "team_id"]
        for key, val in kwargs.items():
            if val and key in _allow:
                setattr(self, key, val)


class NumberFiled:
    def __init__(self, name) -> None:
        self.name = name

    def __set__(self, instance, value) -> None:
        if not isinstance(value, (float, int, np.int64)):
            raise TypeError("point's coordinate must be a number!")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner) -> _T:
        return instance.__dict__[self.name]

    def __delete__(self, instance) -> None:
        del instance.__dict__[self.name]


class AnnotationType(Enum):
    Point = 'point'
    Point3D = 'point3d'
    Polygon = 'polygon'
    Quadrilateral = 'quadrilateral'
    Box2D = 'rectangle'
    Box3D = 'box3d'
    Line = 'line'
    Line3D = 'line'
    SemanticSegmentation3D = "semantic_segmentation_3d"
    Video = "video"
    Audio = "audio"
    Input = "input"


if __name__ == '__main__':
    pass
