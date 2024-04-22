"""
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
    las cuales heredan de la clase padre Vehiculo.
    La clase padre debe tener los siguiente atributos y métodos

    Vehiculo (Clase Padre):
    -Atributos (color, ruedas)
    -Métodos (__init__() y __str__())

    Coche (Clase Hija de Vehiculo)(Además de los atributos y métodos heredados de Vehiculo)
    -Atributos (velocidad (km/hr))
    -Métodos (__init__() y __str__())

    Bicicleta (Clase Hija de Vehiculo)(Además de llos atributos y métodos heredados de Vehiculo)
    -Atributos (tipo (urbana/montaña/etc))
    -Métodos (__init__() y __str__())
"""

class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color  # String
        self._ruedas = ruedas  # Int

    @property
    def color(self):
        return self._color

    @property
    def ruedas(self):
        return self._ruedas

    @color.setter
    def color(self, color):
        self._color = color

    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas

    def __str__(self):
        return f'Vehiculo [Color: {self._color}, Ruedas: {self._ruedas}]'