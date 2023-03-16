import requests
url='https://pro-api.coinmarketcap.com/v1/crutocurrency/listings/latest'
headers={
    'Accepts': 'application/json', 
    'X-CMC_PRO_API_KEY' :'fea42815-ebda-4b39-9a22-3e057beda67d'
}
parameters={
    'limit':'10',
    'convert':'USD',
    'sort':'volume_24h'
}
result=requests.get(url,headers=headers, params=parameters)
cripto_lastest=result.json()['data']

if (cripto_lastest):
    for cripto in cripto_lastest:
        print(f"Nombre: {cripto['name']}")
        print(f"Simbolo: {cripto['symbol']}")