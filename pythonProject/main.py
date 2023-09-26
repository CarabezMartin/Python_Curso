# Test laboratorio
from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas

opcion = None
catalogo = CatalogoPeliculas()

while opcion != 4:
    print('Opciones'.center(50,'*'))
    print('1) Agregar pelicula')
    print('2) Listar peliculas')
    print('3) Eliminar archivo de peliculas')
    print('4) Salir')
    opcion = int(input('Eliga una opcion del menu: '))

    if opcion == 1:
        titulo = input('Ingrese el titulo de la pelicula: ')
        pelicula = Pelicula(titulo)
        catalogo.agregarPelicula(pelicula)
    elif opcion == 2:
        catalogo.listarPelicula()
    elif opcion == 3:
        catalogo.eliminarPelicula()
else:
    print('Salimos del programa')
