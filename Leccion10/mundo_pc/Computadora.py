from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor
class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Ratón: {self._raton}
        '''


if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('Bluethoot', 'Generico')
    monitor1 = Monitor('Samnsung', 24)
    computadora1 = Computadora('Linux', monitor1, teclado1, raton1)
    print(computadora1)