from DispositivoEntrada import DispositivoEntrada
class Raton(DispositivoEntrada):
    contadorRatones = 0

    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        Raton.contadorRatones += 1
        self._idRaton = Raton.contadorRatones

    def __str__(self):
        return f'[ID_Raton: {self._idRaton}, {super().__str__()}]'
