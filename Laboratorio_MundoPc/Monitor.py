from DispositivoEntrada import DispositivoEntrada


class Monitor:

    contado_monitor = 0

    def __init__(self,marca,tam):
        Monitor.contado_monitor += 1
        self.id_monitor = Monitor.contado_monitor
        self.marca = marca
        self.tam = tam

        @property
        def marca(self):
           return self.marca

        @marca.setter
        def marca(self, marca):
           self.marca = marca

        @property
        def tam(self):
            return self.tam

        @tam.setter
        def tam(self, tam):
            self.tam = tam

    def __str__(self):
        return f'Monitor [Id: {self.id_monitor}, Marca: {self.marca}, Tamaño: {self.tam}]'



# monitor = Monitor('Asus','22')
# print(monitor)
