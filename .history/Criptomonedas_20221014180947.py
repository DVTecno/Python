class Criptomoneda(object):
    def __init__(self, nombre,  saldo, cotizacion):
        self.nombre = nombre
        self.saldo = saldo
        self.cotizacion = cotizacion

    def indicarNombre(self, nombre):
        self.nombre = nombre

    def indicarCotizacion(self, cotizacion):
        self.cotizacion = cotizacion

    def indicarSaldo(self, saldo):
        self.saldo = saldo

    def mostrarNombre(self):
        return self.nombre

    def imostrarCotizacion(self):
        return self.cotizacion

    def mostrarSaldo(self):
        return self.saldo

    def calcularSaldo(self, moneda):
        if moneda == "USD":
            return self.saldo*self.cotizacion
        else:
            return self.saldo
