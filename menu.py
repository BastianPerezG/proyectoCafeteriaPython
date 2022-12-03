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
        5.- Ingresar al menu ventas
        ''')
        opcion = int(input("Ingrese una opción: \n"))
        limpiarpantalla()
        if  opcion == 1:    # Ingresar algo         
            print('''
            =========Que desea ingresar?===========
            1.- Un cliente?
            2.- Un trabajador?
            3.- Un usuario?
            4.- Un producto?
            0.- Otro numero para volver al menu principal
            ''')
            opcion1 = int(input("Ingrese una opcion: \n"))# Ingresar Clientes
            limpiarpantalla()
            if opcion1 == 1:
                print("Un Cliente")
            elif opcion1 == 2:
                print("Un trabajador")
            elif opcion1 == 3:
                print("Un usuario")
            elif opcion1 == 4:
                print("Un producto")
            else:
                Menu.__init__()              

        elif opcion == 2:
            print('''
            ========Que tipo de datos desea mostrar?======
            1.- De clientes?
            2.- De trabajadores?
            3.- De usuarios?
            4.- De productos?
            0.- Otro numero para volver al menu principal
            ''')
            opcion2 = int(input("Ingrese una opcion: \n"))# Mostrar
            limpiarpantalla()
            if opcion2 == 1: # Mostrar un cliente
                print('''
                =====Especifique====
                1.- Un cliente en especifico?
                2.- Todos los clientes registrados?
                0.- Otro numero para salir al menu principal
                ''')
                opCli = int(input("Especifique!\n")) # Mostrar
                limpiarpantalla()
                if opCli == 1:
                    print("Mostraremos un cliente especifico")
                elif opCli == 2:
                    print("Mostraremos a todos los hdp")
                else:
                    Menu.__init__()
            elif opcion2 == 2: # Mostrar un trabalhador
                print('''
                =====Especifique====
                1.- Un trabajador en especifico?
                2.- Todos los trabajadores registrados?
                0.- Otro numero para salir al menu principal
                ''')
                opTrab = int(input("Especifique: \n")) # Mostrar trabalhador
                if opTrab == 1:
                    print("Mostraremos un trabajador en especifico")
                elif opTrab == 2:
                    print("Mostraremos a todos los hdp workers")
            elif opcion2 == 3: # Mostrar productos
                print('''
                =====Especifique====
                1.- Un producto en especifico?
                2.- Todos los productos registrados?
                0.- Otro numero para salir al menu principal
                ''')
                opProd = int(input("Especifique: \n"))
                if opProd == 1:
                    pass
                elif opProd == 2:
                    pass
            elif opcion2 == 4:
                pass
            else:
                Menu.__init__()

        elif opcion == 3:

            print('''
            =========Que tipo de dato desea actualizar?========
            1.- De trabajadores?
            2.- De clientes?
            3.- De usuarios?
            4.- De productos?
            0.- Volver al menu principal?
            ''')
            opcion3 = int(input("Ingrese una opcion: \n"))
            limpiarpantalla()
            if opcion3 == 1:
                pass
            elif opcion3 == 2:
                pass
            elif opcion3 == 3:
                pass
            elif opcion3 == 4:
                pass
            else:
                Menu.__init__()

        elif opcion == 4:

            print('''
            ===========Que tipo de dato quiere eliminar?=========
            1.- Un cliente?
            2.- Un trabajador?
            3.- Un usuario?
            4.- Un producto?
            0.- Volver al menu principal?            
            ''')
            opcion4 = int(input("Ingrese una opcion: \n"))
            limpiarpantalla()
            if opcion4 == 1:
                pass
            elif opcion4 == 2:
                pass
            elif opcion4 == 3:
                pass
            elif opcion4 == 4:
                pass
            else:
                Menu.__init__()
Menu.__init__()   
