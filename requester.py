import requests
from helpers import dict_creator


class Requester():
    def request_latest_lauch(self):
        """Return the latest lauch info.

        It should return the info about the latest launch as a json.

        """
        r = requests.get('https://api.spacexdata.com/v3/launches/latest')
        return r.json()

    def request_next_launch(self):
        """Return the next lauch info.

        It should return the info about the next lauch as a json.
        """
        r = requests.get('https://api.spacexdata.com/v3/launches/next')
        return r.json()


if __name__ == '__main__':
    r = Requester()
    print(f'Latest info\n{dict_creator(r.request_latest_lauch())}\n')
    print(f'Next lauch info\n{dict_creator(r.request_next_launch())}\n')
