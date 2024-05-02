from mundo_pc.Teclado import Teclado
from mundo_pc.Raton import Raton
from mundo_pc.Monitor import Monitor
from mundo_pc.Computadora import Computadora
from mundo_pc.Orden import Orden

teclado1 = Teclado('HP', 'USB-C')
raton1 = Raton('Thunderobot', 'Bluethooth')
monitor1 = Monitor('HP', 15)
computadora1 = Computadora('Linux', monitor1, teclado1, raton1)

teclado2 = Teclado('Machenike', 'Bluethoot')
raton2 = Raton('GenericoA', 'USB-C')
monitor2 = Monitor('Xiaomi', 24)
computadora2 = Computadora('Mac3', monitor2, teclado2, raton2)

teclado3 = Teclado('Corsair', 'USB-C')
raton3 = Raton('Razr', 'USB-A')
monitor3 = Monitor('Samnsung', 32)
computadora3 = Computadora('Windows', monitor3, teclado3, raton3)

computadoras1 = [computadora1, computadora2]
computadoras2 = [computadora3]
orden1 = Orden(computadoras1)
print(orden1)
orden2 = Orden(computadoras2)
print(orden2)