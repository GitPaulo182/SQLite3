
#Trabalhando com banco de dados em Python,
#utilizando SQLite3.
#
#Visualizar dados (EXEMPLO 1)

import sqlite3

def visualizarDados():
    banco = sqlite3.connect('banco_dados.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM pessoas")
    print(cursor.fetchall())
    banco.commit()
    banco.close()

visualizarDados()


