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

print("\n********** Palindromo **********")

der = 0
pal = input("Ingrese una palabra")
izq = len(pal)
bandera = False

for let in pal:
    bandera = False
    if pal[der] != pal[izq-1]:
        print(f"La palabra {pal} no es palindromo")
        break
    elif der != izq and pal[der] == pal[izq-1]:
        der += 1
        izq -= 1
        bandera = True

if bandera == True:
    print("Es palindromo")



