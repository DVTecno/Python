import requests
# La url se consigue en la pagina de la api
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

#key provista por la api
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'fea42815-ebda-4b39-9a22-3e057beda67d'
}
#parameter's y formato de la info solicitada
parameters = {
    'limit': '50',
    'convert': 'USD',
    'sort': 'volume_24h'
}
#formato de la info solicitada devuelta en j.son ['data']
result = requests.get(url, headers=headers, params=parameters)
cripto_lastest = result.json()['data']
#Impression por pantalla de toda la info 
if (cripto_lastest):
    for cripto in cripto_lastest:
        print(f"Nombre: {cripto['name']}")
        print(f"Simbolo: {cripto['symbol']}")
        print(f"Precio: {cripto['quote']['USD']['price']}")
        print(
            f"Volumen de monedas en 24hs: {cripto['quote']['USD']['volume_24h']}")
        print('\n')
