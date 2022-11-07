from personas import Personas

class Clientes(Personas):
    
    def __init__(self, run, nombre, app, puntos):
        super().__init__(self, run, nombre, app)
        self.puntos = puntos
      

clienteA = Clientes("run: 22.222.222-2", "Gabriel", "Manzano Valdivia", "puntos acumulados: 3500")
print(clienteA.ver_persona())
print(clienteA.puntos)
        
