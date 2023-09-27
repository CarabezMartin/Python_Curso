# Conexion a base de datos

import pyodbc

#Datos del servidor y base de datos a conectarnos
server = 'IBC1-HCAMACHO'
bd = 'Test'
user = 'sa'
password = 'AllisonAngela@94'

try:
    #Generacion de la conexion
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};SERVER='+server+';DATABASE='+bd+';UID='+user+';PWD='+password)

    with conexion.cursor() as cursor:
        #Ejecicion de consulta
        id_user = input('Ingrese el Id de la persona: ')
        query_users = "SELECT * FROM Personas WHERE id= ?" #% id_user
        cursor.execute(query_users,(id_user,))

        #Guardamos todos los resultados en la variable res
        res = cursor.fetchall()

        for usuario in res:
            print(usuario)

        #INSERT a la base de datos
        print('Insert a la base de datos'.center(50,'*'))
        nombre = input('Ingrese el nombre: ')
        apellido = input('Ingrese el apellido: ')
        insert = 'INSERT INTO Personas(nombre,apellido) VALUES (?,?)'
        cursor.execute(insert,(nombre,apellido))
        print('Insert ejecutado con exito.\n')

        #UPDATE a la base de datos
        update = 'UPDATE Personas SET apellido = ? WHERE id = ?'
        cursor.execute(update,('Barrera','4'))
        print('Update ejecutado con exito.\n')

except:
    print('Conexion Fallida')
finally:
    print('Conexion cerrada')
    conexion.close()