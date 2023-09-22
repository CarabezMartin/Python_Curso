
class Producto:

    codigo_producto = 0

    def __init__(self,desc,precio):
        Producto.codigo_producto += 1
        self.id = Producto.codigo_producto
        self.desc = desc
        self.precio = precio

    def __str__(self):
        return f'Producto [ID: {self.id}, Descripcion: {self.desc}, Precio $: {self.precio}]'