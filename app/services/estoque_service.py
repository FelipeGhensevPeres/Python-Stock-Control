from app.database.connection import conectar


# FUNCAO ADICIONAR INSUMO
def adicionar_insumo(produto):
    
    conexao = conectar()
    cursor = conexao.cursor()
    
    
    cursor.execute(f''' INSERT INTO Estoque
                   (Produto,Quantidade,DataValidade,Lote)
                   VALUES (?,?,?,?) 
                   ''',
                   (produto.nome,
                    produto.quantidade,
                    produto.validade,
                    produto.lote)
                   )
    

    conexao.commit()
    
    
    cursor.close()
    conexao.close
    
    
# FUNCAO DELETAR INSUMO
def deletar_insumo(nome,lote):
    
    conexao = conectar()
    cursor = conexao.cursor()
    
    
    cursor.execute('''
                   DELETE FROM Estoque 
                   WHERE Produto = ? AND Lote = ?
                   ''',
                   (nome,lote))
    
    
    conexao.commit()
    
    
    cursor.close
    conexao.close()
    

# FUNCAO CONSUMIR INSUMO
def consumir_insumo(nome,lote,quantidade):
    
    conexao = conectar()
    cursor = conexao.cursor()
    
    
    cursor.execute('''
                   UPDATE Estoque
                   SET Quantidade = Quantidade - ?
                   WHERE PRODUTO = ?
                   AND Lote = ?
                   ''',
                   (quantidade,nome,lote))
    
    
    conexao.commit()
    
    
    cursor.close()
    conexao.close()
    
    
# FUNCAO VISUALIZAR INSUMO
def visualizar_insumo(nome):
    
    
    conexao = conectar()
    cursor = conexao.cursor()
    
    
    cursor.execute('''
                   SELECT * 
                   FROM Estoque
                   WHERE Produto = ?
                   ''',
                   (nome,))
    
    valores = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    
    
    return valores
    
    
    
