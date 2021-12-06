
#Trabalhando com banco de dados em Python
#utilizando SQLite3
#
#Criando a tabela no banco de dados:

import sqlite3

def criarTabela():
    banco = sqlite3.connect('banco001.db')
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE pessoas (nome text, idade int, email text)")
    banco.commit()
    banco.close()

criarTabela()
