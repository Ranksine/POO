# En un archivo de python se pueden encontrar muchas clases
from Persona import Persona

print('Creación de objetos'.center(30,'-'))
persona1 = Persona('Karla', 'Gomez', 33)
persona1.mostrarDetalle()

print('Eliminación de objetos'.center(30,'-'))
del persona1
