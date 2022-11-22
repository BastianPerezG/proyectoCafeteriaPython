from getpass import getpass
from mysql.connector import connect, Error


class DataBase:

    def __init__(self):

        connection = connect(
            host = 'localhost',
            user = "root",
            password = "Nokia2022",
            dabatabase = "cafeteria_poo",
        )
        self.connection = connection

    def insert(self,sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        self.close()

    def close(self):
        self.connection.close()
        print("La conexion fue cerrada")

    def select(self,sql):
        cursor = self.connection.cursor()
        sql = "SELECT * FROM personas;"
        cursor.execute(sql)
        for row in cursor.fetchall():
            print(row)

