# decidimos separar las clases por archivo
# por eso usamos este metodo para importar lo que esta en personas.py
# from personas import Personas
from conector import DataBase
# nuestra clase Clientes heredando () lo que venga de Personas
class Clientes:
    # esta funcion agrega o redefine el constructor agregando
    # "puntos" como nuevo parametro    
    def __init__(self, cod, puntos, descto, cli_frecuente, run):
    #def __init__(self, run, nombre, app, apm, tel, email, fnac, cod, puntos, descto, cli_frecuente):
        # super().__init__(toma en consideracion estos parametros originales)
        # del constructor en personas
        # super().__init__(self, run, nombre, app, apm, tel, email, fnac)
        # define el self para puntos en este caso quedo igual
        self.cod = cod
        self.puntos = puntos
        self.descto = descto
        self.cli_frecuente = cli_frecuente
        self.run = run

    def insert_cli(self):
        sql = f"INSERT INTO clientes (cli_cod, cli_puntos, cli_descto, cli_frecuente) VALUE ({self.cod}, {self.puntos}, {self.descto}, {self.cli_frecuente});"
        db = DataBase()
        db.insert(sql)

    def mostrar_cli(self):
        tabla = 'clientes' 
        db = DataBase()
        db.select(tabla)

    def mostrar_cli_uq(id):
        tabla = 'clientes'
        columna = 'cli_cod' 
        db = DataBase()
        db.select(tabla,columna, id)

    def actualizar_cli(self):
        pass

    def eliminar_cli(cod):
        sql = 'DELETE FROM clientes WHERE cli_cod = {cod};'
        db = DataBase()
        db.delete(sql)
    
