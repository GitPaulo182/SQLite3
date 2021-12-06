
#Trabalhando com banco de dados em Python
#utilizando SQLite3
#
#Criando o banco de dados:
	
import sqlite3

def inserirDados():
    banco = sqlite3.connect('banco_dados.db')
    cursor = banco.cursor()
    cursor.execute("INSERT INTO pessoas VALUES('Paulo', 46, 'paulo@email.com')")
    banco.commit()
    banco.close()

inserirDados()
