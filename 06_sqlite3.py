
#Trabalhando com banco de dados em Python,
#utilizando SQLite3.
#
#Visualizar dados (EXEMPLO 2)

import sqlite3

def visualizarDados2():
    banco = sqlite3.connect('banco_dados.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM pessoas WHERE idade = 46")
    print(cursor.fetchall())
    banco.commit()
    banco.close()

visualizarDados2()


