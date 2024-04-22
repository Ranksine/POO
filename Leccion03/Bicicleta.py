from Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def __str__(self):
        return f'Bicicleta[Tipo: {self._tipo}] {super().__str__()}'


bici = Bicicleta('rojo', 2, 'Montaña')
print(bici)