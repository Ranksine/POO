from FiguraGeometrica import FiguraGeometrica
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

# No se puede instanciar una clase abstracta
# figura = FiguraGeometrica()

print ('Creacion Objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado = 50, color = 'Rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(f'Calculo del area de un cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

# MRO - Method Resolution Order
# Metodo para conocer el orden de llamada de las clases heredadas
print(Cuadrado.mro())

print('Creacion Objeto rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(ancho = 3, alto = 40, color = 'Moradini')
print(rectangulo1.ancho)
print(rectangulo1.alto)
print(rectangulo1.color)
print(f'Calculo del area de un rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)
