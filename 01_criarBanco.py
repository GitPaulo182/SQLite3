
#Trabalhando com banco de dados em Python,
#utilizando SQLite3.
#
#Criando o banco de dados:

import sqlite3

def criarBanco():
    banco = sqlite3.connect('banco_dados.db')
    banco.commit()
    banco.close()

criarBanco()


