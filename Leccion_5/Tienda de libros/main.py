# Tieda de libros
nombre: str = input("Ingrese el nombre del libro: ")
id: int = int(input("Ingrese el ID del libro: "))
precio: float = float(input("Ingrece el precio $ del libro: "))
envio: bool = bool(input("El envio es gratuito (True/False): "))

print("\n********** INFORMACION DEL LIBRO **********")

print(f"Nombre del libro: {nombre}")
print(f"ID del libro: {id}")
print(f"Precio: ${precio}")
print(f"Envio gratis: {envio}")