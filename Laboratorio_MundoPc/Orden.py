from Computadora import Computadora
from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Orden:

    contador_ordenes = 0
    def __init__(self,computadoras):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self.computadoras = computadoras

    def agregarComputadora(self,computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''

        for computadora in self.computadoras:
            computadoras_str += computadora.__str__()

        return f'''
                    Orden[Id Orden: {self.id_orden}]\n
                    Detalle: [{computadoras_str}]
                '''

raton = Raton('Logitec','USB')
teclado = Teclado('Logitec','USB')
monitor = Monitor('LG','22')
compu = Computadora('Gamer',monitor,teclado,raton)


compu1 = [compu]
orden = Orden(compu1)
print(orden)