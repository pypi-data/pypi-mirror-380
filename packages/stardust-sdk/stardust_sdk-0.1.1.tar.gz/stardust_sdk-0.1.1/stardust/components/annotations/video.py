from .base_annotation import AnnotationType, AnnotationObject


class Video(AnnotationObject):
    def __init__(self,
                 start,
                 end,
                 fps=30,
                 **kwargs):
        """
        This class defines the structure of video label task

        Args:
           start:
               The start time of annotation for this text
           end:
               The end time of annotation for this text

        Returns:
           Video class

        Examples:
            .. code-block:: python

                video = Video(start=0.57, end=12.13)
        """
        assert isinstance(start, float)
        assert isinstance(end, float)
        assert isinstance(fps, int)
        self.start = start
        self.end = end
        self.fps = fps
        AnnotationObject.__init__(self, **kwargs)
