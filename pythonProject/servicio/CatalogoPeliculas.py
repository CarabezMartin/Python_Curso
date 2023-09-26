import os

class CatalogoPeliculas:

    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregarPelicula(cls,pelicula):
        with open(cls.ruta_archivo,'a',encoding='utf8') as archivo:
            archivo.write(f'{pelicula}\n')

    @classmethod
    def listarPelicula(cls):
        with open(cls.ruta_archivo,'r',encoding='utf8') as archivo:
            print('Catalogo Peliculas'.center(50,'*'))
            print(archivo.read())
    @classmethod
    def eliminarPelicula(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')