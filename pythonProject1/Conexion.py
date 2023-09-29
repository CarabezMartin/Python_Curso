from logger_base import log
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
                cls._conexion = bd.connect(
                    'DRIVER={ODBC Driver 17 for SQL server};SERVER=' + cls._SERVER + ';DATABASE=' + cls._DATABASE + ';UID=' + cls._USER + ';PWD=' + cls._PASSWORD)
                log.debug('Conexion exitosa')
                return cls._conexion
            except Exception as e:
                log.debug(f'Ocurrio una excepcion al obtener la conexion {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrio correctamente el cursor')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener el cursor {e}')
                sys.exit()
        else:
            return cls._cursor

if __name__ == '__main__':
    conexion = Conexion().obtenerConexion()
    cursor = Conexion.obtenerCursor()