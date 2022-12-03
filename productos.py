from conector import DataBase
class Productos: 

    def __init__(self,nombre,descripcion, precio, stock):
        self.nombre= nombre
        self.descripcion= descripcion
        self.precio = precio
        self.stock = stock

    def insertar_pro(self):
        sql = f"INSERT INTO productos (pro_nombre,pro_descripcion,pro_stock,pro_precio) VALUE ('{self.nombre}','{self.descripcion}', {self.stock},{self.precio});"
        db = DataBase()
        db.insert(sql)

    def mostrar_pro(self):
        tabla = 'productos' 
        db = DataBase()
        db.select(tabla)

    def mostrar_pro_uq(id):
        tabla = 'productos'
        columna = 'pro_cod' 
        db = DataBase()
        db.select(tabla,columna, id)

    def actualizar_pro(self):
        pass
    def eliminar_pro(cod):
        sql = 'DELETE FROM productos WHERE pro_cod = {cod};'
        db = DataBase()
        db.delete(sql)