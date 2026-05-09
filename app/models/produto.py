class Produto: 
    
    def __init__(self,
                 nome: str,
                 quantidade: int,
                 validade: str,
                 lote: int):
        
        
        self.nome = str(nome)
        self.quantidade = int(quantidade)
        self.validade = str(validade)
        self.lote = int(lote)
        
        
        
        def __str__(self):
            return(
                f'Produto: {self.nome} | '
                f'Quantidade: {self.quantidade} | ' 
            )
        