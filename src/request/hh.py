import requests

from config import URL_HH
from src.abstract_class_api import AbstractJobAPI
from src.data_json.work_with_json import WorkWithJsonHH


class RequestHH(AbstractJobAPI):
    def __init__(self, keyword, area=113):
        self.url = URL_HH
        self.keyword = keyword
        self.area = area
        self.parameter = {'text': self.keyword, 'area': self.area}

    def request(self):
        response = requests.get(self.url, self.parameter)
        WorkWithJsonHH.save_json(response.json()['items'])
