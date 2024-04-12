class Persona:
    """
    En python no se utiliza el constructor ya que python utiliza los constructores de forma oculta
    por lo tanto para inicializar la clase se utiliza '__init__()'
     # __ = doble underscore o  donder (metodo tipo donder), .: "donder init"
     # __str__() = metodo tipo donder str
    """
    def __init__(self,nombre, apellido, edad, *tuplas, **terminos): # self hace la funcion de "this" en otros lenguajes
        # Atributos de instancia (para objetos)
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.tuplas = tuplas
        self.terminos = terminos

    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido}, {self.edad}')
        print(f'Tuplas: {self.tuplas}, Terminos: {self.terminos}')

    # def mostrarDetalle(this):
    #     print(f'Persona: {this.nombre} {this.apellido}, {this.edad}')


persona1 = Persona('Juan', ' Perez', 24, '456212321', 2,3,5,4, m = 'manzana', p = 'pera')
# print(f'Nombre: {persona1.nombre}')
# print(f'Apellido: {persona1.apellido}')
# print(f'Edad: {persona1.edad} \n')
persona1.mostrarDetalle()
# Se pueden agregar parametros especiales para cada objeto de forma dinamica en python
persona1.telefono = '346548977'
print(persona1.telefono, '\n')
# Tambien se puede acceder al metodo directamente desde una llamada a la clase
# mandando un objeto como parametro que sustituye a 'self'
# Persona.mostrarDetalle(persona1)

# persona1.nombre = 'Omars'
# persona1.apellido = 'Aguilars'
# persona1.edad = 25
# print(f'Objeto 1 modificado: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Karla', 'Gomez', 30)
# print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
persona2.mostrarDetalle()
# print(persona2.telefono)