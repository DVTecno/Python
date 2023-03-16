from datetime import datetime
# Bitcoin(BTC)
# Cardano(ADA)
# Ethereum(Ether)
# Bitcoin cash(BCH)
# Stellar(XLM)
# Chainlink(LINK)
# EOS(IO.EOS)
# Ripple(XRP)
print("******************************************************")
print("         ************BIENVENIDOS************")
print("******************************************************")
def conversion_cripto(cant_BTC, cant_XRP):
    BTCUSD = 7442.50*cant_BTC
    XRPUSD = 0.660982*cant_XRP
    saldo_totalUSD = BTCUSD+XRPUSD
    return saldo_totalUSD
cantBTC = float(input("     Ingrese la cantidad de Bitcoin:"))
cantXRP = float(input("     Ingrese la cantidad de Ripple:"))
hora = datetime.now()
print("******************************************************")
print("           ************INFORME************")
print("******************************************************")
print("Dia y hora, en la que se realizo la consulta")
print("      ______________________________________")
print(hora.strftime("      B%A %d/%B/%Y %I:%M:%S:%p"))
print("      ______________________________________")
print("")
print("**********************************************************************")
print("Su valor de Criptomonedas, en Dólares Americano es: USD$" +
str(conversion_cripto(cantBTC, cantXRP)))
print("**********************************************************************")
print("")
