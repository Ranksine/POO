from Computadora import Computadora
class Orden(Computadora):
    contadorOrdenes = 0

    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._computadoras = list(computadoras)

    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__() + '\n'

        return f'Orden: {self._idOrden}, \nComputadoras: \n{computadoras_str}'


compu1 = Computadora('Asus','Samsung', 17, 'USB-C', 'Thunderobot', 'USB-A', 'HP')
compu2 = Computadora('HP', 'HP', 24, 'USB-C', 'HP', 'USB-A', 'HP')
compu3 = Computadora('Lenovo', 'Lenovo', 32, 'USB-C', 'Razr', 'USB-A', 'Razr')
compu4 = Computadora('Alienware', 'Alienware', 14, 'USB-A', 'hp', 'USB-C', 'Corsair')

orden1 = Orden([compu1, compu2])
orden2 = Orden([compu3, compu4])

print('Orden 1'.center(50,'-'))
print(orden1)
print('Orden 2'.center(50,'-'))
print(orden2)