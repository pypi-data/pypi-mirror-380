"""
    Get rosetta's data
"""

import os
import time
import requests
from typing import List, Optional

from stardust.rosetta.rosetta_pool import RosettaPool
from stardust.rosetta.frames2frame import frames_split
from stardust.rosetta.new_farmes2frame import to_split
from stardust.file.file import File


class RosettaData:
    def __init__(
            self,
            project_id: int,
            save_path: str,
            rosetta_type: str = 'top',
    ):
        self.project_id = project_id
        assert rosetta_type in ['top', 'dev'], 'top or dev'
        self.rosetta_type = rosetta_type
        self.save_path = save_path
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        self.pool = RosettaPool(self.rosetta_type)

    def _get_rosetta_json(self, project_id: int, pool_id: list):
        """
        Send a request to export data

        Args:
            project_id:
                project_id
            pool_id:
                pool_id
        Returns:
            response.content
        """
        url = f'{self.pool.env}/rosetta-service/project/doneTask/export'

        req_info = {
            "projectId": project_id,
            "poolId": pool_id,
            "type": 1
        }

        resp = requests.post(url, headers=self.pool.headers, json=req_info)
        if (ct := resp.headers.get('Content-Type')) == "application/octet-stream;charset=utf-8":
            return resp.content
        elif ct == "application/json":
            raise ValueError(resp.json()['message'])
        else:
            raise Exception("Failed to download dataset")

    def _zipfile_factory(self, zipfile: bytes, project_id: int, version: str):
        """
        decompression

        Args:
            zipfile:
                response.content
            project_id:
                project_id
            version:
                version
        Returns:

        """
        save_path = os.path.join(self.save_path, f'{project_id}', "json")
        File.to_unzip(zipfile, save_path)
        if version == 'old':
            frames_split(save_path)
        elif version == 'new':
            to_split(save_path)
        else:
            raise ValueError('version is new or old')

    def export(self, pool_list: Optional[List[int]] = None, split_name: str = 'new'):
        """
        Derived data

        Args:
            pool_list:
                Pool list, optional. If this parameter is not specified, all pools are completed
            split_name:
                new or old

        Returns:

        """
        if not pool_list:
            pool_list = self.pool.get_all_finish_pool_info(self.project_id)
            assert pool_list, f'Project {self.project_id} has no completed pools'
        resp_export = self._get_rosetta_json(self.project_id, pool_list)
        self._zipfile_factory(resp_export, self.project_id, split_name)


if __name__ == '__main__':
    data = RosettaData(1692, '/Users/mac/Desktop')
    data.export([42789,], 'new')
