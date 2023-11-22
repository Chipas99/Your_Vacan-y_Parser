from abc import ABC, abstractmethod


class AbstractJobAPI(ABC):
    @abstractmethod
    def request(self):
        pass
