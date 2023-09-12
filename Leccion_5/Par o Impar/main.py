# Par o impar
num = int(input("Ingrese un numero: "))
num = num % 2
if num == 0:
    print(f"El numero {num} es numero par")
else:
    print(f"El numero {num} es numero impar")