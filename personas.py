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
        txt="{0} {1}, {2}"
        # retorna text en el formato run, nombre, app y lo que quiera agregar
        return txt.format(self.run, self.nombre, self.app)
