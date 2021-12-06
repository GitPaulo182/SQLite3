
#Trabalhando com banco de dados em Python
#utilizando SQLite3
#
#Inserindo dados (EXEMPLO 2):

import sqlite3

def inserirDados2():
    nome = "Maria"
    idade = 30
    email = "maria@email.com"
    banco = sqlite3.connect('banco001.db')
    cursor = banco.cursor()
    cursor.execute("INSERT INTO pessoas VALUES('"+nome+"', "+str(idade)+", '"+email+"')")
    banco.commit()
    banco.close()

inserirDados2()
