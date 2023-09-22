# Diseño de clases

from Productos import *
from Ordenes import *

prod1 = Producto('Camisa',150)
prod2 = Producto('Pantalon',1500)

orden1 = Orden([prod1,prod2])
print(orden1)
print(orden1.calcular_total())

orden2 = Orden([prod1,prod2,prod1])
print(orden2)
print(orden2.calcular_total())
