class Cubo:
    """
    Clase para obtener el volumén de un cubo
    Ejercicio Laboratorio para evaluar lo aprendido sobre clases en Python
    """
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcularVolumen(self):
        return self.ancho * self.alto * self.profundidad


ancho = float(input('Ingresa el ancho: '))
alto = float(input('Ingresa el alto: '))
prof = float(input('Ingresa la profundidad: '))
objCubo = Cubo(ancho,alto,prof)
print(f'El volumén del cubo es: {objCubo.calcularVolumen()}')