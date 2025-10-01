import os
import shutil
from io import BytesIO
from zipfile import ZipFile


class File:
    def __init__(self):
        pass

    @staticmethod
    def mkdir(path: str):
        if os.path.isfile(path):
            dir_path = os.path.dirname(path)
            os.makedirs(dir_path, exist_ok=True)
        else:
            dir_path = path
            os.makedirs(path, exist_ok=True)
        return dir_path

    @staticmethod
    def rmfile(path: str):
        os.remove(path)

    @staticmethod
    def rmdir(path: str):
        shutil.rmtree(path)

    @staticmethod
    def to_unzip(byte_data: bytes, path: str):
        zip_data = BytesIO(byte_data)
        z_file = ZipFile(zip_data, 'r')
        for zf in z_file.namelist():
            z_file.extract(zf, path)
        z_file.close()
        return path


if __name__ == '__main__':
    path = '/Users/stardust/Desktop/shangqi'
    File.rmdir(path)
