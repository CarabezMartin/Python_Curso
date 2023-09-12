# Etapas de vida

edad = int(input("Ingresa tu edad: "))

if edad <= 10:
    print("0-10: La infancia es increible")
elif edad >= 10 and edad <= 20:
    print("10-20: Muchos cambios y mucho estudio")
elif edad >= 20 and edad <= 30:
    print("20-30: Amor y comienza el trabajo")
else:
    print("Etapa de vida no reconocida")
