from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora:

    contador_computadora = 0

    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadora +=1
        self.id_computadora = Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f'''
                    Computadora: [Id: {self.id_computadora}, Nombre: {self.nombre}]
                    Monitor: [Marca: {self.monitor.marca}, Tamaño: {self.monitor.tam}]
                    Teclado: [Marca: {self.teclado.marca}, Tipo: {self.teclado.tipo}]
                    Raton: [Marca: {self.raton.marca}, Tipo: {self.raton.tipo}]
                '''

# raton = Raton('Logitec','USB')
# teclado = Teclado('Logitec','USB')
# monitor = Monitor('LG','22')
# compu = Computadora('Gamer',monitor,teclado,raton)
# print(compu)