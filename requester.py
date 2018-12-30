import requests
from helpers import dict_creator


class Requester():
    def request_latest_launch(self):
        """Return the latest launch info.

        It should return the info about the latest launch as a json.

        """
        r = requests.get('https://api.spacexdata.com/v3/launches/latest')
        return r.json()

    def request_next_launch(self):
        """Return the next launch info.

        It should return the info about the next launch as a json.
        """
        r = requests.get('https://api.spacexdata.com/v3/launches/next')
        return r.json()

    def request_upcoming_launches(self):
        """Return a list with upcoming launches."""
        r = requests.get('https://api.spacexdata.com/v3/launches/upcoming')
        return r.json()


if __name__ == '__main__':
    r = Requester()
    print(f'Latest info\n{dict_creator(r.request_latest_launch())}\n')
    print(f'Next lauch info\n{dict_creator(r.request_next_launch())}\n')

    for launch in r.request_upcoming_launches():
        print(f'{dict_creator(launch)}\n')
