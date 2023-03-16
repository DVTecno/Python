from time import sleep
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

def show(coin, aumento):
    if aumento != '':
        aumento= '+' if aumento else '-'
        print(f"{coin['simbolo']}: {coin['precio']:.4f} [{aumento}]")
    else:
        print(f"{coin['simbolo']}: {coin['precio']:.4f} []")

coins={}
coin_last={}
config=Config()
while True:
    coin_last=coins 
    coins= get_currency(config.url, config.headers, config.parameters)
    
    for key, coin in coins.items():
        if len(coin_last)==0 or coin['precio']== coin_last[key]['precio']:
            show(coin, '')
        elif coin['precio']> coin_last[key]['precio']:
            show(coin, True)
        else:
            show(coin, False)
    for i in range(0, 61):
        print(f"Esperando  para actualizar... {60-i:02d} seg", end='\r')
        sleep(1)
    print("\n")