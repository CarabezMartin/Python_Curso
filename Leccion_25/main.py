# Conexion a base de datos

import pyodbc

server = 'IBC1-HCAMACHO'
bd = 'IIDEATops'
user = 'sa'
password = 'AllisonAngela@94'

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};SERVER='+server+';DATABASE='+bd+';UID='+user+';PWD='+password)
    print('Conexion exitosa')

    query_users= 'SELECT TOP(10) * FROM Users'

    with conexion.cursor() as cursor:
        cursor.execute(query_users)

        res = cursor.fetchall()

        for usuario in res:
            print(usuario)

except:
    print('Conexion Fallida')