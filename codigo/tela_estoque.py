import tkinter as tk
from tela import Tela
from postgres import Postgres


class TelaEstoque(Tela):
    def set_tela(self):
        button_list = [
            tk.Button(
                master=self.frame,
                text="Checar Estoque",
                width=50,
                command=self.checar_estoque,
            ),
            tk.Button(
                master=self.frame,
                text="Alterar Estoque",
                width=50,
                command=self.altera_estoque_tela
            ),
        ]
        for button in button_list:
            button.pack()

    def checar_estoque(self):
        self.frame.destroy()
        self.frame = tk.Frame(master=self.window, width=100, height=100)
        self.frame.pack()
        result = Postgres().select("SELECT * FROM estoque")
        estoque = ""
        for item, qtd in result:
            estoque += f"{item}: {qtd}\n"
        label = tk.Label(master=self.frame, text=estoque)
        label.pack()
        button = tk.Button(
            master=self.frame, text="Voltar", width=50, command=self.back
        )
        button.pack()

    def altera_estoque_tela(self):
        self.frame.destroy()
        self.frame = tk.Frame(master=self.window, width=100, height=100)
        self.frame.pack()

        entry_text1 = tk.StringVar()
        entry_text2 = tk.StringVar()
        entry1=tk.Entry(master=self.frame, textvariable=entry_text1)
        entry2=tk.Entry(master=self.frame, textvariable=entry_text2)
        entry_text1.set("produto")
        entry_text2.set("estoque")
        entry1.pack()
        entry2.pack()
        button = tk.Button(
            master=self.frame, text="alterar", width=50, command=lambda : self.alterar(entry1.get(), entry2.get())
        )
        button.pack()

    def alterar(self, produto, estoque):
        Postgres().alter(f"UPDATE Estoque SET estoque={estoque} WHERE produto='{produto}';")
        self.back()

    def back(self):
        self.frame.destroy()
        TelaEstoque(self.window).set_tela()
