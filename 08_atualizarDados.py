
#Trabalhando com banco de dados em Python,
#utilizando SQLite3.
#
#Atualizar dados:

import sqlite3

def atualizarDados():
    banco = sqlite3.connect('banco_dados.db')
    cursor = banco.cursor()
    cursor.execute("UPDATE pessoas SET nome = 'Maria Moreira' WHERE idade = 30")
    banco.commit()
    banco.close()

atualizarDados()


