from abc import ABC, abstractmethod
from typing import Union


class Formatter(ABC):
    @abstractmethod
    def format(self, json):
        pass


class FormatterSpaceXAPI(Formatter):
    def format(self, json: Union[dict, list]) -> str:
        """
        It return some info from a request response to SpaceXAPI.
        """
        retorno_formatado = f'''
Número do voo: {json.get("flight_number")}
Nome da missão: {json.get("mission_name")}
Ano de lançamento: {json.get("launch_year")}
Data de lançamento UTC: {json.get("launch_date_utc")}
Nome do foguete: {json.get("rocket").get("rocket_name")}
Plataforma de Lançamento: {json.get("launch_site").get("site_name")}
        '''
        return retorno_formatado
