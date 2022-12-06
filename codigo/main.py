import tkinter as tk
from tela_inicial import TelaInicial


def main():
    window = tk.Tk()
    TelaInicial(window).set_tela()
    window.mainloop()


if __name__ == "__main__":
    main()
