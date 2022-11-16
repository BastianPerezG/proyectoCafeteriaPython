from getpass import getpass
from mysql.connector import connect, Error


class DataBase:

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def conectar(self):
        try:
            with connect(
                host="localhost",
                user=self.user,
                password=self.password,
                database="cinema"
            ) as connection:
                print(connection)
                select = "SELECT * FROM person"
                with connection.cursor() as cursor:
                    cursor.execute(select)
                    for row in cursor.fetchall():
                        print(row)
        except Error as e:
            print(e)


