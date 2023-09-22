
class Orden:

    contador_orden = 0

    def __init__(self,productos):
        Orden.contador_orden += 1
        self.id = Orden.contador_orden
        self.productos = list(productos)

    def __str__(self):
        producto_str = ''
        for producto in self.productos:
            producto_str += producto.__str__() + '|'
        return f'Orden:{self.id},\nProductos: {producto_str}'

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total