from datetime import datetime
from traceback import print_stack
# Bitcoin(BTC) Cardano(ADA) Ethereum(Ether) Bitcoin cash(BCH) Litecoin(LTC)
# Stellar(XLM) Chainlink(LINK) EOS(IO.EOS) Ripple(XRP) Dash(DASH)
print("******************************************************")
print("         ************BIENVENIDOS************")
print("******************************************************")
BTCUSD=7630.80
DASHUSD=315.56
LTCUSD=120.84
moneda = input("Indique la moneda de transacción(BTC, DASH o LTC): ").upper()
if moneda=="BTC" or moneda=="DASH" or moneda=="LTC":
    cantidad = float(
        input("Indique el monto, de su Criptomoneda a recargar: "))
    if moneda=="BTC":
        saldo_movil=cantidad*BTCUSD
    elif moneda=="DASH":
        saldo_movil=cantidad*DASHUSD
    else:
        saldo_movil=cantidad*LTCUSD
else:
    print("ERROR: Monedas permitidas BTC, DASH o LTC")
hora = datetime.now()
print("******************************************************")
print("         *********SISTEMA DE RECARGA*********")
print("******************************************************")
print("Dia y hora, en la que se realizo la recarga")
print("      ______________________________________")
print(hora.strftime("      B%A %d/%B/%Y %I:%M:%S:%p"))
print("      ______________________________________")
print("******************************************************")
print("Moneda de pago utilizada para abonar: "+moneda)
print("Su saldo acreditado es: USD$"+str(saldo_movil))
print("******************************************************")
print("")
