from typing import Union, Optional, Dict, Sequence, List
from stardust.components.annotations.point import Point
from stardust.components.annotations.base_annotation import AnnotationObject


class Box2D(AnnotationObject):
    def __init__(self,
                 p1: Union[Sequence, Point] = None,
                 p2: Union[Sequence, Point] = None,
                 center: Union[Sequence, Point] = None,
                 size: Optional[List[float]] = None,
                 source: Optional[str] = None,
                 **kwargs) -> None:
        """
        This class defines the structure of box2d label task

        Args:
            p1:
                Point obj or a Sequence obj, the point at the top left corner of a 2d box
            p2:
                Point obj or a Sequence obj, the point at the bottom right corner of a 2d box
            center:
                Center point coordinates, supporting Point objects or sequences of length 2
            size:
                Size, supports Point objects or sequences of length 2
            source:
                camera name, string, camera name

        Returns:
            Box2D instance

        Examples:
            .. code-block:: python

                bx = Box2D(center=[473.07, 395.93], size=[38.65, 28.67])
                bx.area

                >>> output
                1108.0955000000001
        """

        if p1 is not None and p2 is not None:
            self._set_val("p1", p1)
            self._set_val("p2", p2)
            self.center = [self.width / 2 + self.p1[0], self.height / 2 + self.p1[1]]
            self.size = [self.p2[0] - self.p1[0], self.p2[1] - self.p1[1]]
            # assert self.size[0] > 0 and self.size[1] > 0
        elif center is not None and size is not None:
            self._set_val("center", center)
            self._set_val("size", size)
            self.p1 = [self.center[0] - self.size[0] / 2, self.center[1] - self.size[1] / 2]
            self.p2 = [self.center[0] + self.size[0] / 2, self.center[1] + self.size[1] / 2]
        else:
            raise TypeError("missing required parameters")

        self.source = source
        AnnotationObject.__init__(self, **kwargs)

    def _set_val(self, key, value):
        if isinstance(value, Sequence):
            assert len(value) == 2
            self.__dict__[key] = list(value)
        elif isinstance(value, Point):
            self.__dict__[key] = [value.x, value.y]
        else:
            raise TypeError('Unsupported data type')

    @property
    def corners(self) -> Dict[str, Point]:
        """
        Returns:
            float: the conner points os the current box2d
        """
        return {
            'x1': self.p1[0],
            'y1': self.p1[1],
            'x2': self.p2[0],
            'y2': self.p2[1]
        }

    @property
    def x1(self) -> float:
        """
        Returns:
            float: The x-coordinate of the top left point.
        """
        return self.p1[0]

    @property
    def y1(self) -> float:
        """
        Returns:
            float: The y-coordinate of the top left point.
        """
        return self.p1[1]

    @property
    def x2(self) -> float:
        """
        Returns:
            float: The x-coordinate of the bottom right point.
        """
        return self.p2[0]

    @property
    def y2(self) -> float:
        """
        Returns:
            float: The y-coordinate of the bottom right point.
        """
        return self.p2[0]

    @property
    def height(self) -> float:
        """
        Returns:
            float: the height of the current box2d, axis y
        """
        return round(self.p2[1] - self.p1[1], 2)

    @property
    def width(self) -> float:
        """
        Returns:
            float: the width of the current box2d, axis x
        """
        return round(self.p2[0] - self.p1[0], 2)

    @property
    def area(self) -> float:
        """
        Returns:
            float: the area of the current box2d
        """
        return self.width * self.height

    @staticmethod
    def gen_box(slot, children_lst=None, parent_id=None, label_kind=None, **kwargs):
        """
        generate the Box2D obj

        Args:
            slot:
                rosetta slot
            children_lst:
                rosetta children
            parent_id:
                Upper floor id
        Returns:
            a Box2D instance
        """
        children_lst = children_lst if children_lst else {}
        parent_id = parent_id if parent_id else ""
        label_kind = label_kind if label_kind else ""
        box2d = Box2D([round((p := slot['plane']["topLeft"])['x'], 2), round(p['y'], 2)],
                      [round((p := slot['plane']["bottomRight"])['x'], 2), round(p['y'], 2)],
                      label=label_kind,
                      id=slot['id'],
                      source=slot.get('source'),
                      children=children_lst,
                      parent=parent_id,
                      team_id=kwargs.get('team_id', None)
                      )
        return box2d
