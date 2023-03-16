from datetime import datetime
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
def val_mon(cripto):
    criptos=["BTC", "BCC", "LTC", "ETH", "ETC", "XRP"]
    if cripto in criptos:
        return True
    else:
        return False
def val_num(numero):
        return numero.replace('.','', 1).isdigit()
saldo=0
i=0
while i<3: 
    cripto=input("Ingrese el Nombre de Moneda:->>").upper()
    if val_mon(cripto):
        i+=1
        cantidad=""
        while not val_num(cantidad):
            cantidad = input("Ingrese la cantidad de "+cripto+":->>")
        cotizacion="" 
        while not val_num(cotizacion):
            cotizacion = input("Ingrese la cotización en USD de  "+cripto+":->>")
        saldo=saldo+float(cantidad) *float(cotizacion)   
    else:
        print("Nombre de la Moneda incorrecta")
hora = datetime.now()
print("*********************************************************")
print("             ************INFORME************")
print("*********************************************************")
print("             Dia y hora, en la que se realizo la consulta")
print("                  _______________________________________")
print(hora.strftime("                    B%A %d/%B/%Y %I:%M:%S:%p"))
print("                  _______________________________________")
print("*********************************************************")
print("El saldo total en dolares americanos es :->>USD$"+str(saldo))
print("*********************************************************")
print("")
