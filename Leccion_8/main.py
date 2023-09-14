# Ciclo For, Listas y Tuplas
rango = range(11)

print("********** Numeros divisibles entre 3 **********")
for num in rango:
    if num % 3 == 0:
        print(num)

print("********** Rango de 2 a 6 **********")
rango = range(2,7)
for num in rango:
    print(num)

print("********** Rango de 3 a 10 con incremento de 2 **********")
rango = range(3,11,2)
for num in rango:
    print(num)

print("********** Tuplas **********")
tupla = (13,1,8,3,2,5,8)
lista = []

for num in tupla:
    if num < 5:
        lista.append(num)
print(lista)