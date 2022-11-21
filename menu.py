
class Menu:

    def __init__():

        print('''           
        ===== MENU DE OPCIONES ===== 

        1.- Para Ingresar a Menú Personas
        2.- Para Ingresar a Menú Clientes
        3.- Para Ingresar a Menú Trabajdores
        4.- Para Ingresar a Menú Productos
        5.- Para Ingresar a Menú Usuarios
        0.- Salir
            ''')

        opcion = int(input("Ingrese la opción \n"))

        if opcion == 1:

            print('''
            ===== Seleccione una opción =====
            1.- Ingresar una Persona
            2.- Listar Personas
            3.- Actualizar datos de una persona
            4.- Eliminar persona
            0.- Volver a menú principal''')

            opcion1 = int(input("Ingrese una opción"))

            if opcion1 == 1:
                print("Ingresando Personas")
            elif opcion1 == 2:
                print("Ingresando Personas")
            elif opcion1 == 3:
                print("Ingresando Personas")
            elif opcion1 == 4:
                print("Ingresando Personas")
        else:

            print("No se reconoce la opción, vuelva a intentar")
            Menu.__init__()
Menu.__init__()