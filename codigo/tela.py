import tkinter as tk

class Tela:
    def __init__(self, window):
        self.window = window
        self.frame = tk.Frame(master=self.window, width=100, height=100)
        self.frame.pack()

    def set_tela_inicial(self):
        button_list = [
            tk.Button(
                master=self.frame,
                text="gerenciar Pontos",
                width=50,
                command=self.gerenciar_pontos
            ),
            tk.Button(
                master=self.frame,
                text="Gerenciar Estoque",
                width=50,
                command=self.gerenciar_estoque,
            ),
            tk.Button(
                master=self.frame,
                text="Gerenciar Reservas",
                width=50,
                command=self.realizar_reserva,
            ),
            tk.Button(master=self.frame, text="Registrar Produto", width=50, command=self.registrar_produto),
            tk.Button(master=self.frame, text="Gerar Relatorio", width=50),
            tk.Button(
                master=self.frame,
                text="fechar",
                foreground="black",
                background="white",
                width=50,
                command=self.fechar_event,
            ),
        ]
        for button in button_list:
            button.pack()

    def fechar_event(self):
        self.window.destroy()

    def gerenciar_estoque(self):
        from tela_estoque import TelaEstoque
        self.frame.destroy()
        TelaEstoque(self.window).set_tela()

    def realizar_reserva(self):
        from tela_reserva import TelaReserva
        self.frame.destroy()
        TelaReserva(self.window).set_tela()

    def gerenciar_pontos(self):
        from tela_ponto import TelaPonto
        self.frame.destroy()
        TelaPonto(self.window).set_tela()

    def registrar_produto(self):
        from tela_registro_produto import TelaRegistrarProduto
        self.frame.destroy()
        TelaRegistrarProduto(self.window).set_tela()


