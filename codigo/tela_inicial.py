import tkinter as tk
from tela import Tela
from tela_estoque import TelaEstoque
from tela_reserva import TelaReserva


class TelaInicial(Tela):
    def set_tela(self):
        button_list = [
            tk.Button(
                master=self.frame,
                text="Registrar Ponto",
                width=50,
                # command=
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
            # tk.Button(
            #     master=self.frame, text="Gerenciar Produtos e Servicos", width=50
            # ),
            tk.Button(master=self.frame, text="Registrar Produto", width=50),
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
        self.frame.destroy()
        TelaEstoque(self.window).set_tela()

    def realizar_reserva(self):
        self.frame.destroy()
        TelaReserva(self.window).set_tela()
