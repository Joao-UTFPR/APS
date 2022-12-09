import tkinter as tk
from tela import Tela
from postgres import Postgres


class TelaRegistrarProduto(Tela):
    def set_tela(self):
        button_list = [
            tk.Button(
                master=self.frame,
                text="ver produtos registrados",
                width=50,
                command=self.ver_produtos,
            ),
            tk.Button(
                master=self.frame,
                text="Registrar",
                width=50,
                command=lambda: self.registrar(entry1.get()),
            ),
            tk.Button(
                master=self.frame, text="Voltar", width=50, command=self.back_to_start
            )
        ]
        entry_text1 = tk.StringVar()
        entry1 = tk.Entry(master=self.frame, textvariable=entry_text1)
        entry_text1.set("produto")
        entry1.pack()
        for button in button_list:
            button.pack()

    def registrar(self, produto):
        Postgres().alter(f"insert into Produto_Estoque values('{produto}', 0);")

    def ver_produtos(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        result = Postgres().select("SELECT * FROM Produto_Estoque")
        pontos = ""
        for produto in result:
            pontos += f"{produto[0]}\n"
        label = tk.Label(master=self.frame, text=pontos)
        label.pack()
        button = tk.Button(
            master=self.frame, text="Voltar", width=50, command=self.back
        )
        button.pack()

    def back(self):
        self.frame.destroy()
        TelaRegistrarProduto(self.window).set_tela()

    def back_to_start(self):
        self.window.destroy()
        window = tk.Tk()
        super().__init__(window)
        super().set_tela_inicial()