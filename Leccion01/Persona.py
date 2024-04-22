class Persona:
    """
    En python no se utiliza el constructor ya que python utiliza los constructores de forma oculta
    por lo tanto para inicializar la clase se utiliza '__init__()'
     # __ = doble underscore o  donder (metodo tipo donder), .: "donder init"
     # __str__() = metodo tipo donder str
    """
    def __init__(self,nombre, apellido, edad, *tuplas, **terminos): # self hace la funcion de "this" en otros lenguajes
        # Atributos de instancia (para objetos)
        self._nombre = nombre  # La sintaxis para atributos encapsulados se le añade "_" al inicio del nombre del atributo
        self._apellido = apellido
        self._edad = edad
        self.tuplas = tuplas
        self.terminos = terminos

    @property  # Permite acceder al atributo sin acceder directamente a el
    def nombre(self):
        # print('Llamando método get nombre')
        return self._nombre

    # Si se define el método get pero no set, el atributo se convierte en uno de solo lectura,
    # que no puede ser modificado una vez sea inicializado
    @nombre.setter
    def nombre(self, nombre):
        # print('Llamando método set nombre')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrarDetalle(self):
        print(f'Persona: {self._nombre} {self._apellido}, {self._edad}')

    def __del__(self):  # Destructor de objeto
         print(f'Persona eliminada: {self._nombre} {self._apellido}')

    # def mostrarDetalle(this):
    #     print(f'Persona: {this.nombre} {this.apellido}, {this.edad}')
    #     print(f'Tuplas: {self.tuplas}, Terminos: {self.terminos}')

if __name__ == '__main__':
    persona1 = Persona('Juan', ' Perez', 24, '456212321', 2,3,5,4, m = 'manzana', p = 'pera')
    persona1.nombre = 'Jose Luis'
    persona1.apellido = 'Lara'
    persona1.edad = 30
    persona1.mostrarDetalle()

    print('Nombre del modulo:', __name__)
# print(f'Nombre: {persona1.nombre}')
# print(f'Apellido: {persona1.apellido}')
# print(f'Edad: {persona1.edad} \n')
# persona1.mostrarDetalle()
# Se pueden agregar parametros especiales para cada objeto de forma dinamica en python
# persona1.telefono = '346548977'
# print(persona1.telefono, '\n')
# Tambien se puede acceder al metodo directamente desde una llamada a la clase
# mandando un objeto como parametro que sustituye a 'self'
# Persona.mostrarDetalle(persona1)

# persona1.nombre = 'Omars'
# persona1.apellido = 'Aguilars'
# persona1.edad = 25
# print(f'Objeto 1 modificado: {persona1.nombre} {persona1.apellido} {persona1.edad}')

# persona2 = Persona('Karla', 'Gomez', 30)
# print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
# persona2.mostrarDetalle()
# print(persona2.telefono)