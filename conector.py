from getpass import getpass
from mysql.connector import connect, Error


class DataBase:

    def __init__(self, user, password):
        self.user = input("Ingrese nombre de usuario: ")
        self.password = getpass("Ingrese password : ")

    def conectar(self):
        try:
            with connect(
                host="localhost",
                user=self.user,
                password=self.password,
                database="cafeteria_poo"
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO personas (per_run, per_nombre, per_app, per_apm, per_tel, per_email, per_fnac) VALUE (111111113, 'Jose', 'Carcamo', 'Mata','123456789', 'jose.carcamo@gmail.com', '1940-04-10' )")
                    connection.commit()
                print(connection)
        except Error as e:
            print(e)
    def execute_query(self,query):
        pass



db = DataBase()
db.conectar()

