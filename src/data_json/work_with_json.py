import json
from abc import ABC, abstractmethod
from typing import Any, Dict

from config import JSON_HH, JSON_SJ


class WorkWithJsonAbstract(ABC):
    @classmethod
    @abstractmethod
    def save_json(cls, data: Dict[str, Any]) -> None:
        """
        Метод сохраняет предоставленные данные в файл JSON.

        Параметры:
        - данные (Dict[str, Any]): данные для b
        """
        pass

    @classmethod
    @abstractmethod
    def read_json(cls) -> Dict[str, Any]:
        """
        Чтение и возврат данных из файла JSON.

         Возврат:
         - Dict[str, Any]: данные, считанные из файла JSON.
        """
        pass


class WorkWithJsonHH(WorkWithJsonAbstract):
    path = JSON_HH

    @classmethod
    def save_json(cls, data):
        """
        Сохранение json с сайта в файл.
        """
        with open(cls.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def read_json(cls):
        """
        Чтение json.
        """
        with open(cls.path, 'w', encoding='utf-8') as file:
            return json.load(file)


class WorkWithJsonSJ(WorkWithJsonAbstract):
    path = JSON_SJ

    @classmethod
    def save_json(cls, data):
        """
        Сохранение json с сайта в файл.
        """
        with open(cls.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def read_json(cls):
        """
        Чтение json.
        """
        with open(cls.path, 'w', encoding='utf-8') as file:
            return json.load(file)
