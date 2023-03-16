from datetime import datetime
import requests
_ENDPOINT = "https://api.binance.com"
# Bitcoin(BTC) Cardano(ADA) Ethereum(Ether) Bitcoin cash(BCH) Litecoin(LTC)
# Stellar(XLM) Chainlink(LINK) EOS(IO.EOS) Ripple(XRP) Dash(DASH)
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
def esmoneda(cripto):
    criptos=["BTC","BCC","LTC","ETH","ETC","XRP"]
    return cripto in criptos
def esnumero(numero):
    return numero.replace('.','',1).isdigit()
monedas=[]    
cantidades=[]
cotizaciones=[]
i=0
while i<3:
    moneda=input("Ingrese el Nombre de Moneda:->>").upper()
    while not esmoneda(moneda):
        print("ERROR: Monedas permitidas BTC, BCC, LTC, ETH, ETC, XRP o LTC")
        moneda=input("Ingrese el Nombre de Moneda:->>").upper()
    else:
        monedas.append(moneda)
        data=get_price(moneda+"USDT").json()
        cotizaciones.append(float(data["price"]))
        cantidad=input("Indique la cantidad de ("+moneda+"):->>")
        while not esnumero(cantidad):
            cantidad = input("Indique la cantidad de ("+moneda+"):->>")
        else:
            cantidades.append(float(cantidad))
    i+=1
hora = datetime.now()
print("*********************************************************")
print("                  ************INFORME DE CONSULTA************")
print("******************************************************************************")
print("                                  Dia y hora, en la que se realizo la consulta")
print("                                       ______________________________________")
print(hora.strftime("                                        B%A %d/%B/%Y %I:%M:%S:%p"))
print("                                       ______________________________________")
print("******************************************************************************")
i=0
total=0
while i<3:
    total+=cantidades[i]*cotizaciones[i]
    print("MONEDA: ",monedas[i],
          "CANTIDAD: ",cantidades[i],
          "COTIZACIÓN: ",cotizaciones[i],
          "Cantidad de USDT: ",cantidades[i]*cotizaciones[i])
    i+=1
print("******************************************************************************")
print("El saldo total en dolares americanos es :->>USD$"+str(total))
print("******************************************************************************")
print("")
