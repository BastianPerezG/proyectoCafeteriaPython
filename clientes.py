# decidimos separar las clases por archivo
# por eso usamos este metodo para importar lo que esta en personas.py
from personas import Personas
# nuestra clase Clientes heredando () lo que venga de Personas
class Clientes(Personas):
    # esta funcion agrega o redefine el constructor agregando
    # "puntos" como nuevo parametro    
    def __init__(self, run, nombre, app, puntos):
        # super().__init__(toma en consideracion estos parametros originales)
        # del constructor en personas
        super().__init__(self, run, nombre, app)
        # define el self para puntos en este caso quedo igual
        self.puntos = puntos
      
# de que otras formas vamos agregando esta informacion? inputs? como definir cuando es entero y no string???
clienteA = Clientes("run: 22.222.222-2", "Gabriel", "Manzano Valdivia", "puntos acumulados: 3500")
print(clienteA.ver_persona())
# recordar que este puntos que estamos llamando, es el que defini en el ultimo self.
print(clienteA.puntos)

# otras preguntas: para agregar parametros se hace 1 def para cada parametro adicional? como funciona eso?
        
