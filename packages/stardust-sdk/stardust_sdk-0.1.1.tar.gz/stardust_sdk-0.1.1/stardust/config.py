import os
import configparser
from datetime import datetime

now_time = datetime.now().strftime('%Y%m%d%H%M')
absolute_path = os.path.dirname(__file__)
config = configparser.ConfigParser()

config_path = f'{os.path.dirname(os.path.abspath(__file__))}/config.ini'
assert os.path.exists(config_path)
config.read(config_path)


# OSS credentials
class OssUser:
    oss_key = config.get('OssUser', 'key')
    oss_secret = config.get('OssUser', 'secret')
    oss_bucket = config.get('OssUser', 'bucket')
    endpoint = config.get('OssUser', 'endpoint')
    prefix_url = config.get('OssUser', 'prefix_url')


# Rosetta credentials
class RosUser:
    username = int(config.get('RosUser', 'username'))
    password = config.get('RosUser', 'password')


class RosConfig:
    env_prod = config.get('RosConfig', 'env_prod')
    env_dev = config.get('RosConfig', 'env_dev')


class SavePath:
    input_rosetta_path = os.path.join(absolute_path, f'api/static/input')
    export_rosetta_path = os.path.join(absolute_path, f'api/static/star_export')


# MorningStar configuration
class MS:
    domain = "ROSETTA"
    url_auth = "https://portal-uat.rosettalab.top/rosetta-open/token/verify"
    url_export = "https://portal-uat.rosettalab.top/rosetta-open/dataset/export"
    url_create = "https://portal-uat.rosettalab.top/rosetta-open/dataset/slice"
    url_import = "https://portal-uat.rosettalab.top/rosetta-open/dataset/import"
