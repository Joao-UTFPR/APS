import tkinter as tk
from tela import Tela
from postgres import Postgres
import os
import sys

class TelaPonto(Tela):
    def set_tela(self):
        button_list = [
            tk.Button(
                master=self.frame,
                text="Bater Ponto",
                width=50,
                command=self.bater_ponto_tela,
            ),
            tk.Button(
                master=self.frame,
                text="checar pontos",
                width=50,
                command=self.checar_ponto_tela
            ),
            tk.Button(
                master=self.frame, text="Voltar", width=50, command=self.back_to_start
            )
        ]
        for button in button_list:
            button.pack()


    def bater_ponto_tela(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        entry_text1 = tk.StringVar()
        entry1 = tk.Entry(master=self.frame, textvariable=entry_text1)
        entry_text1.set("nome")
        entry1.pack()
        button = tk.Button(
            master=self.frame, text="alterar", width=50, command=lambda: self.bater(entry1.get())
        )
        voltar = tk.Button(
            master=self.frame, text="Voltar", width=50, command=self.back
        )
        button.pack()
        voltar.pack()

    def bater(self, nome):
        Postgres().alter(f"INSERT INTO ponto VALUES(NOW(), '{nome}');")
        self.back()

    def checar_ponto_tela(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        result = Postgres().select("SELECT * FROM ponto")
        pontos = ""
        for horario, pessoa in result:
            pontos += f"{pessoa}: {horario}\n"
        label = tk.Label(master=self.frame, text=pontos)
        label.pack()
        button = tk.Button(
            master=self.frame, text="Voltar", width=50, command=self.back
        )
        button.pack()

    def back(self):
        self.frame.destroy()
        TelaPonto(self.window).set_tela()

    def back_to_start(self):
        self.window.destroy()
        window = tk.Tk()
        super().__init__(window)
        super().set_tela_inicial()