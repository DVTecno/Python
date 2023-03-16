from datetime import datetime
import requests
# Bitcoin(BTC) Cardano(ADA) Ethereum(Ether) Bitcoin cash(BCH) Litecoin(LTC)
# Stellar(XLM) Chainlink(LINK) EOS(IO.EOS) Ripple(XRP) Dash(DASH)
print("******************************************************")
print("         ************BIENVENIDOS************")
print("******************************************************")
print("                Ejemplo en consulta")
print("            _____________________________")
print("            BTC, BCC, LTC, ETH, ETC , XRP")
print("******************************************************")
def esmoneda(cripto):
    return cripto in monedas
monedas = ()
monedas_dict = {}
COINMARKET_API_KEY = "fea42815-ebda-4b39-9a22-3e057beda67d"
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}
data = requests.get(
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest", headers=headers).json()
for cripto in data["data"]:
    monedas_dict[cripto["symbol"]] = cripto["name"]
monedas = monedas_dict.keys()
hora = datetime.now()
i = 0
while i < 3:
    i += 1
    moneda = input("Ingrese el nombre de la moneda:->>").upper()
    while not esmoneda(moneda):
        print("ERROR: Monedas Equivocada")
        moneda = input("Ingrese el nombre de la Moneda:->>").upper()
    else:
        print(
            "*******************************************************************************************")
        print("                  ************INFORME DE CONSULTA************")
        print(
            "*******************************************************************************************")
        print("                                              Dia y hora, en la que se realizo la consulta")
        print("                                                    ______________________________________")
        print(hora.strftime("                                                    B%A %d/%B/%Y %I:%M:%S:%p"))
        print("                                                    ______________________________________")
        print( 
            "*******************************************************************************************")
        print(
            "*******************************************************************************************")
        print("La Moneda con Symbol:", moneda,
              "y nombre:", monedas_dict.get(moneda),
              "es valida porque existe en coimnmarketcap.com")
        print(
            "*******************************************************************************************")

