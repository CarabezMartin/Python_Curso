from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):

    contador_raton = 0

    def __init__(self,marca,tipo):
        Raton.contador_raton += 1
        self.id_raton = Raton.contador_raton
        super().__init__(marca,tipo)

    def __str__(self):
        return f'Raton [Id: {self.id_raton}, Marca: {self.marca}, Tipo entrada: {self.tipo}]'
