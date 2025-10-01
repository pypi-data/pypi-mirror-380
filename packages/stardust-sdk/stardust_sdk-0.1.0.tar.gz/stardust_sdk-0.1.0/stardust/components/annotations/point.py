import numpy as np

from stardust.components.annotations.base_annotation import AnnotationType, AnnotationObject, NumberFiled


class Point(AnnotationObject):

    def __init__(self,
                 x,
                 y,
                 **kwargs) -> None:
        """
        This class defines the concept of 2d geometry point

        Args:
            x: a float number
            y: a float number

        Returns:
            Point instance

        Examples:
            .. code-block:: python

                p = Point(11.12, 345.43)
        """
        self.x = x
        self.y = y
        AnnotationObject.__init__(self, **kwargs)

    def to_array(self) -> np.array:
        return np.array([self.x, self.y])

    @classmethod
    def gen_point(cls, slot, children_lst, parent_id, label_kind=None):
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
        point = Point(
            slot['point']['x'],
            slot['point']['y'],
            parent=parent_id,
            id=slot['id'],
            label=label_kind,
            children=children_lst
        )
        return point
