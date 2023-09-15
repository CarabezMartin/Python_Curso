# Funciones y Funciones recursivas
def sum_valores(*args) -> float:
    sum = 0
    for num in args:
        sum += num
    return sum

print(f'Resultado de funcion: {sum_valores(1.5,2,3,4,5,6)}')

print("\n********** Funcion Recursiva **********")

def recursivo(num):
    if num == 1:
        print(num)
    else:
        recursivo(num-1)
        print(num)

recursivo(5)

print("\n********** Calculadora de impuestos **********")

def calcularImpuesto(pago,impuesto):
    return pago + pago * (impuesto/100)

pago = int(input("Proporcione el pago sin impuesto: "))
impuesto = int(input("Proporcione el monto del impuesto: "))
print(f"Pago con el impuesto: {calcularImpuesto(pago,impuesto)}")
