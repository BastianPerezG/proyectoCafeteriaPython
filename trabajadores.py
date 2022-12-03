from personas import Personas
from conector import DataBase

class Trabajador(Personas):

    def __init__(self, run, inicio_turno,termino_turno,fcontr,contrato,perf_cod):

        super.__init__(run)
        self.inicio_turno = inicio_turno
        self.termino_turno = termino_turno
        self.fcontr = fcontr
        self.contrato = contrato
        self.perf_cod = perf_cod
        self.run = run 

    def insert_tra(self):
        sql = f"INSERT INTO trabajadores (tra_inicio_turno,tra_termino_turno, tra_fcontr, per_run, perf_cod) VALUE ({self.inicio_turno}, {self.termino_turno}, {self.fcontr},{self.run},{self.perf_cod});"
        db = DataBase()
        db.insert(sql)
    
    def mostrar_tra(self):
        tabla = 'trabajadores' 
        db = DataBase()
        db.select(self, tabla)

    def mostrar_tra_uq(self, id):
        tabla = 'trabajadores'
        columna = 'tra_cod' 
        db = DataBase()
        db.select(self, tabla, id)
    
    def actualizar_tra(self):
        pass

    def eliminar_tra(cod):
        sql = 'DELETE FROM trabajadores WHERE tra_cod = {cod};'
        db = DataBase()
        db.delete(sql)