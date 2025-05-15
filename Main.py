import Connector as c
import pandas as pd
import os
host1 = input("Digite o host1 >> ").strip()
user1 = input("Digite o user1 >> ").strip()
senha1 = input("Digite a senha1 >> ").strip()
database1 = input("Digite a database1 >> ").strip()

host2 = input("Digite o host2 >> ").strip()
user2 = input("Digite o user2 >> ").strip()
senha2 = input("Digite a senha2 >> ").strip()
database2 = input("Digite a database2 >> ").strip()

host3 = input("Digite o host3 >> ").strip()
user3 = input("Digite o user3 >> ").strip()
senha3 = input("Digite a senha3 >> ").strip()
database3 = input("Digite a database3 >> ").strip()

table1 = input("Digite a tabela1 >> ").strip()
table2 = input("Digite a tabela2 >> ").strip()
table3 = input("Digite a tabela3 >> ").strip()

connection_1 = c.connect(
    host1, user1, senha1, database1)
connection_2 = c.connect(
    host2, user2, senha2, database2)
connection_3 = c.connect(
    host3, user3, senha3, database3)


df_1 = connection_1.read(table1)
df_2 = connection_2.read(table2)
df_3 = connection_3.read(table3)

df_4 = pd.merge(df_1, df_2, on=list(
                set(df_1.columns) & set(df_2.columns)), how="outer")
df_4 = pd.merge(df_4, df_3, on=list(
                set(df_4.columns) & set(df_3.columns)), how="outer")

while True:
    choice1 = str(input(
        "Oq deseja fazer 1-Verificar um cliente especifico| 2-Verificar todos os clientes| 3-Desejo exportar para um arquivo ")).strip()

    match choice1:
        case '1':
            metodos = [f"{i}-{v}" for i, v in enumerate(df_4.columns)]
            try:
                choice2 = int(
                    input(f"Qual Método vc deseja usar como pesquisa? {list(metodos)} "))
            except:
                print('Opção invalida')
            choiced = df_4.columns[choice2]
            pesquisa = input(f"Digite o(a) {choiced} do cliente ").strip()
            try:
                df_5 = df_4[df_4[choiced] == pesquisa]
                if df_5.empty:
                    print(f"Nenhum usuario com este(a) {choiced}")
                else:
                    print(df_5)
            except:
                print("Erro ao buscar o usuario")

        case '2':
            print(df_4)
        case '3':
            choice3 = int(input("Qual tipo de arquivo deseja utilizar 2-xlsx|1-csv"))
            dowload_path = os.path.join(os.path.expanduser("~"),"Downloads")
            if choice3 == 1:
                try:
                    file_path = os.path.join(dowload_path,"Cliente.csv")
                    df_4.to_csv(file_path, index=False)
                except:
                    print("erro ao instalar o arquivo")
            elif choice3 == 2:
                try:
                    file_path = os.path.join(dowload_path,"Cliente.xlsx")
                    df_4.to_excel(file_path, index=False)
                except:
                    print("Erro ao instalar o arquivo")
            else:
                print("Opção invalida")
        case _:
            print("opção invalidada")
