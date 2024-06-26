# Un archivo o modulo en python puede contener varias clases
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [Nombre: {self.nombre}, Edad: {self.edad}]'

# Clase hijo de clase padre Persona
class Empleado(Persona):
    def __init__(self,nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado [Sueldo: {self.sueldo}] {super().__str__()} '

