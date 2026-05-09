from app.database.connection import conectar

def adicionar_insumo(produto):
    
    conexao = conectar()
    cursor = conexao.cursor()
    
    
    cursor.execute(''' INSERT INTO Estoque (Produto,Quantidade,DataValidade,Lote) VALUES (?,?,?,?) '''
                    (
                    produto.nome,
                    produto.quantidade,
                    produto.validade,
                    produto.lote
                    )
                 )
    
    conexao.commit()
    
    cursor.close()
    conexao.close
                   
