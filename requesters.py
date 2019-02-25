from abc import ABC, abstractmethod

import requests


class AbstractRequester(ABC):
    """
    Just an abstract class.
    """
    def __init__(self, url: str) -> None:
        self.url = url

    @abstractmethod
    def request(self):
        pass


class RequesterToSpaceXAPI(AbstractRequester):
    """
    An extension from AbstractRequester.

    The main role to this extension is, make a request to a URL and
    convert the result into a dict.
    """
    def request(self) -> dict:
        request = requests.get(self.url)
        return request.json()
