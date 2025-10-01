"""
    Get a token for the rosetta platform
"""
__all__ = ['RosettaToken']
import time
import random
import json

import requests

from stardust.config import RosConfig, RosUser


class Auth:
    def __init__(self):
        self.username: str = RosUser.username
        self.password: str = RosUser.password


class RosettaToken(Auth):
    def __init__(self, env: str):
        super().__init__()
        self.login_url: str = f'{env}/rosetta-service/user/login'
        self.session_id: str = ''
        self.authorize: str = ''

    def get_authorize(self):
        headers = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
        }
        data = {
            "username": self.username,
            "password": self.password
        }
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(self.login_url, headers=headers, data=data)
        self.authorize = response.json()['data']['tokenValue']

    def get_headers(self):
        def generate_string():
            r = 20
            n = [''] * r
            o = list(str(int(time.time() * 1000))[::-1])
            for i in range(r):
                e = random.randint(0, 35)
                t = str(e if e < 26 else chr(e + 87))
                n[i] = t if e % 3 else t.upper()
            for i in range(8):
                n.insert(3 * i + 2, o[i])
            return ''.join(n[::-1])

        self.session_id = generate_string()
        self.get_authorize()
        headers = {
            "authority": "server.rosettalab.top",
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN",
            "authorize": self.authorize,
            "content-type": "application/json",
            "eagleeye-sessionid": self.session_id,
            "origin": "https://rosettalab.top",
            "referer": "https://rosettalab.top/",
            "sec-ch-ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
        }
        return headers


if __name__ == '__main__':
    exp = RosettaToken(RosConfig.env_prod)
    exp.get_authorize()
    print(exp.get_headers())
