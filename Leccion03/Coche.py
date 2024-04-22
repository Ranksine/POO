from Vehiculo import Vehiculo
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad= velocidad

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    def __str__(self):
        return f'Coche [Velocidad {self._velocidad}(km/h)] {super().__str__()}'


coche = Coche('Negro', 4, 250)
print(coche)
