import time
import hashlib
from typing import Dict, List
from functools import wraps
import pickle
import requests

from stardust.config import MS as ms_config
from stardust.convertion.to_pandaset import to_pandaset
from stardust.rosetta.frames2frame import func_ms


def decoration(func_obj):
    """
    This decorator is mainly used to invalidate the method auth due to time-outs
    Returns:
    """

    @wraps(func_obj)
    def _func(ms, *args, **kwargs):
        try:
            ret = func_obj(ms, *args, **kwargs)
        except requests.exceptions.ConnectionError as e:
            raise requests.exceptions.ConnectionError("MorningStar connection failed")
        if ret.status_code == 502:
            setattr(ms, "auth", ms._auth())
            ret = func_obj(*args, **kwargs)
        return ret

    return _func


class MS:
    def __init__(self):
        self.config = ms_config
        self.app_key = f"{ms_config.domain}_OPEN_APP_KEY"
        self.auth = self._auth()

    def _md5(self, input_string) -> str:
        """
        Generates md5 digest of MS, dependent on time and OPEN_APP_KEY
        Args:
            input_string:

        Returns:
            str
        """
        return hashlib.md5(input_string.encode()).hexdigest()

    def _auth(self):
        self._time = time_value = int(time.time() * 1000)
        self.md5_value = self._md5(f"{str(time_value)}{self.app_key}")
        payload = {
            "appKey": self.app_key,
            "sign": self.md5_value,
            "createTime": self._time
        }
        resp = requests.post(self.config.url_auth,
                             headers={
                                 "Content-Type": "application/json"},
                             json=payload)
        assert resp.json()['code'] == 20, "Authentication failed"

    def _export_dataset_ms(self, dataset_id: int,
                           version_num: int,
                           slice_id: int = None,
                           page_no: int = 1,
                           page_size: int = 10
                           ) -> requests.Response:
        assert dataset_id and version_num
        url = self.config.url_export
        req_json = {
            "datasetId": dataset_id,
            "versionNum": version_num,
            "sliceId": slice_id,
            "pageNo": page_no,
            "pageSize": page_size,
            "appKey": self.app_key,
            "sign": self.md5_value,
            "createTime": self._time,
        }
        res = requests.post(url,
                            headers={
                                "Content-Type": "application/json"
                            },
                            json=req_json)
        return res

    def _create_dataset_ms(self, dataset_id: int,
                           data_instance_ids: List[str],
                           name: str,
                           description: str,
                           version_num: int
                           ) -> requests.Response:
        url = self.config.url_create
        req_json = {
            "datasetId": dataset_id,
            "dataInstanceIds": data_instance_ids,
            "appKey": self.app_key,
            "sign": self.md5_value,
            "createTime": self._time,
            "name": name,
            "description": description,
            "versionNum": version_num,
        }
        res = requests.post(url,
                            headers={
                                "Content-Type": "application/json"
                            },
                            json=req_json)
        return res

    def _import_dataeet_slice(self,
                              dataset_id: int,
                              model_id: int,
                              version_num: int,
                              annotation_result: List
                              ) -> requests.Response:
        url = self.config.url_import
        req_json = {
            "datasetId": dataset_id,
            "modelId": model_id,
            "versionNum": version_num,
            "appKey": self.app_key,
            "sign": self.md5_value,
            "createTime": self._time,
            "annotationResult": annotation_result
        }
        res = requests.post(url,
                            headers={
                                "Content-Type": "application/json"
                            },
                            json=req_json)
        return res

    # Export dataset content
    def export_dataset(self, **kwargs) -> Dict:
        """
        Export ms data and automatically detach consecutive frames

        Args:
            dataset_id: int
                Data set ID
            version_num: int
                Version number
            slice_id: int
                Slice ID
            page_no: int
                Slice paging
            page_size: int
                Amount of data per page

        Returns: Dict
            Derived data slicing

        Examples:
            .. code-block:: python

                from stardust.ms.ms import MS

                frame_gen = MS().export_dataset(
                    dataset_id=351787480925605888,
                    version_num=18
                )
                for frame in frame_gen:
                    pass

        """
        # Request dataset export from MorningStar
        resp = self._export_dataset_ms(**kwargs)
        assert isinstance(resp, requests.Response) and resp.status_code == 200, "Request failed"
        assert resp.json()['code'] == 2000, f"Dataset export failed, {resp.json()['message']}"

        # Split frames as needed
        ms_data = func_ms(resp.json())

        # Return generator to converter
        return ms_data

    # Create dataset slice
    def create_dataset(self, **kwargs) -> Dict:
        """
        Create a dataset slice

        Args:
            dataset_id: int
                Data set ID
            data_instance_ids: int
                Data instance ID
            name: int
                Slice name
            description: int
                Slice description

        Returns: Dict
            Create slice results

        Examples:
            .. code-block:: python

                from stardust.ms.ms import MS

                resp = MS().create_dataset(
                    dataset_id=352036425840988160,
                    data_instance_ids=[351787490434093056],
                    name="Slice 1",
                    description="description"
                )
                print(resp)

        """
        resp = self._create_dataset_ms(**kwargs)
        assert isinstance(resp, requests.Response) and resp.status_code == 200, "Request failed"
        assert resp.json()['code'] == 2000, f"Dataset creation failed, {resp.json()['message']}"
        return resp.json()

    # Import pre-processed slice
    def import_dataset_ms(self, **kwargs) -> Dict:
        """
        Import data set

        Args:
            dataset_id: int
                Data set ID
            model_id: int
                Model ID
            version_num: int
                Version number
            annotation_result: List
                Result of pretreatment

        Returns: Dict
            Import result

        Examples:
            .. code-block:: python

                from stardust.ms.ms import MS

                resp = MS().import_dataset_ms(
                    dataset_id=351787480925605888,
                    model_id="404",
                    version_num=1,
                    annotation_result=[
                          {
                            "annotation": {
                              "annotations": [
                                {
                                  "key": "3D box",
                                  "label": "3D box",
                                  "type": "slotChildren",
                                  "slotsChildren": [...]
                                }
                              ],
                              "operators": [...]
                            },
                            "dataInstanceId": "351787490434093056"
                          },
                          {
                            "annotation": {
                              "annotations": [...],
                              "operators": [...]
                            },
                            "dataInstanceId": "351787490622836736"
                          }
                        ]
                )
                print(resp)

        """
        resp = self._import_dataeet_slice(**kwargs)
        assert isinstance(resp, requests.Response) and resp.status_code == 200, "Request failed"
        assert resp.json()['code'] == 2000, f"Dataset import failed, {resp.json()['message']}"
        return resp.json()


if __name__ == "__main__":
    # Example export from MorningStar
    gen_data = MS().export_dataset(
        dataset_id=354992337446768640,
        version_num=3
    )
    for data in gen_data:
        print(data)
