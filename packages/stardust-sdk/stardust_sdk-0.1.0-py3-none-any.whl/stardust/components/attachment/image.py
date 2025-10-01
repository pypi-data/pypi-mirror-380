from typing import Optional, List
import numpy as np
import cv2 as cv
from dataclasses import dataclass
from stardust.components.annotations import Box3D, Point3D
from stardust.components.camera.camera import Camera
from stardust.components.attachment.attachment import AttachmentType, UriInfo

ALL_IMAGE = (".jpg", ".jpeg", ".png", ".webp")


class Image(UriInfo):
    def __init__(
            self,
            uri: str,
            width: Optional[int] = None,
            height: Optional[int] = None,
            name: Optional[str] = None,
            camera_param: Optional[Camera] = None
    ):
        """
        Picture object
        
        Args:
            width: 
                the picture width
            height: 
                the picture height
            name: 
                the picture name
            camera_param:
                class Camera
                    
        Returns:
            Image instance
        
        Examples:
            .. code-block:: python
        
                image = Image('', camera_param=cam)
        """
        super(Image, self).__init__(uri)
        self.type = AttachmentType.Image.value
        self.width = width
        self.height = height
        self.name = name
        self.camera_param = camera_param

    @staticmethod
    def _visual(**kwargs):
        img = cv.imread(kwargs['file_path'])
        cv.rectangle(img, kwargs['min_point'], kwargs['max_point'], (0, 255, 0), thickness=3, lineType=cv.LINE_AA)
        cv.imshow('Image', img)
        cv.waitKey(0)

    @staticmethod
    def _visual2(*args):
        box1, box2, file_path = args
        img = cv.imread(file_path)
        for i in range(4):
            cv.line(img, tuple(box1[i]), tuple(box1[(i + 1) % 4]), (0, 255, 0), 3)
            cv.line(img, tuple(box2[i]), tuple(box2[(i + 1) % 4]), (0, 255, 0), 3)
            Image.draw_dashed_line(img, tuple(box1[i]), tuple(box2[i]), (0, 255, 0), 3, line_type=cv.LINE_AA, shift=0)
        cv.imshow('Image', img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def draw_dashed_line(image, start_point, end_point, color, thickness, line_type, shift):
        line_length = int(np.sqrt((end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) ** 2))
        x_step = (end_point[0] - start_point[0]) / line_length
        y_step = (end_point[1] - start_point[1]) / line_length

        for i in range(0, line_length, 10):  # Step size of 10; adjust as needed
            x1 = int(start_point[0] + i * x_step)
            y1 = int(start_point[1] + i * y_step)
            x2 = int(start_point[0] + (i + 5) * x_step)
            y2 = int(start_point[1] + (i + 5) * y_step)
            cv.line(image, (x1, y1), (x2, y2), color, thickness, lineType=line_type, shift=shift)

    @staticmethod
    def get_points(max_point, min_point):
        x1, y1 = np.array(min_point, int)
        x2, y2 = np.array(max_point, int)
        rectangle_coordinates = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
        return rectangle_coordinates

    def visual_2d_box(self, box3d: Box3D, file_path: Optional[str]):
        vertices = box3d.vertices
        vertices_matrix = np.c_[np.array([vertices[n] for n in [0, 3, 6, 1]]), np.array([1, 1, 1, 1])]
        pixel_points = np.array([self.camera_param.get_pixel_coordinate(_[:3]) for _ in
                                 np.dot(vertices_matrix, self.camera_param.cam2lidar_rt.I.T).tolist()], dtype=np.int32)
        max_point = max(pixel_points, key=lambda x: sum(x))
        min_point = min(pixel_points, key=lambda x: sum(x))
        file_path = file_path if file_path else self.download_url()
        self._visual(file_path=file_path, max_point=max_point, min_point=min_point)

    def visual_3d_box(self, box3d: Box3D, file_path: Optional[str]):
        vertices = box3d.vertices
        vertices_matrix = np.c_[np.array(vertices), np.array([1] * 8)]
        pixel_points = np.array([self.camera_param.get_pixel_coordinate(_[:3]) for _ in
                                 np.dot(vertices_matrix, self.camera_param.cam2lidar_rt.I.T).tolist()])
        box1 = np.array([pixel_points[_] for _ in [0, 1, 3, 6]])
        sum_of_coordinates1 = np.sum(box1, axis=1)
        max_coordinate1 = box1[np.argmax(sum_of_coordinates1)]
        min_coordinate1 = box1[np.argmin(sum_of_coordinates1)]
        box1 = self.get_points(max_coordinate1, min_coordinate1)

        box2 = np.array([pixel_points[_] for _ in [2, 4, 5, 7]])
        sum_of_coordinates2 = np.sum(box2, axis=1)
        max_coordinate2 = box2[np.argmax(sum_of_coordinates2)]
        min_coordinate2 = box2[np.argmin(sum_of_coordinates2)]
        box2 = self.get_points(max_coordinate2, min_coordinate2)

        self._visual2(box1, box2, file_path)

    @staticmethod
    def gen_image(image_obj):
        """
        generate the Image obj

        Args:
            image_obj:
                rosetta image data
        Returns:
            a Image instance

        """
        _ = Image(uri=image_obj['url'],
                  width=image_obj.get('width'),
                  height=image_obj.get('height'),
                  name=image_obj['name'])
        if "camera" in image_obj:
            _.camera_param = Camera.gen_camera(image_obj['camera'])
        return _


@dataclass
class ImageSet:
    """
    Args:
        image_set: Image list
    """
    type = AttachmentType.ImageSet.value
    image_set: List[Image]


if __name__ == '__main__':
    box3d = Box3D(
        center=Point3D(19.617147983589785, -0.3571670183003431, 0.2083393465328241),
        size=Point3D(2.0032044225562577, 4.793909959547556, 1.5418855556278792),
        rotation=[0, 0, -1.5731558280731583]
    )
    cam = Camera(
        'PinHole',
        heading=(0.4351436321314605, -0.4677553765588058, 0.5492505771794342, -0.5386824023335351),
        position=(1.5601294, -0.37986112, 1.3333596),
        intrinsic=(1846.008599353862, 1857.930995475229, 1948.09353722228, 1078.768188621484),
        radial=(0, 0, 0, 0),
        tangential=(0, 0)
    )
    image = Image('', camera_param=cam)
    # https://rosettalab.top/task/970/224049822964001714/viewOnly
    # image.visual_2d_box(box3d, '/Users/stardust/Desktop/1681532060061245.jpg')
    image.visual_3d_box(box3d, '/Users/mac/Downloads/jc93_suz_Ew_0b_sunny_m_0_1701929360184.jpg')
