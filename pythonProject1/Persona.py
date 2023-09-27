class Persona:

    def __init__(self,id_persona,nombre,apellido):
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