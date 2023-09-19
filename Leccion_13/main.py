# Herencia Multiple

from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica,Color):

    def __init__(self,lado,color):
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)

    def CalcularArea(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

class Rectangulo(FiguraGeometrica,Color):

    def __init__(self,alto,ancho,color):
        FiguraGeometrica.__init__(self,alto,ancho)
        Color.__init__(self,color)

    def Calcular_Area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

cuadrado = Cuadrado(5,'Verde')
print(cuadrado)
print(cuadrado.CalcularArea())

rectangulo = Rectangulo(5,7,'Violeta')
print(rectangulo)
print(rectangulo.Calcular_Area())
