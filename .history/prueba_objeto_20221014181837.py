from Criptomonedas import Criptomoneda

"""ethereum = Criptomoneda("ETH ", 0.0, 454.543)
print(ethereum.mostrarNombre(), ethereum.calcularSaldo("USD"))"""

bitcoin = Criptomoneda("BTC", 0.34, 5000.00)
bitcoin.mostrarNombre()

bitcoin.calcularSaldo("USD")

bitcoin.indicarSaldo(0.5)
bitcoin.calcularSaldo("USD")

