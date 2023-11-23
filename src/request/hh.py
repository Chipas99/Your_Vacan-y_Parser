import requests

from src.abstract_class_api import AbstractJobAPI


class RequestHH(AbstractJobAPI):
    def __init__(self, keyword, area=113):
        self.url = 'https://api.hh.ru/vacancies'
        self.keyword = keyword
        self.area = area
        self.parameter = {'text': self.keyword, 'area': self.area}

    def request(self):
        responce = requests.get(self.url, self.parameter)
        return responce.json()
