# Herencia
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Vehiculo [Color: {self.color}, Ruedas: {self.ruedas}]'


class Coche(Vehiculo):
    # Se agregan los atributos de la clase heredada mas el de la clase actual
    def __init__(self, color, ruedas, velocidad):
        # Se utiliza siper para inicializar los atributos de la clase padre
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    # Se sobrescribe el metodo __str__ para imprimir el objeto a nuestro gusto
    def __str__(self):
        return f'Coche [Velocidad: {self.velocidad}] {super().__str__()}'


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Bicicleta [Tipo: {self.tipo}] {super().__str__()}'


vehiculo1 = Vehiculo('Rojo', 4)
print(vehiculo1)

coche1 = Coche(vehiculo1.color, vehiculo1.ruedas, 250)
print(coche1)

bicicleta1 = Bicicleta('Verde', 2, 'Montaña')
print(bicicleta1)
