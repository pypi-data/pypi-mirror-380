"""
    Get rosetta pool information
"""
import requests

from stardust.rosetta.rosetta_token import RosettaToken
from stardust.config import RosConfig

__all__ = ['RosettaPool']


class RosettaPool:
    sever_map = {
        'top': RosConfig.env_prod,
        'dev': RosConfig.env_dev
    }

    def __init__(self, env: str = 'top'):
        self.env = self.sever_map[env]
        self.headers: dict = RosettaToken(self.env).get_headers()

    def get_pool_info(self, project_id: int):
        url = f'{self.env}/rosetta-service/project/doneTask/get?projectId={project_id}'
        res = requests.get(url, headers=self.headers)
        res_data = res.json()
        pool_list = [{
            i['poolId']: i['poolName']} for i in res_data['data']]
        return pool_list

    def get_all_finish_pool_info(self, project_id: int):
        url = f'{self.env}/rosetta-service/project/doneTask/get?projectId={project_id}'
        res = requests.get(url, headers=self.headers)
        res_data = res.json()
        assert res_data['code'] not in  (5802, )
        pool_list = [i['poolId'] for i in res_data['data']]
        assert pool_list, ValueError(f'Project {project_id} has no completed pools')
        return pool_list


if __name__ == '__main__':
    pool = RosettaPool()
    print(pool.get_pool_info(1337))
    print(pool.get_all_finish_pool_info(1337))
