from conector import DataBase
from getpass import getpass
#La class Personas contiene los elementos run, nombre, etc
class Personas:
    # constructor 
    def __init__(self, run, nombre, app):

        self.run = run
        self.nombre = nombre
        self.app = app
    # metodo para leer las instancias persona
    def ver_persona(self):
        # define lo que se pretende retornar
        txt="{0}, {1}, {2}"
        # retorna text en el formato run, nombre, app y lo que quiera agregar
        return txt.format(self.run, self.nombre, self.app)


    def listar_todas_personas(self):
        user = input("Ingrese nombre de usuario de la bd \n")
        password = getpass("Ingrese la password del usuario \n")
        db = DataBase(user,password)
        db.conectar

person = Personas("11.111.111-1", "Juan", "Pérez")
person.listar_todas_personas()
