
#Trabalhando com banco de dados em Python,
#utilizando SQLite3.
#
#

import sqlite3

def inserirDados2():
    nome = "Maria"
    idade = 30
    email = "maria@email.com"
    banco = sqlite3.connect('banco_dados.db')
    cursor = banco.cursor()
    cursor.execute("INSERT INTO pessoas VALUES('"+nome+"', "+str(idade)+", '"+email+"')")
    banco.commit()
    banco.close()

inserirDados2()


