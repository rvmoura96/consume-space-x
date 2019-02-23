from abc import ABC, abstractmethod

import requests


class AbstractRequester(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def request(self):
        pass


class Requester(AbstractRequester):
    def request(self):
        request = requests.get(self.url)
        return request.json()
