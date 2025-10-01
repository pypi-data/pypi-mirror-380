import os
from dataclasses import dataclass
from typing import List, Optional

import numpy as np
import open3d as o3d

from stardust.components.attachment.attachment import AttachmentType, UriInfo

ALL_POINTCLOUD = (".pcd", ".ply")


class PointCloud(UriInfo):
    def __init__(
            self,
            uri: Optional[str] = None,
            name: Optional[str] = None,
            file_path: Optional[str] = None
    ):
        """
        Point cloud structure, marked as point cloud type

        Args:
            uri:
                Cloud address of the point cloud
            name：
                Point cloud name
            file_path:
                Local path of the point cloud file

        Returns:
            PointCloud instance
        
        Examples:
            .. code-block:: python
        
                path = '/Users/stardust/Desktop/1681532060081818.pcd'
                p = PointCloud(filename=path)
                print(p.points_info)
        """

        super(PointCloud, self).__init__(uri)
        self.type = AttachmentType.PointCloud.value
        self.name = name
        # assert os.path.isfile(file_path)
        _, ext = os.path.splitext(file_path)
        assert ext
        self.file_path = file_path
        _ = os.path.splitext(os.path.basename(self.file_path))[0]
        # assert _.isdigit(), 'Name the point cloud file according to the time stamp'
        self.timestamp = _

    @property
    def pcd(self):
        return o3d.t.io.read_point_cloud(self.file_path)

    def points_info(self, add1=False) -> np.ndarray:
        _ = self.pcd.point.positions.numpy()
        if add1:
            _ = np.c_[_, np.array([1] * len(_))]
        return _

    def get_attribute_items(self, attribute: str) -> Optional[np.ndarray]:
        try:
            return eval(f'self.pcd.point.{attribute}.numpy()')
        except KeyError as e:
            print(f'No {attribute} attribute, point cloud information:')
            print(self.pcd)
            return None


@dataclass
class PointCloudSet:
    """
    Args:
        point_cloud_set:
            PointCloud list

    Returns:
        PointCloudSet class
    """
    type = AttachmentType.PointCloudSet.value
    point_cloud_set: List[PointCloud]


if __name__ == '__main__':
    path = '/Users/stardust/Desktop/files/000206.pcd'
    p = PointCloud(file_path=path)
    print(p.points_info(True))
    print(p.__dir__())
