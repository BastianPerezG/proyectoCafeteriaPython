from personas import Personas
from clientes import Clientes
import os
def limpiarpantalla():
    os.system('cls')
class Menu:
    def __init__():

        print('''
        ========Menú Principal========
        1.- Ingresar un dato
        2.- Mostrar un dato
        3.- Actualizar un dato
        4.- Eliminar un dato
        ''')
        opcion = int(input("Ingrese una opción: \n"))
        if  opcion == 1:
            
            print('''
            =========Que desea ingresar?===========
            1.- Un cliente?
            2.- Un trabajador?
            3.- Un usuario?
            4.- Un producto?
            0.- Volver al menu principal?
            ''')
            opcion1 = int(input("Ingrese una opcion"))
        elif opcion == 2:

            print('''
            ========Que tipo de datos desea mostrar?======
            1.- De trabajadores?
            2.- De clientes?
            3.- De usuarios?
            4.- De productos?
            0.- Volver al menu principal?
            ''')
        elif opcion == 3:

            print('''
            =========Que tipo de dato desea actualizar?========
            1.- De trabajadores?
            2.- De clientes?
            3.- De usuarios?
            4.- De productos?
            0.- Volver al menu principal?
            ''')
        elif opcion == 4:

            print('''
            ===========Que tipo de dato quiere eliminar?=========
            1.- Un cliente?
            2.- Un trabajador?
            3.- Un usuario?
            4.- Un producto?
            0.- Volver al menu principal?            
            ''')
Menu.__init__()   
