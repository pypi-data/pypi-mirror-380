from typing import Dict
from .base_annotation import AnnotationObject


class Text(AnnotationObject):
    def __init__(self,
                 start=None,
                 end=None,
                 content=None,
                 **kwargs):
        """
        This class defines the structure of text label task

        Args:
           start:
               The start time of annotation for this text
           end:
               The end time of annotation for this text

        Returns:
           Text instance

        Examples:
            .. code-block:: python

                text = Text(start=0.57, end=12.13)
        """
        assert isinstance(start, int)
        assert isinstance(end, int)
        self.start = start
        self.end = end
        self.content = content
        AnnotationObject.__init__(self, **kwargs)

    @classmethod
    def gen_text(cls, slot, children_lst: Dict = None, parent_id: str = None, label_kind: str = None):
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

        text = Text(
            start=slot['start'],
            end=slot['length'] + slot['start'],
            content=slot['text'],
            parent=parent_id,
            id=slot['id'],
            children_lst=children_lst,
            label=label_kind
        )

        return text
