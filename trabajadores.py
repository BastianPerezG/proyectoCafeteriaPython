from personas import Personas
from conector import DataBase
class Trabajador(Personas):

    def __init__(self, run, nombre, app, apm, tel, email, fnac, turno, inicio_actividades):

        super.__init__(run, nombre, app, apm, tel, email, fnac)
        self.turno = turno
        self.inicio_actividades = inicio_actividades

    def insert_trab(self):
        sql = f"INSERT INTO cafeteria.trabajadores ( tra_cod, tra_inicio_turno,tra_termino_turno, tra_fcontr, per_run, perf_cod) VALUE ({self.turno}, {self.inicio_actividades})"
        db = DataBase()
        db.insert(sql)
    
