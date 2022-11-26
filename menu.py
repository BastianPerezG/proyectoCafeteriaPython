# importando de personas
from personas import Personas
import os
# funcion para limpiar pantalla ya incorporada en python
def limpiarpantalla():
    os.system('cls')
# clase menu 
class Menu:
    # constructor __init__
    def __init__():
        # menu de opciones (Menu principal de personas)
        print('''           
        ===== MENU DE OPCIONES ===== 

        1.- Para Ingresar a Menú Personas
        2.- Para Ingresar a Menú Clientes
        3.- Para Ingresar a Menú Trabajadores
        4.- Para Ingresar a Menú Productos
        5.- Para Ingresar a Menú Usuarios
        6.- Otros (Un ver historico de boletas y un ver de historico de ventas)
        0.- Salir
            ''')
        # luego de que el usuario ingrese una opcion llamamos la funcion limpiarpantalla()
        opcion = int(input("Ingrese la opción \n"))
        limpiarpantalla()
        if opcion == 1:
            # Ingresando al submenu personas
            print('''
            ===== Menu personas =====
            1.- Ingresar una Persona
            2.- Listar Personas
            3.- Actualizar datos de una persona
            4.- Eliminar persona
            0.- Volver a menú principal
            ''')
            # primera opcion para ingresar una persona y limpiar pantalla
            opcion1 = int(input("Ingrese una opción"))
            limpiarpantalla()
            if opcion1 == 1:
                # presione cualquier tecla solo para dar una pausa
                input("Presione cualquier tecla")
                # cargamos cada uno de los atributos en estas variables
                run = input("Ingrese el rut")
                nombre = input("Ingrese el nombre")
                app = input("Ingrese el apellido paterno")
                apm = input("Ingrese el apellido materno")
                tel = input("Ingrese el numero de telefono")
                email = input("Ingrese el email de la persona")
                fnac = input("Ingrese la fecha de nacimiento de la persona (En formato YYYY-MM-DD)")
                # una nueva variable para definir una instancia
                persona = Personas(run, nombre, app, apm, tel, email, fnac)
                # Una vez ingresados estos datos aplicamos el metodo "insertar"
                # que ya esta definido en el archivo personas.py
                persona.insertar()
            elif opcion1 == 2:
                print("Listando personas")
                
            elif opcion1 == 3:
                print("Actualizando datos")
            elif opcion1 == 4:
                print("Eliminando persona")
        else:

            print("No se reconoce la opción, vuelva a intentar")
            Menu.__init__()

        if opcion == 2:

            print('''
            ===== Menu clientes ======
            1.- Ingresar un cliente
            2.- Listar clientes
            3.- Actualizar datos de un cliente
            4.- Eliminar un cliente
            0.- Volver a menú principal
            ''')
            opcion2 = int(input("Ingrese una opción"))

            if opcion2 == 1:
                print("Ingresando cliente")
            if opcion2 == 2:
                print("Listando clientes")
            if opcion2 == 3:
                print("ACtualizando datos de cliente")
            if opcion2 == 4:
                print("Eliminando un cliente")
            else:
                print("")
Menu.__init__()