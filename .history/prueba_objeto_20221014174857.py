from Criptomonedas import Criptomoneda
ethereum = Criptomoneda("ETH ", 0.0, 454.543)



bitcoin = Criptomoneda("BTC", 0.34, 5000.00)
bitcoin.mostrarNombre()
"BTC"
bitcoin.calcularSaldo("USD")
1700.0000000000002
bitcoin.indicarSaldo(0.5)
bitcoin.calcularSaldo("USD")
2500.0
print(ethereum.mostrarNombre(), ethereum.calcularSaldo("USD"))

