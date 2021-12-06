
#Trabalhando com banco de dados em Python
#utilizando SQLite3
#
#Visualizando  dados (EXEMPLO 1):

import sqlite3

def visualizarDados():
    banco = sqlite3.connect('banco001.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM pessoas")
    print(cursor.fetchall())
    banco.commit()
    banco.close()

visualizarDados()

