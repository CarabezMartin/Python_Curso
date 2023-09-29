from logger_base import log
class Persona:

    def __init__(self,id_persona=None,nombre=None,apellido=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido

    def __str__(self):
        return \
            f'''
            Id Persona: {self._id_persona},
            Nombre: {self._nombre}, 
            Apellido: {self._apellido}
            '''

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id):
        self._id_persona = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

if __name__ == '__main__':
    persona1 = Persona(1,'Juan','Esparza')
    log.debug(persona1)