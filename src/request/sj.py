import dotenv
import requests
from dotenv import load_dotenv
from config import URL_SJ
from src.abstract_class_api import AbstractJobAPI
from src.data_json.work_with_json import WorkWithJsonSJ


config = dotenv.dotenv_values('.env')


class RequestSJ(AbstractJobAPI):
    def __init__(self, keyword, page=1):
        self.url = URL_SJ
        self.params = {'keywords': keyword, 'page': page}

    def connect_to_api(self):
        pass

    def request(self) -> dict:
        headers = {
            "X-Api-App-Id": 'v3.r.137982883.d4c48acc4f12815b610190faa57a4a8392da17a8.a05cf674745962498d2e32bef467f0643bad6cd1'
        }
        response = requests.get(self.url, params=self.params, headers=headers)
        return WorkWithJsonSJ.save_json(response.json()["objects"])
