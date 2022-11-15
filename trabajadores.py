from personas import Personas
class Trabajador(Personas):

    def __init__(self, run, nombre, app, turno, inicio_actividades):

        super.__init__(run, nombre, app)
        self.turno = turno
        self.inicio_actividades = inicio_actividades
    
