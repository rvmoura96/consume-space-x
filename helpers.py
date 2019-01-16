from abc import ABC, abstractmethod


class Formatter(ABC):
    @abstractmethod
    def format(self, json):
        pass


class SimpleFormatter(Formatter):
    def format(self, json):
        quebra = '\n'
        retorno_formatado = (
            f'Número do voo: {json.get("flight_number")}{quebra}'
            f'Nome da missão: {json.get("mission_name")}{quebra}'
            f'Ano de lançamento: {json.get("launch_year")}{quebra}'
            f'Data de lançamento UTC: {json.get("launch_date_utc")}{quebra}'
            f'Nome do foguete: {json.get("rocket_name")}{quebra}'
            f'Plataforma de Lançamento: {json.get("launch_site").get("site_name")}'
        )
        return retorno_formatado
