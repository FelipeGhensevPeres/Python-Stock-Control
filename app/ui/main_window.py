from tkinter import Tk,Canvas,Button,PhotoImage,Text,Entry,END         
from app.models.produto import Produto
from app.services.estoque_service import adicionar_insumo,deletar_insumo,consumir_insumo,visualizar_insumo


#INICIAR INTERFACE 
def iniciar_sistema():


    # ADICIONAR INSUMO NA INTERFACE
    def adicionar_insumo_ui():

        produto = Produto(
            nome=nome_insumo.get(),
            quantidade=int(qtde_insumo.get()),
            validade=data_insumo.get(),
            lote=int(lote_insumo.get())
        )

        adicionar_insumo(produto=produto)

        caixa_texto.delete("1.0", END)

        caixa_texto.insert(
            "1.0",
            f"{produto.nome} adicionado com sucesso!"
        )
        
        
    # DELETAR INSUMO NA INTERFACE
    def deletar_insumo_ui():
        
        if len(nome_insumo.get()) < 2 or len(lote_insumo.get()) < 1:
            caixa_texto.delete('1.0',END)
            
            caixa_texto.insert('1.0', 'Nome do Insumo Inválido')
            
            return
        
        
        deletar_insumo(nome=nome_insumo.get(),
                       lote=int(lote_insumo.get()))
        
        caixa_texto.delete('1.0',END)
        
        
        caixa_texto.insert('1.0',f'{nome_insumo.get()} deletado com sucesso!')
        
    
    # CONSUMIR INSUMO DA INTERFACE
    def consumir_insumo_ui():
        if (len(nome_insumo.get()) < 2
        or len(qtde_insumo.get()) < 1
        or len (lote_insumo.get()) < 1):
            
            caixa_texto.delete('1.0',END)
            
            caixa_texto.insert('1.0','Nome,Lote e Quantidade do Insumo Inválido')
            
            return
        
        consumir_insumo(nome=nome_insumo.get(),
                        lote=int(lote_insumo.get()),
                        quantidade=int(qtde_insumo.get()))
        
        caixa_texto.delete('1.0',END)
        
        caixa_texto.insert('1.0',f'Insumo {nome_insumo.get()} consumido com sucesso em {qtde_insumo.get()} quantidades')
        
    
    # VISUALIZACAO DO INSUMO NA INTERFACE
    def visualizar_insumo_ui():
        
        if len(nome_insumo.get()) < 2:
            
            caixa_texto.delete('1.0',END)
            
            caixa_texto.insert('1.0','Nome do Insumo Inválido')
            
            return
            
        
        valores = visualizar_insumo(nome=nome_insumo.get())
        
        texto = ''
        
        for (id_produto,produto,quantidade,validade,lote) in valores:
            
            texto += f'''
            --------------------------
            Produto: {produto}
            Quantidade: {quantidade}
            Validade: {validade}
            Lote: {lote}
            '''
            
            caixa_texto.delete('1.0',END)
            
            caixa_texto.insert('1.0',texto)
    

    window = Tk()

    window.geometry("711x646")
    window.configure(bg="#ffffff")

    canvas = Canvas(
        window,
        bg="#ffffff",
        height=646,
        width=711,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    background_img = PhotoImage(
        file="janela/background.png"
    )

    canvas.create_image(
        355.5,
        323.0,
        image=background_img
    )
    
    
    img0 = PhotoImage(file="janela/img0.png")
    
    b0 = Button(image=img0,
                borderwidth=0,
                highlightthickness=0,
                command=visualizar_insumo_ui,
                relief='flat')
    
    b0.place(
        x=479,
        y=195,
        width=178,
        height=38
    )
    
    
    img1 = PhotoImage(file="janela/img1.png")
    
    b1 = Button(image=img1,
                borderwidth=0,
                highlightthickness=0,
                command=deletar_insumo_ui,
                relief='flat')
    
    b1.place(
        x=247,
        y=197,
        width=178,
        height=36
    )
    
    
    img2 = PhotoImage(file="janela/img2.png")
    
    b2 = Button(image=img2,
                borderwidth=0,
                highlightthickness=0,
                command=consumir_insumo_ui,
                relief='flat')
    
    b2.place(
        x=479,
        y=123,
        width=178,
        height=35
    )
    

    img3 = PhotoImage(file="janela/img3.png")

    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=adicionar_insumo_ui,
        relief="flat"
    )

    b3.place(
        x=247,
        y=125,
        width=178,
        height=34
    )

    caixa_texto = Text(
        bd=0,
        bg="#ffffff",
        highlightthickness=0
    )

    caixa_texto.place(
        x=250,
        y=502,
        width=410,
        height=114
    )

    nome_insumo = Entry(
        bd=0,
        bg="#ffffff",
        highlightthickness=0
    )

    nome_insumo.place(
        x=377,
        y=278,
        width=280,
        height=31
    )

    data_insumo = Entry(
        bd=0,
        bg="#ffffff",
        highlightthickness=0
    )

    data_insumo.place(
        x=377,
        y=324,
        width=280,
        height=31
    )

    lote_insumo = Entry(
        bd=0,
        bg="#ffffff",
        highlightthickness=0
    )

    lote_insumo.place(
        x=377,
        y=372,
        width=280,
        height=31
    )

    qtde_insumo = Entry(
        bd=0,
        bg="#ffffff",
        highlightthickness=0
    )

    qtde_insumo.place(
        x=377,
        y=420,
        width=280,
        height=31
    )

    window.resizable(False, False)

    window.mainloop()