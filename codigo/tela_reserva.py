import tkinter as tk
from tela import Tela
from postgres import Postgres
import os
import sys

class TelaReserva(Tela):
    def set_tela(self):
        entry_text1 = tk.StringVar()
        entry_text2 = tk.StringVar()
        widget_list = [
            tk.Entry(master=self.frame, textvariable=entry_text1),
            tk.Entry(master=self.frame, textvariable=entry_text2),
            tk.Button(
                master=self.frame, text="Reservar", width=50, command=lambda: self.reservar(widget_list[0].get(), widget_list[1].get())
            ),
            tk.Button(
                master=self.frame, text="Checar Reservas", width=50, command=self.checar_reservas
            ),
            tk.Button(
                master=self.frame, text="Voltar", width=50, command=self.back_to_start
            )
        ]
        for widget in widget_list:
            widget.pack()

        entry_text1.set("nome")
        entry_text2.set("dia_hora")

    def reservar(self, nome, dia_hora):
        Postgres().alter(f"INSERT INTO reserva VALUES('{nome}', '{dia_hora}');")

    def checar_reservas(self):
        self.frame.destroy()
        self.frame = tk.Frame(master=self.window, width=100, height=100)
        self.frame.pack()
        result = Postgres().select("SELECT * FROM reserva")
        reservas = ""
        for nome, dia in result:
            reservas += f"{nome}: {dia}\n"
        label = tk.Label(master=self.frame, text=reservas)
        label.pack()
        button = tk.Button(
            master=self.frame, text="Voltar", width=50, command=self.back
        )
        button.pack()

    def back(self):
        self.frame.destroy()
        TelaReserva(self.window).set_tela()

    def back_to_start(self):
        self.window.destroy()
        window = tk.Tk()
        super().__init__(window)
        super().set_tela_inicial()