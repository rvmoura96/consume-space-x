from abc import ABC, abstractmethod

import requests


class Requester(ABC):
    @abstractmethod
    def request(self):
        pass


class RequesterLatestLaunch(Requester):
    def request(self):
        """Return the latest launch info.

        It should return the info about the latest launch as a json.
        """
        r = requests.get('https://api.spacexdata.com/v3/launches/latest')
        return r.json()


class RequesterNextLaunch(Requester):
    def request(self):
        """Return the next launch info.

        It should return the info about the next launch as a json.
        """
        r = requests.get('https://api.spacexdata.com/v3/launches/next')
        return r.json()


class RequesterUpcomingLaunches(Requester):
    def request(self):
        """Return the upcoming launches.

        It should return the infor for all the upcoming launches.
        """
        r = requests.get('https://api.spacexdata.com/v3/launches/upcoming')
        return r.json()


class RequesterPastLaunches(Requester):
    def request(self):
        """Return the past launches.

        It should return the info for all the past launches.
        """
        r = requests.get('https://api.spacexdata.com/v3/launches/past')
        return r.json()
