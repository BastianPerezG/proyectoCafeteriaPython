from personas import Personas
from clientes import Clientes
from productos import Productos
from trabajadores import Trabajador
from usuario import Usuario

import os
def limpiarpantalla():
    os.system('cls')
        # a partir de esta columna se encuentran las opciones del menu principal
            # los submenu if = opcion1, opcion2, opcion3, etc se encuentran a partir de estacolumna
                # adicionalmente, algunos de estos sumenu tendran otro submenu para elegir
                # por ejemplo: entre un cliente especifico o todos los clientes
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
        if  opcion == 1:# Ingresar algo  ***********************************  **********************************     
            print('''
            =========Que desea ingresar?===========
            1.- Un cliente?
            2.- Un trabajador?
            3.- Un usuario?
            4.- Un producto?
            0.- Presione cualquier número para salir al menu principal
            ''')
            opcion1 = int(input("Ingrese una opcion: \n"))# Ingresar Clientes
            limpiarpantalla()
            if opcion1 == 1: # ingresar un cliente
                print("Un Cliente")
                
                puntos = int(input("Ingrese los puntos del cliente"))
                descto = float(input("Ingrese el descuento de este cliente"))
                cli_frecuente = input("Es un cliente frecuente? responda si o no: \n").capitalize()               
                
                if cli_frecuente == "Si":
                    cli_frecuente = True
                else:
                    cli_frecuente = False
               
                cliente = Clientes(puntos, descto, cli_frecuente)
                
                cliente.insert_cli()

                print("=============Se a ingresado un nuevo cliente con exito=========== \n")
                input("Presione una tecla para volve al menu principal: \n")
                limpiarpantalla()
                Menu.__init__()
            elif opcion1 == 2:       # Ingresar un trabajador      
                # run, inicio_turno,termino_turno,fcontr,perf_cod
                run = int(input("Digite el rut del trabajador: \n"))
                inicio_turno = input("Ingrese el inicio de turno en formato 'YYYY-MM-DD HH:MM:SS' : \n")
                termino_turno = input("Ingrese el termino de turno en formato 'YYYY-MM-DD HH:MM:SS' : \n")
                fcontr = input("Ingrese la fecha de contratacion del trabajador en formato YYYY-MM-DD : \n")
                perf_cod = int(input("Ingrese 1 para cajero, 2 para administrador y 3 para garzón: \n"))
                
                worker = Trabajador(inicio_turno,termino_turno, fcontr, run, perf_cod)
                worker.insertar_tra()                
                print("=============Se a ingresado un nuevo trabajador con exito=========== \n")
                input("Presione una tecla para volve al menu principal: \n")
                limpiarpantalla()
                Menu.__init__()
            elif opcion1 == 3: # Ingresar un usuario
                print("Un usuario")
                nombre = input("Ingrese el nombre del usuario: \n--->")
                password = input("Crea tu clave de usuario: \n--->")
                cli_cod = int(input("Ingrese el codigo de cliente asignado: \n--->"))

                usuario = Usuario(nombre, password, cli_cod)
                usuario.insertar_usu_cli()
                print("=============Se a ingresado un nuevo usuario con exito=========== \n")
                input("Presione una tecla para volve al menu principal: \n")
                limpiarpantalla()
                Menu.__init__()

            elif opcion1 == 4: # Ingresar un producto
                
                # {self.nombre}','{self.descripcion}', {self.stock},{self.precio}
                nombre = input("Ingrese el nombre del producto: \n--->")
                descripcion = input("Agregue una descripcion para este producto: \n--->")
                stock = int(input("Ingrese la cantidad: \n"))
                precio = int(input("Ingrese el precio de este producto: \n--->"))

                producto = Productos(nombre, descripcion, stock, precio)
                producto.insertar_pro()
                print("=============Se a ingresado un nuevo producto con exito=========== \n")
                input("Presione una tecla para volve al menu principal: \n")
                limpiarpantalla()
                Menu.__init__()    

            else:
                Menu.__init__()              

        elif opcion == 2: # Mostrar algo ********************************************************************
            print('''
            ========Que tipo de datos desea mostrar?======
            1.- De clientes?
            2.- De trabajadores?
            3.- De productos?
            4.- De usuarios?
            0.- Presione cualquier número para salir al menu principal
            ''')
            opcion2 = int(input("Ingrese una opcion: \n--->"))# de que?
            limpiarpantalla()

            if opcion2 == 1: # Mostrar un cliente
                #------------------------------------------------------------------>Sub-Sub_menu 2 OPCIONES
                print('''
                =====Especifique====
                1.- Un cliente en especifico?
                2.- Todos los clientes registrados?
                0.- Presione cualquier número para salir al menu principal
                ''')
                opCli = int(input("Especifique!\n"))
                limpiarpantalla()

                if opCli == 1: # Cliente especifico #------------------------------>RESPUESTA--<Sub-Sub-Menu
                    print("Mostraremos un cliente especifico")
                    id = int(input("Ingrese el codigo de cliente que quiere mostrar: \n"))
                    Clientes.mostrar_cli_uq(id)
                elif opCli == 2: # Cliente especifico #------------------------------>RESPUESTA--<Sub-Sub-Menu
                    print("Mostraremos a todos los clientes")
                    Clientes.mostrar_cli()
                else:
                    limpiarpantalla()
                    Menu.__init__()
            elif opcion2 == 2: # Mostrar un trabalhador
                #------------------------------------------------------------------>Sub-Sub_menu 2 OPCIONES
                print('''
                =====Especifique====
                1.- Un trabajador en especifico?
                2.- Todos los trabajadores registrados?
                0.- Presione cualquier número para salir al menu principal
                ''')

                opTrab = int(input("Especifique: \n"))
                limpiarpantalla()

                if opTrab == 1: # Trabajador especifico #-------------------------->RESPUESTA--<Sub-Sub-Menu
                    print("Mostraremos un trabajador en especifico")  
                    id = int(input("Ingrese el id del trabajador: \n"))             
                    Trabajador.mostrar_tra_uq(id)
                elif opTrab == 2: #Todos los Trabajadores--------------------------->RESPUESTA--<Sub-Sub-Menu
                    print("=======================Lista de trabajadores vigentes en el registro========================= ")
                    Trabajador.mostrar_tra()
                    print("=======================Lista de trabajadores vigentes en el registro========================= ")
                else:
                    limpiarpantalla()
                    Menu.__init__()
            elif opcion2 == 3: # Mostrar productos 
                print('''
                =====Especifique====
                1.- Un producto en especifico?
                2.- Todos los productos registrados?
                0.- Presione cualquier número para salir al menu principal
                ''')
                opProd = int(input("Especifique: \n"))
                limpiarpantalla()
                if opProd == 1:
                    print("Mostrar un producto especifico")
                    id = int(input("Ingrese el id del producto: \n"))             
                    Productos.mostrar_pro_uq(id)
                    input("Presione una tecla para volve al menu principal: \n")
                    limpiarpantalla()
                    Menu.__init__()

                elif opProd == 2:
                    print("Mostrar todos los productos")
                    Productos.mostrar_pro()
                    input("Presione una tecla para volve al menu principal: \n")
                    limpiarpantalla()
                    Menu.__init__()
                else:
                    limpiarpantalla()
                    Menu.__init__()
                
            elif opcion2 == 4: # Mostrar usuario
                print('''
                =====Especifique====
                1.- Un usuario en especifico?
                2.- Todos los usuarios registrados?
                0.- Presione cualquier número para salir al menu principal
                ''')
                opUsu = int(input("Especifique: \n"))
                limpiarpantalla()
                if opUsu == 1:  #Mostramos un usuario especifico--------------------------->RESPUESTA--<Sub-Sub-Menu
                    
                    id = int(input("Ingrese el id del usuario: \n"))             
                    Usuario.mostrar_usu_uq(id)
                    print("Mostrando el usuario seleccionado: \n")
                    input("Presione una tecla para volve al menu principal: \n")
                    limpiarpantalla()
                    Menu.__init__()

                elif opUsu == 2: # Mostramos Todos los usuarios --------------------------->RESPUESTA--<Sub-Sub-Menu
                    
                    Usuario.mostrar_usu()
                    print("Mostrando todos los usuarios")
                    input("Presione una tecla para volve al menu principal: \n")
                    limpiarpantalla()
                    Menu.__init__()
                else:
                    limpiarpantalla()
                    Menu.__init__()
            else:
                Menu.__init__()

        elif opcion == 3: # Actualizar algo*****************************************************************************************

            print('''
            =========Que desea actualizar?========
            1.- Un trabajador?
            2.- Un client?
            3.- Un usuario?
            4.- Un producto?
            0.- Presione cualquier número para salir al menu principal
            ''')

            opcion3 = int(input("Ingrese una opcion: \n")) # que actualizar?
            limpiarpantalla()

            if opcion3 == 1: #----------------------------------------------------Actualizar Worker
                Trabajador.mostrar_tra()
                id = int(input("Elija el id del trabajador que desea modificar: \n--->"))

                limpiarpantalla()
                Trabajador.mostrar_usu_uq()
                # id,inicio_turno,termino_turno,perf_cod
                inicio_turno = input("Cambiar el inicio de turno o mantener el actual: \n--->")
                termino_turno = input("Cambiar el termino de turno o mantener el actual: \n")
            elif opcion3 == 2: #-------------------------------------------------Actualizar cliente

                Clientes.mostrar_cli()
                id = int(input("Elija el id del clinte que desea modificar: \n--->"))

                limpiarpantalla()
                Clientes.mostrar_cli_uq(id)

                puntos = int(input("Ingrese los puntos acumulados o mantenga los actuales: \n"))
                limpiarpantalla()
                Clientes.mostrar_cli_uq(id)
                descto = float(input("Ingrese los descuentos o mantenga los actuales: \n"))
                limpiarpantalla()
                
                Clientes.actualizar_cli(id, puntos, descto)
                limpiarpantalla()

                print("=============Se ha actualizado un cliente con exito=========== \n")
                Clientes.mostrar_cli_uq(id)
                input("Presione una tecla para volve al menu principal: \n")

                limpiarpantalla()
                Menu.__init__()
            elif opcion3 == 3: #------------------------------------------------Actualizar usuario

                Usuario.mostrar_usu()            
                id = int(input("Elija el id del usuario que desea modificar: \n--->"))

                limpiarpantalla()
                Usuario.mostrar_usu_uq(id)
                
                nombre = input("Ingrese el nuevo nombre de usuario o mantenga el mismo de siempre: \n")
                limpiarpantalla()
                Usuario.mostrar_usu_uq(id)
                password = input("Ingrese la nueva clave o mantenga la misma de siempre: \n")               

                Usuario.actualizar_usu(id, nombre, password)
                limpiarpantalla()

                print("=============Se ha actualizado un usuario con exito=========== \n")
                Usuario.mostrar_usu_uq(id)
                input("Presione una tecla para volve al menu principal: \n")

                limpiarpantalla()
                Menu.__init__()
            elif opcion3 == 4: #--------------------------------------Actualizar producto
                Productos.mostrar_pro()
                id = int(input("Elija el id del producto que desea modificar: \n--->"))

                limpiarpantalla()
                Usuario.mostrar_usu_uq(id)
            else:
                limpiarpantalla()
                Menu.__init__()

        elif opcion == 4: # Eliminar algo******************************************************************************

            print('''
            ===========Que tipo de dato quiere eliminar?=========
            1.- Un cliente?
            2.- Un trabajador?
            3.- Un usuario?
            4.- Un producto?
            0.- Presione cualquier número para salir al menu principal      
            ''')

            opcion4 = int(input("Ingrese una opcion: \n")) # que eliminar?
            limpiarpantalla()

            if opcion4 == 1: # ---------------------------------------------ELIMINAR CLIENTE
                
                id = int(input("Ingrese el id de quien quiere eliminar: \n"))
                Clientes.eliminar_cli(id)
                print(f"Se ha eliminado al cliente: {id}")
                input("Presione una tecla para volve al menu principal: \n")
                limpiarpantalla()
                Menu.__init__()

            elif opcion4 == 2: #------------------------------------------ELIMINAR TRABAJADOR
                
                id = int(input("Ingrese el id de quien quiere eliminar: \n"))
                Trabajador.eliminar_tra(id)
                print(f"Se ha eliminado el trabajador: {id}")
                input("Presione una tecla para volve al menu principal: \n")
                limpiarpantalla()
                Menu.__init__()

            elif opcion4 == 3: #-------------------------------------------ELIMINAR USUARIO
                
                id = int(input("Ingrese el id de quien quiere eliminar: \n"))
                Usuario.eliminar_usu(id)
                print(f"Se ha eliminado al usuario: {id}")
                input("Presione una tecla para volve al menu principal: \n")
                limpiarpantalla()
                Menu.__init__()

            elif opcion4 == 4: # -------------------------------------------ELIMINAR PRODUCTO
                
                id = int(input("Ingrese el id del producto que quiere eliminar: \n"))
                Productos.eliminar_pro(id)
                print(f"Se ha eliminado el producto: {id}")
                input("Presione una tecla para volve al menu principal: \n")
                limpiarpantalla()
                Menu.__init__()

            else:
                limpiarpantalla()
                Menu.__init__()
        elif opcion == 5:
            pass

limpiarpantalla()
Menu.__init__()
