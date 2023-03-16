import requests
def esmoneda(cripto):
    return cripto in monedas

data={}
monedas = ()
monedas_dict = {}

COINMARKET_API_KEY = "fea42815-ebda-4b39-9a22-3e057beda67d"
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}

data=requests.get("https://api.coimnmarketcap.com/v2/ticker/").json
for id in data["data"]:
    monedas_dict[data["data"][id]["symbol"]]=data["data"][id]["quotes"]["USD"]["price"]

monedas=monedas_dict.keys()
moneda = input("Ingrese el Nombre de la moneda:->>").upper()
while not esmoneda(moneda):
    print("moneda invalida")
    moneda = input("Ingrese el Nombre de la moneda:->>").upper()
else:
    print("La moneda con Symbol:",moneda,
          "tiene un precio de:",monedas_dict.get(moneda),"USD")