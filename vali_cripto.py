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
criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]
count=0
acumulado=0
while count<3 :
    cripto = input("Ingrese el Nombre de la Moneda:->>").upper()
    if cripto in criptos:
        cantidad = float(input("Ingrese la cantidad de "+cripto +":->>"))
        cotizacion = float(input("Indique la cotización en USD de "+cripto+":->>"))
        acumulado=acumulado+(cantidad*cotizacion)
        count+=1
    else:
        print("Moneda Incorrecta, (intente nuevamente)")
hora = datetime.now()
print("*********************************************************")
print("             ************INFORME************")
print("*********************************************************")
print("             Dia y hora, en la que se realizo la consulta")
print("                  _______________________________________")
print(hora.strftime("                    B%A %d/%B/%Y %I:%M:%S:%p"))
print("                  _______________________________________")
print("*********************************************************")
print("El saldo acumulado en dolares americanos es :usd$"+str(acumulado))  
print("*********************************************************")
print("")
