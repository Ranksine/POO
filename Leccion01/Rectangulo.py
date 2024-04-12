class Rectangulo:
    """
    Clase para calcular el area de un rectangulo
    
    Ejercicio para evaluar lo aprendido con las clases en Python
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

base = float(input('Ingresa la base: '))
altura = float(input('Ingresa la altura: '))
objRectangulo = Rectangulo(base, altura)

print(f'El area de un rectangulo de base {base} y altura {altura} = {objRectangulo.calcularArea()}')