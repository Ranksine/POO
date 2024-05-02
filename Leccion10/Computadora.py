from Monitor import Monitor
from Teclado import  Teclado
from Raton import Raton
class Computadora(Monitor, Teclado, Raton):
    contadorComputadoras = 0

    def __init__(self, nombre, marcaMonitor, tamaño, tipoEntradaT, marcaTeclado, tipoEntradaR, marcaRaton):
        Computadora.contadorComputadoras += 1
        self._idComputadora = Computadora.contadorComputadoras
        Monitor.__init__(self, marcaMonitor, tamaño)
        Teclado.__init__(self, tipoEntradaT, marcaTeclado)
        Raton.__init__(self, tipoEntradaR, marcaRaton)
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self.monitor

    @property
    def teclado(self):
        return self.teclado

    @property
    def raton(self):
        return self.raton

    def __str__(self):
        return f'   [Computadora: (ID_Computadora: {self._idComputadora})\n      Nombre: {self.nombre}\n      Monitor: {Monitor.__str__(self)}\n      Teclado: {Teclado.__str__(self)}\n      Ratón: {Raton.__str__(self)}]'

if __name__ == '__main__':
    nuevaCompu = Computadora('Asus','Samsung', 17, 'USB-C', 'Thunderobot', 'USB-A', 'HP')
    print(nuevaCompu)