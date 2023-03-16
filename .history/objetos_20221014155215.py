from abc import ABC,abstractmethod
class Figura(ABC):
    def __init__(self,nombre):
        self.nombre=nombre
    @abstractmethod
    def area(self):
        pass
    def perimetro(self):
        pass
class Rectangulo    
            