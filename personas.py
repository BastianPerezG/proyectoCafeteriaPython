from conector import DataBase

#La class Personas contiene los elementos run, nombre, etc
class Personas:
    # constructor 
    def __init__(self, run, nombre, app, apm, tel, email, fnac):

        self.run = run
        self.nombre = nombre
        self.app = app
        self.apm = apm
        self.tel = tel
        self.email = email
        self.fnac = fnac
    
    def insertar(self):
        sql = f"INSERT INTO personas (per_run, per_nombre, per_app, per_apm, per_tel, per_email, per_fnac) VALUE ('{self.run}','{self.nombre}', '{self.app}','{self.apm}','{self.tel}','{self.email}',{self.fnac} )"
        db = DataBase()
        db.insert(sql)

