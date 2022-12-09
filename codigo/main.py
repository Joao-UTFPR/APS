import tkinter as tk

from tela import Tela


def main():
    window = tk.Tk()
    Tela(window).set_tela_inicial()
    window.mainloop()


if __name__ == "__main__":
    main()
