import requests
import urllib3
import json
import re

# Using cache to prevent API range limit
from functools import lru_cache

from .exceptions import InvalidCNPJError, CNPJNotFoundError, OpenCNPJError
from .utils import return_number, format

# Prevent warnings about endpoint SSL certificates
urllib3.disable_warnings()

class OpenCnpj():
    """
        Pass HTTP and HTTPs proxies as dict if working under a proxy server
    """
    def __init__(self, proxies = None):
        self.OPEN_CNPJ_ENDPOINT = 'https://api.opencnpj.org/'
        self.proxies = proxies

    def __is_valid(self, cnpj: str):
        pattern = re.compile(r'^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$')
        return bool(pattern.fullmatch(cnpj))

    @lru_cache(maxsize=1000)
    def get(self, cnpj: str) -> dict:
        """
        Return CNPJ data
        """
        try:
            if not self.__is_valid(cnpj):
                raise InvalidCNPJError("Format not valid")
        except TypeError:
            raise OpenCNPJError("You need to provide a String type")
        
        if not self.exists(cnpj):
            raise CNPJNotFoundError('CNPJ not found')

        endpoint = self.OPEN_CNPJ_ENDPOINT + cnpj
        response = requests.get(endpoint, verify=False, proxies=self.proxies)
        return json.loads(response.text)
    
    @lru_cache(maxsize=1000)
    def exists(self, cnpj: str) -> bool:
        """
        Return if CNPJ exists
        """
        if not self.__is_valid(cnpj):
            raise InvalidCNPJError("Format not valid")
        
        endpoint = self.OPEN_CNPJ_ENDPOINT + cnpj
        response = requests.get(endpoint, verify=False, proxies=self.proxies)
        return response.status_code == 200
    
    def format_cnpj(self, raw_cnpj: str) -> str:
        """
        Turn into humanized CNPJ(e.g: 00.000.000/0001-00)
        """

        # Return only number and remove None value
        try:
            clean_cnpj = [return_number(char) for char in raw_cnpj if return_number(char) is not None]
        except TypeError:
            raise OpenCNPJError("You need to provide a String type")

        if len(clean_cnpj) != 14:
            raise InvalidCNPJError("CNPJ must have 14 numbers")


        return format(clean_cnpj)
    