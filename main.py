from requesters import RequesterToSpaceXAPI
from helpers import FormatterSpaceXAPI


requester_urls = {
    'latest': 'https://api.spacexdata.com/v3/launches/latest',
    'next': 'https://api.spacexdata.com/v3/launches/next',
    'upcoming': 'https://api.spacexdata.com/v3/launches/upcoming',
    'past': 'https://api.spacexdata.com/v3/launches/past',
}


options_menu = {
    'latest': 'Último Lançamento',
    'next': 'Próximo Lançamento',
    'upcoming': 'Próximos Lançamentos',
    'past': 'Lançamentos Passados'
}


def main():
    formatter = FormatterSpaceXAPI()
    while True:
        option = str()
        iterative_options = ['upcoming', 'past']

        for key, value in options_menu.items():
            print(f'[{key}] - {value}')
        option = input('Selecione uma das opções entre []\n')

        requester = RequesterToSpaceXAPI(requester_urls.get(option))
        response = requester.request()

        if option in iterative_options:
            for i in response:
                print(formatter.format(i))
        else:
            print(formatter.format(response))


if __name__ == '__main__':
    main()
