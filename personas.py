class Personas:
    def __init__(self, run, nombre, app):

        self.run = run
        self.nombre = nombre
        self.app = app

    def ver_persona(self):
        txt="{0} {1}, {2}"
        return txt.format(self.run, self.nombre, self.app)
