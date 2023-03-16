from email import header
from wsgiref import headers
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

