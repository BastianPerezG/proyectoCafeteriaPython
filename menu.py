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
            # Ingresando al submenu PERSONAS
            print('''
            ===== Menu personas =====
            1.- Nueva Persona
            2.- Mostrar Personas registradas
            3.- Actualizar datos de una persona
            4.- Eliminar registro de una persona
            0.- Volver a menú principal
            ''')
            # primera opcion para ingresar una persona y limpiar pantalla
            opcion1 = int(input("Ingrese una opción"))
            limpiarpantalla()
            if opcion1 == 1:
                # cargamos cada uno de los atributos en estas variables
                run = input("Ingrese el rut")
                nombre = input("Ingrese el nombre")
                app = input("Ingrese el apellido paterno")
                apm = input("Ingrese el apellido materno")
                tel = input("Ingrese el numero de telefono")
                email = input("Ingrese el email de la persona")
                fnac = input("Ingrese la fecha de nacimiento de la persona (En formato YYYY-MM-DD)")
                # con esta variable definimos lo que enviaremos en insertar() hacia la clase Personas
                persona = Personas(run, nombre, app, apm, tel, email, fnac)
                # Una vez ingresados estos datos aplicamos el metodo "insertar()"
                # que ya esta definido en el archivo personas.py como un metodo para insertar datos
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

        elif opcion == 2:
            # mostramos el submenu CLIENTES
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

                run = input("Ingrese el rut")
                nombre = input("Ingrese el nombre")
                app = input("Ingrese el apellido paterno")
                apm = input("Ingrese el apellido materno")
                tel = input("Ingrese el numero de telefono")
                email = input("Ingrese el email de la persona")
                fnac = input("Ingrese la fecha de nacimiento de la persona (En formato YYYY-MM-DD)")
                # con esta variable definimos lo que enviaremos en insertar() hacia la clase Personas
                persona = Personas(run, nombre, app, apm, tel, email, fnac)
                # Una vez ingresados estos datos aplicamos el metodo "insertar()"
                # que ya esta definido en el archivo personas.py como un metodo para insertar datos
                persona.insertar()
            if opcion2 == 2:
                print("Listando clientes")
            if opcion2 == 3:
                print("ACtualizando datos de cliente")
            if opcion2 == 4:
                print("Eliminando un cliente")
            else:
                print("cingresaste cero o una letra o algo asi")
        elif opcion == 3:
            print('''
            1.- Nuevo trabajador
            2.- Mostrar los trabajadores
            3.- Actualizar datos de un trabajador
            4.- Eliminar un trabajador de la lista
            5.- Definir turno del trabajador
            0.- salir
            ''')

            opcion3 = int(input("Ingrese una opción: \n"))

            if opcion3 == 1:
                print("Ingresando un trabajador")
            elif opcion3 == 2:
                print("Listando trabajadores")            
            elif opcion3 == 3:
                print("Actualizar datos de un trabajador")
            elif opcion3 == 4:
                print("ELiminar!")
            elif opcion3 == 5:
                print("Definir turno; A, B, C")
            else:
                print("Ingresaste otra cosa")
        elif opcion == 4:
            print('''
            1.- Ingresar un nuevo producto
            2.- Mostrar los productos disponibles
            3.- Actualizar datos de un producto
            4.- Eliminar un producto
            0.- Salir de este menu            
            ''')
            opcion4 = int(input("Ingrese una opción: \n"))
            if opcion4 == 1:
                print("Nuevo producto")
            elif opcion4 == 2:
                print("Mostrar productos disponibles")
            elif opcion4 == 3:
                print("ACtualizando datos de producto")
            elif opcion4 == 4:
                print("Eliminar producto")
            else:
                print("Aqui va algo")
        elif opcion == 5:
            print('''
            1.- Registrarse
            2.- Mostrar usuarios
            3.- ACtualizar mis datos
            4.- Eliminar un usuario
            0.- Salir de este submenu
            ''')

        

Menu.__init__()