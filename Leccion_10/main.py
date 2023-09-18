# Creacion de clases y objetos de la clase

class AreaRectangulo:

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return  self.base * self.altura

print("********** AREA DE RECTANGULO **********")
base = int(input("Ingresa la base del rectangulo: "))
altura = int(input("Ingresa la altura del rectangulo: "))

rectangulo = AreaRectangulo(base,altura)
print(f"Area del rectangulo {rectangulo.calcularArea()}")
#FIN AREA DE RECTANGULO

#INICIO DE CALCULO DE VOLUMEN
class VolumenCubo:
    def __init__(self,ancho,profundo,alto):
        self._ancho = ancho
        self._profundo = profundo
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self,ancho):
        self._ancho = ancho

    @property
    def profundo(self):
        return self._profundo

    @profundo.setter
    def profundo(self, profundo):
        self._profundo = profundo

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto
    def calcularVolumen(self):
        return self._ancho * self._profundo * self._alto

print("********** VOLUMEN DE UN CUBO **********")
ancho = int(input("Ingresa el ancho del cubo: "))
prof = int(input("Ingresa la profundidad del cubo: "))
alto = int(input("Ingresa la altura del cubo: "))

cubo = VolumenCubo(ancho,prof,alto)
print(f"Volumen del cubo: {cubo.calcularVolumen()}")
