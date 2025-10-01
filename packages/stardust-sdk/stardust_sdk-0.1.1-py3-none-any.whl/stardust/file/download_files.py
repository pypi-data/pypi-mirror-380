import os
import re
import json
import asyncio
from pathlib import Path
from loguru import logger
from urllib.parse import quote, unquote
from typing import List, Sequence, Dict, Tuple

import aiohttp
import uvloop
from tqdm import tqdm
from stardust.components.attachment.image import ALL_IMAGE
from stardust.components.attachment.pointcloud import ALL_POINTCLOUD
from stardust.rosetta.rosetta_data import RosettaData
from stardust.components.frame import Frame

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
logger.add("app.log", rotation="500 MB")


class Downloader:
    def __init__(self, urls: List[Tuple[str]], save_path: str = None):
        """
        downloader

        Args:
            urls:
                Required download link
            save_path:
                Save directory
        """
        self.urls = urls
        self.save_path = save_path
        self.slice_num = 1000
        self.attempts = 3
        self.bar = tqdm(total=len(self.urls))
        self.err_list = list()

    @staticmethod
    def is_empty(filename):
        return os.path.getsize(filename) != 0

    @staticmethod
    async def write_local(result, local_path):
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        with open(local_path, 'wb') as wp:
            wp.write(result)
            return True

    async def fetch(self, session, url, local_path):
        for n in range(self.attempts):
            try:
                async with session.get(url) as response:
                    if response.status != 200:
                        print(f"Failed to download {url}  status_code:{response.status}")
                        continue
                    content = await response.content.read()
                    result = await self.write_local(content, local_path)
                    if result:
                        self.bar.update(1)
                        if n != 0:
                            print(f'{n} Retry successfully {url}')
                        return True
            except Exception as e:
                print(f'Failed to download {url}: {e}')
            await asyncio.sleep(0.3)
        self.err_list.append(f"Failed to download {url}")
        return False

    async def async_download(self):
        async with aiohttp.ClientSession() as session:
            for i in range(0, len(self.urls), self.slice_num):
                tasks = []
                for url, file_save_path in self.urls[i: i + self.slice_num]:
                    url = quote(url, safe=':/')
                    if os.path.exists(file_save_path) and self.is_empty(file_save_path):
                        self.bar.update(1)
                        continue
                    tasks.append(asyncio.create_task(self.fetch(session, url, file_save_path)))
                if tasks:
                    await asyncio.wait(tasks)
            if self.err_list:
                error_txt = os.path.join(os.getcwd(), 'download_error.txt')
                with open(error_txt, 'w') as wp:
                    for _ in self.err_list:
                        wp.write(_)
                        wp.write("\n")
                    print(f'{len(self.err_list)} urls failed to download')
            self.bar.close()


def attachment_name_factory(att, save_path, project_id, task_id, frame_num, image_url_lst, pointcloud_url_lst,
                            name=None):
    if att.startswith("oss://stardust-data/"):
        att = att.replace("oss://stardust-data/", "https://stardust-data.oss-cn-hangzhou.aliyuncs.com/")
    if (suffix := Path(att).suffix) in ALL_IMAGE:
        if name:
            image_url_lst.append(
                (att, os.path.join(save_path, str(project_id), "images", name, f"{task_id}_{frame_num}{suffix}")))
        else:
            image_url_lst.append(
                (att, os.path.join(save_path, str(project_id), "images", f"{task_id}_{frame_num}{suffix}")))
    elif suffix in ALL_POINTCLOUD:
        pointcloud_url_lst.append(
            (att, os.path.join(save_path, str(project_id), "pcds", f"{task_id}_{frame_num}{suffix}")))
    else:
        raise TypeError("Dataset type not supported yet")


