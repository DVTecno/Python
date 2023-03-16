from datetime import datetime
# Bitcoin(BTC)
# Cardano(ADA)
# Ethereum(Ether)
# Bitcoin cash(BCH)
# Stellar(XLM)
# Chainlink(LINK)
# EOS(IO.EOS)
# Ripple(XRP)
def captu_cripto():
    criptomoneda = input("      Ingrese el Nombre de la Criptomoneda:")
    cantidad = float(input("        Ingrese la cantidad de su Criptomoneda ("+criptomoneda.upper()+"):"))
    cotizacion = float(input("      Cotización por USD del día de su : "+criptomoneda.upper()+" US$"))
    return cantidad*cotizacion
print("******************************************************")
print("         ************BIENVENIDOS************")
print("******************************************************")
i = 1
suma = 0
while i <= 5:
    suma = suma+captu_cripto()
    i += 1
hora = datetime.now()
print("******************************************************")
print("           ************INFORME************")
print("******************************************************")
print("Dia y hora, en la que se realizo la consulta")
print("      ______________________________________")
print(hora.strftime("      B%A %d/%B/%Y %I:%M:%S:%p"))
print("      ______________________________________")
print("******************************************************")
print("El valor de sus Criptomonedas es : USD$"+str(suma))
print("******************************************************")
print()
