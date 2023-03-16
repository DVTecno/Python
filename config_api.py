import requests

def esmoneda(cripto):
    return cripto in monedas

monedas_list = []
#COINMARKET_API_KEY = "fea42815-ebda-4b39-9a22-3e057beda67d"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY':  'fea42815-ebda-4b39-9a22-3e057beda67d'
}

data = requests.get(
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest", headers=headers).json()
for cripto in data["data"]:
    monedas_list.append(cripto["symbol"])
    
monedas = tuple(monedas_list)

moneda = input("Ingrese el Nombre de la Moneda a verificar:->>")
while not esmoneda(moneda):
    print("ERROR: MONEDA INVALIDA")
    moneda = input("Ingrese el Nombre de la Moneda a verificar:->>")
else:
    print("La moneda,", moneda, "es valida porque existe en COIMNMARKETCAP.COM")