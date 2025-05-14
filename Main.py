import Connector as c
import pandas as pd



connection_1 = c.connect(
    "localhost", "root", "240123Ex!", "bdclientesmonitor")
connection_2 = c.connect(
    "localhost", "root", "240123Ex!", "bdclientespagamento")
connection_3 = c.connect(
    "localhost", "root", "240123Ex!", "bdclientesatisfaçao")


df_1 = connection_1.read('clientesmonitorados')
df_2 = connection_2.read('clientepagamento')
df_3 = connection_3.read('clientesatisfeito')

while True:
    escolha = str(input(
    "Oq deseja fazer 1-Verificar um cliente especifico| 2-Verificar todos os clientes ")).strip()
    match escolha:
        
        case '2':
            df_4 = pd.merge(df_1, df_2, on=list(
                set(df_1.columns) & set(df_2.columns)), how="outer")
            df_4 = pd.merge(df_4, df_3, on=list(
                set(df_4.columns) & set(df_3.columns)), how="outer")
            print(df_4)
        case _:
            print("opção invalidada")


