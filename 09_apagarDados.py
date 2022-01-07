
#Trabalhando com banco de dados em Python,
#utilizando SQLite3.
#
#Apagar dados:

import sqlite3

def apagarDados():
    try:
        banco = sqlite3.connect('banco_dados.db')
        cursor = banco.cursor()
        cursor.execute("DELETE FROM pessoas WHERE idade = 46")
        banco.commit()
        banco.close()
        print("Dados removidos!")

    except sqlite3.Error as erro:
        print("Erro ao remover: ", erro)

apagarDados()



