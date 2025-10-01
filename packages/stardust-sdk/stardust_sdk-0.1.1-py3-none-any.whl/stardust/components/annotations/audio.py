from .base_annotation import AnnotationObject


class Audio(AnnotationObject):
    def __init__(self, start, end, **kwargs):
        """
        This class defines the structure of video label task

        Args:
            start: float
                The start time of annotation for this audio
            end: float
                The end time of annotation for this audio

        Returns:
            Audio instance

        Examples:
            .. code-block:: python

                audio = Audio(start=0.57, 12.13)
        """
        assert isinstance(start, float)
        assert isinstance(end, float)
        self.start = start
        self.end = end
        AnnotationObject.__init__(self, **kwargs)
