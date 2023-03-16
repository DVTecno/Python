from email import header
from wsgiref import headers
import requests

from symbol import parameters

url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers={
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'fea42815-ebda-4b39-9a22-3e057beda67d'
}

parameters={
    'limit': '5',
    'convert': 'USD',
    'sort': ''
}