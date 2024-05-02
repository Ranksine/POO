from DispositivoEntrada import DispositivoEntrada
class Teclado(DispositivoEntrada):
    contadorTeclados = 0

    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        Teclado.contadorTeclados += 1
        self._idTeclado = Teclado.contadorTeclados

    def __str__(self):
        return f'[ID_Teclado : {self._idTeclado}, {super().__str__()}]'
