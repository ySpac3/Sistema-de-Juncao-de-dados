import mysql.connector
import pandas as pd

class connect():
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        pass

    def read(self,table):
        try:
            connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
            )
            cursor = connection.cursor()
            
            df = pd.read_sql(f"Select * FROM {table}", connection)

            return df
             

        except mysql.connector.Error as err:
            print(f"Erro: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()