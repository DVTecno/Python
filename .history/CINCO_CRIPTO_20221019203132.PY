from types import ClassMethodDescriptorType
from unittest import result
import requests

class Config:
    def __init__(self):
        self.url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self.headers={
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'fea42815-ebda-4b39-9a22-3e057beda67d'
        }
        self.parameters={
            'limit': '5',
            'convert': 'USD',
            'sort': 'market_cap'
        }

def get_currency(url, headers, parameters):
    result=requests.get(url, headers=headers, params=parameters)
    cripto_lastast=result.json()['data']
    coins={}
    if (cripto_lastast):
        for cripto in cripto_lastast:
            coin={}
            coin['nombre'] = cripto['name']
            coin['simbolo'] = cripto['symbol']
            coin['precio'] = cripto['quote']['USD']['price']
            coin['volumen_24h'] = cripto['quote']['USD']['volume_24h']
            coins[coin['simbolo']]=coin
        return coins