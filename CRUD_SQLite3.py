
#CRUD COM SQLITE3 E PYQT5
import sys
import sqlite3
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *

numero_id = 0

# CLASSE REFERENTE A TELA DE ATUALIZAÇÃO
class Janela3 (QMainWindow):
    def __init__(self):
        super().__init__()

        self.primeiraLabel()
        self.segundaLabel()
        self.primeiroBotao()
        self.primeiraLinha()
        self.segundaLinha()
        self.terceiraLinha()
        self.quartaLinha()
        self.carregarJanela()

    # CARACTERÍSTICAS DA PRIMEIRA LABEL
    def primeiraLabel(self):
        self.label1a = QtWidgets.QLabel(self)
        self.label1a.move(20, 0)
        self.label1a.resize(400, 60)
        self.label1a.setAlignment(QtCore.Qt.AlignCenter)
        self.label1a.setText("CRUD com SQLite3")
        self.label1a.setFont(QtGui.QFont("Arial", 14,
                                   QtGui.QFont.Black))

    # CARACTERÍSTICAS DA SEGUNDA LABEL
    def segundaLabel(self):
        self.label2a = QtWidgets.QLabel(self)
        self.label2a.move(20, 50)
        self.label2a.resize(400, 60)
        self.label2a.setAlignment(QtCore.Qt.AlignLeft)
        self.label2a.setText("Digite os Dados para Atualização:")
        self.label2a.setFont(QtGui.QFont("Arial", 12,
                                   QtGui.QFont.Black))

    # CARACTERÍSTICAS DA PRIMEIR0 BOTÃO
    def primeiroBotao(self):
        self.botao1a = QPushButton("Atualizar", self)
        self.botao1a.move(20, 200)
        self.botao1a.resize(100, 30)
        self.botao1a.clicked.connect(self.atualizarLinha)

    # CARACTERÍSTICAS DA PRIMEIRA LINHA
    def primeiraLinha(self):
        self.linha1a = QLineEdit("", self)
        self.linha1a.move(20, 110)
        self.linha1a.resize(400, 20)
        self.linha1a.setMaxLength(50)
        self.linha1a.setPlaceholderText("Digite o nome")

    # CARACTERÍSTICAS DA SEGUNDA LINHA
    def segundaLinha(self):
        self.linha2a = QLineEdit("", self)
        self.linha2a.move(20, 140)
        self.linha2a.resize(100, 20)
        self.linha2a.setMaxLength(3)
        self.linha2a.setPlaceholderText("Digite a idade")

    # CARACTERÍSTICAS DA TERCEIRA LINHA
    def terceiraLinha(self):
        self.linha3a = QLineEdit("", self)
        self.linha3a.move(20, 170)
        self.linha3a.resize(400, 20)
        self.linha3a.setMaxLength(50)
        self.linha3a.setPlaceholderText("Digite o e-mail")

    def quartaLinha(self):
        self.linha4a = QLineEdit("", self)
        self.linha4a.move(20, 80)
        self.linha4a.resize(100, 20)
        self.linha4a.setMaxLength(3)
        self.linha4a.setPlaceholderText("ID")



    # EVENTO DE FECHAMENTO DA JANELA 2 (RETORNA A JANELA PRINCIPAL)
    def closeEvent(self, event):
        self.retornaJanela1 = JanelaPrincipal()
        self.retornaJanela1.show()
        event.accept()

    def atualizarLinha(self):
        global  numero_id
        nome1 = self.linha1a.text()
        idade1 = self.linha2a.text()
        email1 = self.linha3a.text()
        id1 = self.linha4a.text()
        banco = sqlite3.connect('banco_dados1.db')
        cursor = banco.cursor()
        cursor.execute(f"UPDATE pessoas SET "
                       f"nome = {nome1}, "
                       f"idade = {idade1}, "
                       f"email = {email1} "
                       f"WHERE id = {id1}")
        banco.commit()
        banco.close()
        self.close()

    # CARACTERÍSTICAS DA JANELA 1
    def carregarJanela(self):
        self.setGeometry(700,100,440,240)
        self.setWindowTitle("Janela 3")
        self.setFixedSize(440,240)


