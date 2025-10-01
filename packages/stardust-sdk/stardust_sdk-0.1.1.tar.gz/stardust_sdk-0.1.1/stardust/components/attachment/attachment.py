import os
from enum import Enum
from retry import retry
from typing import Optional
from dataclasses import dataclass

import requests


class AttachmentType(Enum):
    """
        Media type enumeration
    """
    Text = "TEXT"
    Image = "IMAGE"
    ImageSet = "IMAGE_SET"
    Video = "VIDEO"
    Audio = "AUDIO"
    AudioSet = "AUDIO_SET"
    PointCloud = "POINTCLOUD"
    PointCloudSet = "POINTCLOUD_SET"
    ImageSequence = "IMAGE_SEQUENCE"
    PointCloudSequence = "POINTCLOUD_SEQUENCE"
    PointCloudSetSequence = "POINTCLOUD_SET_SEQUENCE"


@dataclass
class UriInfo:
    uri: str

    @staticmethod
    def _mkdir(path) -> None:
        if not os.path.isfile(path):
            raise ValueError('download_path is error')
        dir_path = os.path.dirname(path)
        os.makedirs(dir_path, exist_ok=True)

    @retry(tries=3)
    def download_url(self, download_path: Optional[str] = None) -> str:
        if download_path:
            save_path = download_path
            self._mkdir(save_path)
        else:
            save_path = f'./{os.path.basename(self.uri)}'
        response = requests.get(self.uri, timeout=3)
        with open(save_path, 'wb') as wp:
            wp.write(response.content)
        return save_path
