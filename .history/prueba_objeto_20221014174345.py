from Criptomonedas import Criptomoneda
ethereum = Criptomoneda("ETH ", 0.0, 454.543)
print(ethereum.mostrarNombre(), ethereum.calcularSaldo("USD"))
>> > from Criptomonedas import Criptomoneda
>> > bitcoin = Criptomoneda("BTC", 0.34, 5000.00)
>> > bitcoin.mostrarNombre()
"BTC"
>> > bitcoin.calcularSaldo("USD")
1700.0000000000002
>> > bitcoin.indicarSaldo(0.5)
>> > bitcoin.calcularSaldo("USD")
2500.0

"""class Criptomoneda(object):
    def __init__(self, nombre,  saldo, cotizacion):
    self.nombre = nombre
    self.saldo = saldo
    self.cotizacion = cotizacion
 
def indicarNombre(self, nombre):
    self.nombre=nombre
 
def indicarCotizacion(self, cotizacion):
    self.cotizacion=cotizacion
 
def indicarSaldo(self, saldo):  
    self.saldo=saldo
 
def mostrarNombre(self):
    return self.nombre
 
def imostrarCotizacion(self): 
    return self.cotizacion
 
def mostrarSaldo(self):  
    return  self.saldo
 
def calcularSaldo(self, moneda):  
    if moneda== “USD”:
        return self.saldo*self.cotizacion
    else:
        return self.saldo"""