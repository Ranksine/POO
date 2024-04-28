class MiClase():
    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodoEstatico(): 
        print(f'Hola desde metodo estatico: {MiClase.variable_clase}')


MiClase.metodoEstatico()

# print(MiClase.variable_clase)
# miClase = MiClase('Valor variable instancia')
# print(miClase.variable_instancia)
# print(miClase.variable_clase)
#
# # Variables de clase al vuelo = variables que podemos crear para ser usadas por todos los objetos de la clase
# # despues de inicializar la clase.
# MiClase.variable_clase2 = 'Valor variable clase 2'
#
# miClase2 = MiClase('Otro valor de variable de instancia')
# print(miClase2.variable_instancia)
# print(miClase2.variable_clase)
# print(MiClase.variable_clase2)
# print(miClase.variable_clase2)
# print(miClase2.variable_clase2)