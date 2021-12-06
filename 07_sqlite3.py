
#Trabalhando com banco de dados em Python,
#utilizando SQLite3.
#
#Visualizar dados (EXEMPLO 3)

import sqlite3

def visualizarDados3():
    banco = sqlite3.connect('banco_dados.db')
    cursor = banco.cursor()
    cursor.execute("SELECT email FROM pessoas WHERE idade = 30")
    print(cursor.fetchall())
    banco.commit()
    banco.close()

visualizarDados3()


