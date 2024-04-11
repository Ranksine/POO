class Persona:
    """
    En python no se utiliza el constructor ya que python utiliza los constructores de forma oculta
    por lo tanto para inicializar la clase se utiliza '__init__()'
     # __ = doble underscore o  donder (metodo tipo donder), .: "donder init"
     # __str__() = metodo tipo donder str
    """
    def __init__(self):
        # Atributos de instancia (para objetos)
        self.nombre = 'Juan'
        self.apellido = 'Perez'
        self.edad = 28


persona1 = Persona()
print(f'Nombre: {persona1.nombre}')
print(f'Apellido: {persona1.apellido}')
print(f'Edad: {persona1.edad}')