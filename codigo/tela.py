import tkinter as tk

# from tela_inicial import TelaInicial


class Tela:
    def __init__(self, window):
        self.window = window
        self.frame = tk.Frame(master=self.window, width=100, height=100)
        self.frame.pack()

    # def restart(self):
    #     TelaInicial(self.window).set_tela()
