import requests
from helpers import dict_creator


class Requester():
    def request_latest_lauch(self):
        r = requests.get('https://api.spacexdata.com/v3/launches/latest')
        resposta = dict_creator(r.json())
        return resposta


if __name__ == '__main__':
    r = Requester()
    print(r.request_latest_lauch())
