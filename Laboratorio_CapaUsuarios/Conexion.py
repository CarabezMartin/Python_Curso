import pyodbc as bd
import sys

class Conexion:

    _SERVER = 'IBC1-HCAMACHO'
    _DATABASE = 'Test'
    _USER = 'sa'
    _PASSWORD = 'AllisonAngela@94'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};Server='+cls._SERVER+';DATABASE='+cls._DATABASE+';UID='+cls._USER+';PWD='+cls._PASSWORD)
                print('Conexion Exitosa')
                return cls._conexion
            except Exception as e:
                print('Ocurrio un error al generar la conexion')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                print('Cursor Exitoso')
                return cls._cursor
            except Exception as e:
                print('Ocurrio un error al obtener el cursor')
                sys.exit()
        else:
            return cls._cursor

if __name__ == '__main__':
    Conexion.obtenerCursor()