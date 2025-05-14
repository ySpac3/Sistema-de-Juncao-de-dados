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



            cursor.execute(f"SHOW COLUMNS FROM {table}")
            columns_result = cursor.fetchall()
            table_columns = [column[0] for column in columns_result]

            dt = {col: [] for col in table_columns }


            cursor.execute(f"SELECT * FROM {table}")
            table_result = cursor.fetchall()

            for row in table_result:
              for index,column_name in enumerate(table_columns):
                  dt[column_name].append(row[index])
            
            df = pd.DataFrame(dt)

            return df
             

        except mysql.connector.Error as err:
            print(f"Erro: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()