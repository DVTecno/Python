from Criptomonedas import Criptomoneda

"""ethereum = Criptomoneda("ETH ", 0.0, 454.543)
print(ethereum.mostrarNombre(), ethereum.calcularSaldo("USD"))"""

bitcoin = Criptomoneda("BTC", 0.34, 5000.00)
print(bitcoin.mostrarNombre())
print(bitcoin.calcularSaldo("USD"))
bitcoin.indicarSaldo(0.5)
print(bitcoin.calcularSaldo("USD"))

litecoin=Criptomoneda("LtC",1.67,124.00)
print(litecoin.mostrarNombre())
print(litecoin.calcularSaldo("USD"))
litecoin.indicarCotizacion(154.45)
print(litecoin.calcularSaldo("USD"))
ripple=Criptomoneda("XPR",34.93,0.4785)
print(ripple.mostrarNombre())



