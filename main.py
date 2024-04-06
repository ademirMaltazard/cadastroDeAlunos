from PyQt5 import QtWidgets, uic
import mysql.connector

# CONEXAO COM O BANCO
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="escola"
)

cursor = conexao.cursor(dictionary=True)

print("Conectado no banco com sucesso!!!")

# FUNÇÕES
def FuncaoExibirDados():
    matricula = formulario.lineEdit_Matricula.text()
    nome = formulario.lineEdit_Nome.text()
    senha = formulario.lineEdit_Senha.text()
    curso = ''
    print(f'matricula: {matricula}\n'
          f'nome: {nome}\n'
          f'senha: {senha}\n')
    # curso
    if formulario.radioButton_DS.isChecked():
        curso = ('DATA SCIENCE')
    elif formulario.radioButton_DFS.isChecked():
        curso = 'DESIGN FULL STACK'
    elif formulario.radioButton_PFS.isChecked():
        curso = 'PROGRAMAÇÃO FULL STACK'
    print(f'Curso: {curso}')

    #Inserir os dados no banco
    query = f'INSERT INTO aluno(nome_aluno, senha_aluno, curso)'\
                'VALUES (%s,%s, %s)'
    dados = (str(nome), str(senha), curso)
    cursor.execute(query, dados)
    conexao.commit()

def Show():
    consulta.show()
    query = '''SELECT * FROM aluno'''
    cursor.execute(query)
    dados = cursor.fetchall()
    consulta.tableWidget_Exibir.setRowCount(len(dados))

    row = 0
    for indice in dados:
        consulta.tableWidget_Exibir.setItem(row, 0, QtWidgets.QTableWidgetItem(str(indice["id_aluno"])))
        consulta.tableWidget_Exibir.setItem(row, 1, QtWidgets.QTableWidgetItem(indice["nome_aluno"]))
        consulta.tableWidget_Exibir.setItem(row, 2, QtWidgets.QTableWidgetItem(indice["senha_aluno"]))
        consulta.tableWidget_Exibir.setItem(row, 3, QtWidgets.QTableWidgetItem(indice["curso"]))
        row+=1


def filtrar():
    texto = consulta.textEdit_nome.toPlainText()
    filtro = ("%" + texto + "%")
    print(filtro)
    cursor.execute(f"SELECT * FROM aluno WHERE nome_aluno  LIKE '%s'", filtro)
    dados = cursor.fetchall()
    print(dados)

# Gerando um aplicação
app = QtWidgets.QApplication([])

# carregar arquivo .ui
formulario = uic.loadUi('cadastro.ui')
consulta = uic.loadUi('consulta.ui')

# Ações
formulario.pushButton_CADASTRAR.clicked.connect(FuncaoExibirDados)
formulario.pushButton_CONSULTA.clicked.connect(Show)
consulta.pushButton_filtrar.clicked.connect(filtrar)

# exibir a tela
formulario.show()
app.exec()
