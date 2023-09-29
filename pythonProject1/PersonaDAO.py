from Conexion import Conexion
from Persona import Persona


class PersonaDAO:
    '''
    DAO (Data Access Object)
    '''
    _SELECT = 'SELECT * FROM Personas'
    _INSERT = 'INSERT INTO Personas(nombre,apellido) VALUES (?,?)'
    _UPDATE = 'UPDATE Personas SET nombre = ?, apellido = ? WHERE id = ?'
    _DELETE = 'DELETE FROM Personas WHERE id = ?'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            personas = []

            for registro in registros:
                persona = Persona(registro[0],registro[1],registro[2])
                personas.append(persona)
            return personas

    @classmethod
    def insetar(cls,persona):
        with Conexion.obtenerCursor() as cursor:
            print(f'Persona a insertar: {persona}')
            valores = (persona.nombre,persona.apellido)
            cursor.execute(cls._INSERT,valores)


if __name__ == '__main__':
    personas = PersonaDAO.seleccionar()

    for persona in personas:
        print(persona)

    PersonaDAO.insetar()

    personas = PersonaDAO.seleccionar()

    for persona in personas:
        print(persona)