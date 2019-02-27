from abc import ABC, abstractmethod
from typing import Union
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

    The main role to this extension is, make a request to a URL from SpaceXAPI
    and convert the result into a dict or a list.
    """

    def request(self) -> Union[list, dict]:
        """
        It returns a list or a dict created after the request.json().

        From last and next launches it will return a dict.

        From upcoming and past it will return a list.
        """
        request = requests.get(self.url)
        response = request.json()
        return response
