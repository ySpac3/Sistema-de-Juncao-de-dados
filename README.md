# Como funciona

Um sistema que busca informações de 3 bancos de dados mysql diferentes e unem todos em um dataframe só podendo ser exportado como csv ou xlsx ou listar um usuário em especifico presente nesses banco de dados ou ser alterada alguma informação de um usuario
assim mudando todas as informaçõs em todos os 3 bancos de dados caso possua neste banco

# Como usar

No inicio será pedido os 3 logins de banco de dados como HOST,USER,PASSWORD,DATABASE, após isso será perguntado oq deseja fazer 
Caso queira apenas vizualizar será imprimido um dataframe com todos usuarios e suas informações
Caso queira alterar uma informação será pedido o código do usuario assim podendo ser alterada a informação necessaria
Caso queira listar um usuario especifico por alguma informação será perguntada qual informação deseja ser utilizada de base para a pesquisa e após isso será pedido o valor da informação, assim que passado será imprimido novamente as informações do cliente requisitado