# CLASSE REFERENTE A JANELA 2
class Janela2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.jan3 = Janela3()

        self.primeiroBotao()
        self.segundoBotao()
        self.primeiraLabel()
        self.segundaLabel()

        self.carregarJanela2()
        self.listaGeral()

    # CARACTERÍSTICAS DA JANELA 2
    def carregarJanela2(self):
        self.setGeometry(700,100,440,560)
        self.setWindowTitle("Janela 2")
        self.setFixedSize(440,560)

    # CARACTERÍSTICAS DA PRIMEIRA LABEL
    def primeiraLabel(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.move(20, 0)
        self.label1.resize(400, 60)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setText("CRUD com SQLite3")
        self.label1.setFont(QtGui.QFont("Arial", 14,
                                   QtGui.QFont.Black))

    # CARACTERÍSTICAS DA SEGUNDA LABEL
    def segundaLabel(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.move(20, 60)
        self.label1.resize(200, 60)
        self.label1.setAlignment(QtCore.Qt.AlignLeft)
        self.label1.setText("Lista de Dados:")
        self.label1.setFont(QtGui.QFont("Arial", 12,
                                   QtGui.QFont.Black))

    # CARACTERÍSTICAS DA PRIMEIR0 BOTÃO
    def primeiroBotao(self):
        self.botao1 = QPushButton("Excluir Dados", self)
        self.botao1.move(320, 500)
        self.botao1.resize(100, 30)
        self.botao1.clicked.connect(self.apagarDados)

    def segundoBotao(self):
        self.botao2 = QPushButton("Atualizar Dados", self)
        self.botao2.move(20, 500)
        self.botao2.resize(100, 30)
        self.botao2.clicked.connect(self.atualizarDados)

    # CARACTERÍSTICAS DA TABELA DE VISUALIZAÇÃO DE DADOS
    def listaGeral(self):
        self.lista = QTableWidget(self)
        self.lista.setColumnCount(4)
        self.lista.setHorizontalHeaderLabels(('Id', 'Nome', 'Idade', 'E-mail'))
        self.lista.setColumnWidth(0,120)
        self.lista.setColumnWidth(1,50)
        self.lista.move(20, 90)
        self.lista.resize(400, 400)

    def atualizarDados(self):
        global numero_id
        linha = self.lista.currentRow()

        banco = sqlite3.connect('banco_dados1.db')
        cursor = banco.cursor()
        cursor.execute("SELECT id FROM pessoas")
        dados_lidos = cursor.fetchall()
        valor_id = dados_lidos[linha][0]
        cursor.execute("SELECT * FROM pessoas WHERE id = " + str(valor_id))
        pessoa = cursor.fetchall()
        self.jan3.show()
        self.close()

        numero_id = valor_id

        self.jan3.linha4a.setText(str(pessoa[0][0]))
        self.jan3.linha1a.setText(str(pessoa[0][1]))
        self.jan3.linha2a.setText(str(pessoa[0][2]))
        self.jan3.linha3a.setText(str(pessoa[0][3]))


    def apagarDados(self):
        banco = sqlite3.connect('banco_dados1.db')
        cursor = banco.cursor()
        linha = self.lista.currentRow()
        self.lista.removeRow(linha)
        cursor.execute("SELECT id FROM pessoas")
        dados_lidos = cursor.fetchall()
        valor_id = dados_lidos[linha][0]
        cursor.execute("DELETE FROM pessoas WHERE id = " + str(valor_id))

        banco.commit()
        banco.close()

    # CARREGA OS DADOS DO BANCO NA TABELA DE VISUALIZAÇÃO
    def carrgarDados(self):
        banco = sqlite3.connect('banco_dados1.db')
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM pessoas")
        dados_lidos = cursor.fetchall()

        self.lista.setRowCount(len(dados_lidos))

        for i in range(0, len(dados_lidos)):
            for j in range(0, 4):
                self.lista.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

        banco.close()

# CLASSE REFERENTE A TELA DE CADASTRO
class JanelaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.jan2 = Janela2()

        self.primeiraLabel()
        self.segundaLabel()
        self.primeiroBotao()
        self.segundoBotao()
        self.primeiraLinha()
        self.segundaLinha()
        self.terceiraLinha()
        self.carregarJanela()

    # CARACTERÍSTICAS DA PRIMEIRA LABEL
    def primeiraLabel(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.move(20, 0)
        self.label1.resize(400, 60)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setText("CRUD com SQLite3")
        self.label1.setFont(QtGui.QFont("Arial", 14,
                                   QtGui.QFont.Black))

    # CARACTERÍSTICAS DA SEGUNDA LABEL
    def segundaLabel(self):
        self.label2 = QtWidgets.QLabel(self)
        self.label2.move(20, 60)
        self.label2.resize(200, 60)
        self.label2.setAlignment(QtCore.Qt.AlignLeft)
        self.label2.setText("Digite seus dados:")
        self.label2.setFont(QtGui.QFont("Arial", 12,
                                   QtGui.QFont.Black))

    # CARACTERÍSTICAS DA PRIMEIR0 BOTÃO
    def primeiroBotao(self):
        self.botao1 = QPushButton("Cadastrar", self)
        self.botao1.move(20, 180)
        self.botao1.resize(100, 30)
        self.botao1.clicked.connect(self.botao_Inserir)

    # CARACTERÍSTICAS DA SEGUNDO BOTÃO
    def segundoBotao(self):
        self.botao2 = QPushButton("Visualizar Dados", self)
        self.botao2.move(320, 180)
        self.botao2.resize(100, 30)
        self.botao2.clicked.connect(self.botao_Visualizar)

    # CARACTERÍSTICAS DA PRIMEIRA LINHA
    def primeiraLinha(self):
        self.linha1 = QLineEdit("", self)
        self.linha1.move(20, 90)
        self.linha1.resize(400, 20)
        self.linha1.setMaxLength(50)
        self.linha1.setPlaceholderText("Digite o nome")

    # CARACTERÍSTICAS DA SEGUNDA LINHA
    def segundaLinha(self):
        self.linha2 = QLineEdit("", self)
        self.linha2.move(20, 120)
        self.linha2.resize(100, 20)
        self.linha2.setMaxLength(3)
        self.linha2.setPlaceholderText("Digite a idade")

    # CARACTERÍSTICAS DA TERCEIRA LINHA
    def terceiraLinha(self):
        self.linha3 = QLineEdit("", self)
        self.linha3.move(20, 150)
        self.linha3.resize(400, 20)
        self.linha3.setMaxLength(50)
        self.linha3.setPlaceholderText("Digite o e-mail")

    # CARACTERÍSTICAS DA JANELA 1
    def carregarJanela(self):
        self.setGeometry(700,100,440,240)
        self.setWindowTitle("Janela 1")
        self.setFixedSize(440,240)


    # EVENTO PARA INSERIR INFORMAÇÕES NO BANCO DE DADOS
    def botao_Inserir(self):
        nome = self.linha1.text()
        idade = self.linha2.text()
        email = self.linha3.text()

        '''
            1 - O EVENTO ABAIXO VERIFICA SE JÁ EXISTE UM BANCO DE DADOS COM O NOME PROPOSTO
            E CONECTA AO MESMO, SE NÃO EXISTIR, CRIA O BANCO DE DADOS E SE CONECTA A ELE. 
            2 - VERIFICA SE NO BANCO DE DADOS CONECTADO EXISTE A TABELA COM O NOME PROPOSTO,
            SE NÃO, CRIA A TABELA COM AS CARACTERÍSTICAS APONTADAS.
            3 - ESTANDO TUDO OK, INSERE AS INFORMAÇÕES NA TABELA DE DADOS.
        '''
        try:
            banco = sqlite3.connect('banco_dados1.db')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS pessoas ("
                            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "nome text,"
                            "idade int,"
                            "email text"
                            ")")
            cursor.execute("INSERT INTO pessoas VALUES(NULL, '"+nome+"', "+idade+", '"+email+"')")
            banco.commit()
            banco.close()
            self.linha1.setText("")
            self.linha2.setText("")
            self.linha3.setText("")

        except sqlite3.Error as erro:
            print(erro)

    # EVENTO DO BOTÃO PARA VISUALIZAÇÃO DOS DADOS DO BANCO
    def botao_Visualizar(self):
        self.jan2.carrgarDados()
        self.jan2.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela1 = JanelaPrincipal()
    tela1.show()
    sys.exit(app.exec_())


