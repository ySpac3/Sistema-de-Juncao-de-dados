import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

class connect():
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        pass

    def read(self,table):
        url = f'mysql+mysqlconnector://{self.user}:{self.password}@{self.host}/{self.database}'
        engine = create_engine(url)
        try:
            df = pd.read_sql(f"Select * FROM {table}", engine)
            return df
        finally:
            engine.dispose()