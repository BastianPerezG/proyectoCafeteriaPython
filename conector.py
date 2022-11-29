from getpass import getpass
from mysql.connector import connect, Error


class DataBase:

    def __init__(self):
        try:
            aux = connect(
                host ='localhost',
                user ='root',
                password = getpass("Ingrese la pass"),
                database ='cafeteria'
            )
            self.connection = aux
        except Error as e:
            print("Error" + e)

    def insert(self,sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            self.close()
        except Error as e:
            print(e)
    def close(self):
        self.connection.close()
        print("La conexion fue cerrada")

    def select(self, tabla):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM {tabla};")
        for row in cursor.fetchall():
            print(row)

    def update(self,sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        self.close()
    
    def delete(self,sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        self.close()

db = DataBase()
