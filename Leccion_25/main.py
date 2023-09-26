# Conexion a base de datos

import pyodbc

server = 'IBC1-HCAMACHO'
bd = 'IIDEATops'
user = 'sa'
password = 'AllisonAngela@94'

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};SERVER='+server+';DATABASE='+bd+';UID='+user+';PWD='+password)
    print('Conexion exitosa')

    query_users= 'SELECT * FROM Users WHERE UserID= %s'

    with conexion.cursor() as cursor:
        id_user = input('Ingrese el Id de la persona: ')
        print(id_user)
        cursor.execute(query_users,(id_user,))

        res = cursor.fetchall()

        for usuario in res:
            print(usuario)

except:
    print('Conexion Fallida')
finally:
    print('Conexion cerrada')
    conexion.close()