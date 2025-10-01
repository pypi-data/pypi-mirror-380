"""
Utilities for Alibaba Cloud OSS storage.
"""
import oss2
from typing import List
from stardust.config import OssUser as OssConfig

__all__ = ["oss"]


# Account configuration
class OssAuth(object):
    def __init__(self):
        self.oss_key = OssConfig.oss_key
        self.oss_secret = OssConfig.oss_secret
        self.endpoint = OssConfig.endpoint
        self.prefix_url = OssConfig.prefix_url
        self.auth = oss2.Auth(self.oss_key, self.oss_secret)


class Oss(OssAuth):
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(Oss, cls).__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, bucket=OssConfig.oss_bucket, connect_timeout=None, enable_crc=True):
        super().__init__()
        self.bucket = oss2.Bucket(self.auth,
                                  self.endpoint,
                                  bucket,
                                  connect_timeout=connect_timeout,
                                  enable_crc=enable_crc)

    def load_oss_file_lst(self, file_lst: List = None):
        if not file_lst:
            return "empty"
        # Build batch download request
        batch = oss2.BatchGetObjectsRequest(bucket_name)
        for obj in object_list:
            batch.add_key(obj)

        # Execute batch download request
        result = bucket.batch_get_objects(batch)

        # Process download results
        for i, obj in enumerate(result.object_list):
            if obj.status == 200:
                save_path = 'path/to/save/' + object_list[i]  # Update save path to match your environment
                with open(save_path, 'wb') as f:
                    f.write(obj.read())
            else:
                print(f"Failed to download {object_list[i]}")

        print("Download completed.")


oss = Oss()
if __name__ == '__main__':
    oss = Oss()
    print(oss.bucket.object_exists("Clients/COSMO/ChatDataset/Production/LDC/.DS_Store"))
