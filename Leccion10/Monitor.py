class Monitor:
    contadorMonitores = 0

    def __init__(self, marca, tamaño):
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores
        self._marca = marca
        self._tamaño = tamaño

    @property
    def idMonitor(self):
        return self._idMonitor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamaño(self):
        return self.tamaño

    @tamaño.setter
    def tamaño(self, tamaño):
        self.tamaño = tamaño

    def __str__(self):
        return f'[ID_Monitor: {self._idMonitor}, Marca: {self._marca}, Tamaño: {self._tamaño}"]'
