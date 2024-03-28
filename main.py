from PyQt5 import QtWidgets, uic
import mysql.connector

# CONEXAO COM O BANCO
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="escola"
)

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
    cursor = conexao.cursor()
    query = f'INSERT INTO aluno(nome_aluno, senha_aluno, curso)'\
                'VALUES (%s,%s, %s)'
    dados = (str(nome), str(senha), curso)
    cursor.execute(query, dados)
    conexao.commit()


# Gerando um aplicação
app = QtWidgets.QApplication([])



# carregar arquivo .ui
formulario = uic.loadUi('cadastro.ui')

# Ações
formulario.pushButton_CADASTRAR.clicked.connect(FuncaoExibirDados)

# exibir a tela
formulario.show()
app.exec()
