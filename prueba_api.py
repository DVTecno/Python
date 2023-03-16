from datetime import datetime
from ast import If
import requests
_ENDPOINT = "https://api.binance.com"
#Bitcoin(BTC)
#Cardano(ADA)
#Ethereum(Ether)
#Bitcoin cash(BCH)
#Stellar(XLM)
#Chainlink(LINK)
#EOS(IO.EOS)
print("******************************************************")
print("         ************BIENVENIDOS************")
print("******************************************************")
print("            Moneda disponibles en consulta")
print("            _____________________________")
print("            BTC, BCC, LTC, ETH, ETC , XRP")
print("******************************************************")
def _url(api):
    return _ENDPOINT+api
def get_price(cripto):
    return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))
def val_cripto(cripto):
    criptos=["BTC","BCC","LTC","ETH","ETC","XRP"]
    if cripto in criptos:
        return True
    else:
        return False
moneda=""
while not val_cripto(moneda):
    moneda=input("Ingrese el Nombre de la Moneda a Cotizar: ").upper()
data=get_price(moneda+"USDT").json() 
hora = datetime.now()
print("*********************************************************")
print("             ************INFORME************")
print("*********************************************************")
print("             Dia y hora, en la que se realizo la consulta")
print("                  _______________________________________")
print(hora.strftime("                    B%A %d/%B/%Y %I:%M:%S:%p"))
print("                  _______________________________________")
print("*********************************************************")
print("El precio de ",moneda,"es:->>USDT",data["price"]) 
print("*********************************************************")
print("")
