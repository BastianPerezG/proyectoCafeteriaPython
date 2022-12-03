from conector import DataBase
class Usuario:

    def __init__(self, nombre,password, tra_cod,cli_cod):
        self.nombre = nombre
        self.password = password
        self.cli_cod = cli_cod
        self.tra_cod = tra_cod



    def insertar_usu_cli(self):
        sql = f"INSERT INTO usuarios (usu_nom,usu_pass,cli_cod) VALUE ('{self.nombre}','{self.password}', {self.cli_cod});"
        db = DataBase()
        db.insert(sql)

    def insertar_usu_tra(self):
        sql = f"INSERT INTO usuarios (usu_nom,usu_pass,tra_cod) VALUE ('{self.nombre}','{self.password}', {self.tra_cod});"
        db = DataBase()
        db.insert(sql)

    def mostrar_usu(self):
        tabla = 'usuarios' 
        db = DataBase()
        db.select(tabla)

    def mostrar_usu_uq(id):
        tabla = 'usuarios'
        columna = 'usu_cod' 
        db = DataBase()
        db.select(tabla, id)

    def actualizar_usu(self):
        pass

    def eliminar_usu(cod):
        sql = 'DELETE FROM usuario WHERE usu_cod = {cod};'
        db = DataBase()
        db.delete(sql)