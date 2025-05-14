import Connector as c
import pandas as pd

escolha = int(input("Oq deseja fazer 1-Verificar um cliente especifico| 2-Verificar todos os clientes "))

connection_1 = c.connect("localhost", "root", "240123Ex!", "bdclientesmonitor")

df_1 = connection_1.read('clientesmonitorados')




