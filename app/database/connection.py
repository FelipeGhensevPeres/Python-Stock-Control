import pyodbc

DADOS_CONEXAO = ('Driver=SQLite3 ODBC Driver;'
                 'Server=localhost;'
                 'Database=Estoque.db')


def conectar():
    
    conexao = pyodbc.connect(DADOS_CONEXAO)
    
    return conexao