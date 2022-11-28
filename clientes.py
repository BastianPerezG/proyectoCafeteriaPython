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
        self.cli_frecuente = True
        self.run = run

    def insert_cli(self):
        sql = f"INSERT INTO cafeteria.clientes (cli_cod, cli_puntos, cli_descto, cli_frecuente, per_run) VALUE ({self.cod}, {self.puntos}, {self.descto}, {self.cli_frecuente}, {self.run})"
        db = DataBase()
        db.insert(sql)

    
        

      
# de que otras formas vamos agregando esta informacion? inputs? como definir cuando es entero y no string???
#clienteA = Clientes("22.222.222-2", "Gabriel", "Manzano", 3500)
#print(clienteA.ver_persona())
# recordar que este puntos que estamos llamando, es el que defini en el ultimo self.
#print(clienteA.puntos)

# otras preguntas: para agregar parametros se hace 1 def para cada parametro adicional? como funciona eso?
