
class Usuario:

    def __init__(self,id_user=None,nombre=None,apellido=None):
        self._id_user = id_user
        self._nombre = nombre
        self._apellido = apellido

    def __str__(self):
        return \
            f'''
            Id Persona: {self._id_user},
            Nombre: {self._nombre}, 
            Apellido: {self._apellido}
            '''

    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, id):
        self._id_user = id

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
    usuario = Usuario(1,'Juan','Esparza')
    print(usuario)