def load_dataset(frame: Frame = None,
                 project_id: int = None,
                 save_path=None,
                 **kwargs) -> None:
    """
    The function of loading data sets, you can enter the Frame object, you can also enter the project pool, if there is already a local rosetta_json will not be downloaded again
    save_path is used as the path to save annotation files. If the path has a frame, the data in the frame is obtained. Otherwise, the project_id,, and other values are required.

    Args:
        frame:
            Frame object
        save_path:
            Save directory
        peoject_id:
            rosetta project ID
        pool_lst:
            pool list

    Returns:

    Outputs:
        path
            -{project_id}
                --jsons
                    {task_id}_{frame_id}.json
                --images
                    --{camera_id}
                        {task_id}_{frame_id).jpg
                --pcds
                    {task_id}_{frame_id}.pcd
                --poses
                    {task_id}_{frame_id).txt
                --calibrations
                    {camera_id}.json

    """
    assert save_path
    if save_path and not os.path.exists(save_path):
        os.makedirs(save_path)

    # Links that need to be downloaded
    image_url_lst = list()
    pointcloud_url_lst = list()
    # Handle in-memory Frame objects
    if frame:
        project_id = frame.task_info.project_id  # Rosetta project ID
        task_id = frame.task_info.task_id  # Task ID
        frame_num = frame.task_info.frame_num  # Frame index
        media = frame.media  # Annotation files
        # Check for point clouds first
        if hasattr(media, "point_cloud") and media.point_cloud and media.point_cloud.uri:
            attachment_name_factory(media.point_cloud.uri, save_path, project_id, task_id, frame_num, image_url_lst,
                                    pointcloud_url_lst)
        # Download related images if present
        if hasattr(media, "image") and media.image:
            if isinstance(media.image, Sequence):
                for img in media.image:
                    attachment_name_factory(img.uri, save_path, project_id, task_id, frame_num, image_url_lst,
                                            pointcloud_url_lst, name=img.camera_param.name)
            else:
                attachment_name_factory(media.image.uri, save_path, project_id, task_id, frame_num, image_url_lst,
                                        pointcloud_url_lst)
    # Or fetch directly from a project ID
    elif project_id is not None:
        assert isinstance(project_id, int)
        pool_lst = kwargs.get("pool_lst", [])  # Pool IDs for the Rosetta project
        RosettaData(project_id, save_path).export(pool_lst)

        # Prepare directory for processed JSON files
        jsons_save_path = os.path.join(save_path, str(project_id), "jsons")
        os.makedirs(jsons_save_path, exist_ok=True)
        # Iterate Rosetta JSON to extract download links
        for file in Path(save_path).joinpath(str(project_id), "json").glob(f"*.json"):
            with open(file, 'r', encoding='utf-8') as f:
                attachment = (data := json.load(f))['taskParams']['record']['attachment']
                task_id = data['taskId']
                # Frame number
                frame_num = str(file).rsplit(".", 1)[0][-4:]
                if not frame_num.isdigit():
                    frame_num = '0001'
                # Extract URLs and destinations
                if isinstance(attachment, Dict):
                    # re_find_lst = re.findall("'url': '(?P<urls>.*?)',", str(attachment))
                    main_url = attachment['url']
                    attachment_name_factory(main_url, save_path, project_id, task_id, frame_num, image_url_lst,
                                            pointcloud_url_lst)
                    for att in attachment.get("imageSources", []):
                        img_url = att['url']
                        name = att['name']
                        attachment_name_factory(img_url,
                                                save_path,
                                                project_id,
                                                task_id,
                                                frame_num,
                                                image_url_lst,
                                                pointcloud_url_lst, name)
                elif isinstance(attachment, str):
                    attachment_name_factory(attachment,
                                            save_path,
                                            project_id,
                                            task_id,
                                            frame_num,
                                            image_url_lst,
                                            pointcloud_url_lst)
            with open(f'{jsons_save_path}/{task_id}_{frame_num}.json', 'w', encoding='utf-8') as new_json:
                json.dump(data, new_json, ensure_ascii=False)
    else:
        raise TypeError("Missing required parameters")

    asyncio.run(Downloader(pointcloud_url_lst).async_download())
    asyncio.run(Downloader(image_url_lst).async_download())
    return save_path


if __name__ == '__main__':
    load_dataset(save_path="/Users/mac/Documents/pyproject/sd_sdk/stardust_sdk/Stardust_SDK/data/",
                 project_id=1529, pool_lst=[])
