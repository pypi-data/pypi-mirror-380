from typing import Union, Optional, List

from stardust.components.attachment import *


class Media:
    def __init__(
            self,
            point_cloud: Optional[Union[PointCloud, PointCloudSet]] = None,
            image: Optional[Union[Image, ImageSet]] = None
    ):
        """
        Annotate container objects such as files, point clouds, pictures, audio and video

        Args:
            point_cloud:
                Point cloud, point cloud set

                eg:
                    point_cloud = PointCloud("1681532060081818.pcd")
            image:
                image、image—set，eg: image = Image("1689737321.jpg")

        Returns：
            Media instance

        Examples:
            .. code-block:: python

                media = Media(point_cloud=PointCloud(*), image=Image(*))

        """
        self.point_cloud = point_cloud
        self.image = image


class TaskInfo:
    def __init__(self,
                 task_id: int = None,
                 frame_num: int = None,
                 project_id: int = None,
                 pool_id: int = None,
                 ):
        """
        rosetta Information about the project

        Args:
            task_id:
                int, rosetta_task_id
            frame_num:
                int, frame, Start at 0
            project_id:
                int, rosetta_project_id
            pool_id:
                int, rosetta_pool_id
        Returns:
            TaskInfo instance

        Examples:
            .. code-block:: python

                task_info = TaskInfo(288919499858784002, 0, 1703, 456212)

        """
        self.task_id = task_id
        self.frame_num = frame_num
        self.project_id = project_id
        self.pool_id = pool_id


class Annotation:
    def __init__(self,
                 box3d_lst=None,
                 box2d_lst=None,
                 input_lst=None,
                 line_lst=None,
                 polygon_lst=None,
                 key_point_lst=None,
                 text_lst=None
                 ):
        """
        Annotate the result, supporting 3D box, 2D box, input box, line, polygon

        Args:
            box3d_lst:
                All box3d annotation results, in general, take the box3d object id as the key and box3d object as the value
            box2d_lst:
                All box2d annotation results, in general, take the box2d object id as the key and box2d object as the value
            input_lst:
                In general, the input object id is used as the key and the input object as the value
            line_lst:
                In general, the result of all line annotations takes the id of the line object as the key and the line object as the value
            polygon_lst:
                All polygon annotations, in general, take the id of the polygon object as the key and the polygon object as the value
        Returns:
            Annotation instance

        Examples:
            .. code-block:: python

                ann = Annotation(
                    box3d_lst,
                    box2d_lst,
                    input_lst,
                    line_lst,
                    polygon_lst,
                )

        """
        if not box3d_lst:
            box3d_lst = {}
        if not box2d_lst:
            box2d_lst = {}
        if not input_lst:
            input_lst = {}
        if not line_lst:
            line_lst = {}
        if not polygon_lst:
            polygon_lst = {}
        if not key_point_lst:
            key_point_lst = {}
        if not text_lst:
            text_lst = {}

        self.box3d_lst = box3d_lst
        self.box2d_lst = box2d_lst
        self.input_lst = input_lst
        self.line_lst = line_lst
        self.polygon_lst = polygon_lst
        self.key_point_lst = key_point_lst
        self.text_lst = text_lst


Prediction = Annotation


class Frame:
    def __init__(self,
                 media: Media = None,
                 task_info: TaskInfo = None,
                 annotation: Annotation = None,
                 prediction: Prediction = None,
                 ):
        """
        Single frame structure

        Args:
            media:
                Media obj
            task_info:
                TaskInfo obj
            annotation:
                Annotation obj

        Returns:
            Frame instance

        Examples:
            .. code-block:: python

                frame = Frame(media,
                    task_info,
                    annotation,
                    prediction
                )
        """
        self.media = media
        self.task_info = task_info
        self.annotation = annotation
        self.prediction = prediction

    @property
    def urls(self) -> List[str]:
        """
        Gets the address of the annotated file

        Returns:
            list
        """
        lst = list()
        if self.media.point_cloud.uri:
            lst = [self.media.point_cloud.uri, ]
        if isinstance(self.media.image, list):
            lst.extend([image.uri for image in self.media.image])
        return lst


if __name__ == '__main__':
    pass
