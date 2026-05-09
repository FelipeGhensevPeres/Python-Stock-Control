from tkinter import Tk,Canvas,Button,PhotoImage,Text,Entry,END         
from app.models.produto import Produto
from app.services.estoque_service import adicionar_insumo


def iniciar_sistema():

    def adicionar_produto_ui():

        produto = Produto(
            nome=nome_insumo.get(),
            quantidade=qtde_insumo.get(),
            validade=data_insumo.get(),
            lote=lote_insumo.get()
        )

        adicionar_insumo(produto=produto)

        caixa_texto.delete("1.0", END)

        caixa_texto.insert(
            "1.0",
            f"{produto.nome} adicionado com sucesso!"
        )

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

    img3 = PhotoImage(file="janela/img3.png")

    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=adicionar_produto_ui,
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