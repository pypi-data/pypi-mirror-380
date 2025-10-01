from typing import List, Union
from numpy import array
from .point3d import Point3D
from .base_annotation import AnnotationObject


class Segementation(AnnotationObject):
    """
    3d semantic segmentation
    """

    def __init__(self, points: Union[List[Point3D], array], **kwargs):
        self.points = points
        super().__init__(**kwargs)
