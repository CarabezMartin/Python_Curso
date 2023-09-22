from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):

    contador_teclado = 0

    def __init__(self,marca,tipo):
        Teclado.contador_teclado += 1
        self.id_teclado = Teclado.contador_teclado
        super().__init__(marca,tipo)

    def __str__(self):
        return f'Teclado: [Id: {self.id_teclado}, Marca: {self.marca}, Tipo entrada: {self.tipo}]'

