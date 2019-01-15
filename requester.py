from abc import ABC, abstractmethod
import requests
from helpers import dict_creator


class Requester(ABC):
    @abstractmethod
    def request(self):
        pass


class RequesterLatestLauch(Requester):
    def request(self):
        """Return the latest launch info.

        It should return the info about the latest launch as a json.

        """
        r = requests.get('https://api.spacexdata.com/v3/launches/latest')
        return r.json()


class RequesterNextLauch(Requester):
    def request(self):
        """Return the next launch info.

        It should return the info about the next launch as a json.
        """
        r = requests.get('https://api.spacexdata.com/v3/launches/next')
        return r.json()


class RequesterUpcomingLauches(Requester):
    def request(self):
        """Return the upcoming launches.

        It should return the infor for all the upcoming launches.
        """
        r = requests.get('https://api.spacexdata.com/v3/launches/upcoming')
        return r.json()


class RequesterPastLauches(Requester):
    def request(self):
        """Return the past launches.

        It should return the info for all the past launches.
        """
        r = requests.get('https://api.spacexdata.com/v3/launches/past')
        return r.json()


if __name__ == '__main__':
    r = Requester()
    print(f'Latest info\n{dict_creator(r.request_latest_launch())}\n')
    print(f'Next lauch info\n{dict_creator(r.request_next_launch())}\n')

    for launch in r.request_upcoming_launches():
        print(f'{dict_creator(launch)}\n')

    print('Past Launches \n')
    for launch in r.request_past_launches():
        print(f'{dict_creator(launch)}\n')
