"""Ponto de entrada do Jogo da Forca."""

import tkinter as tk

from interface import InterfaceJogo
from jogo import JogoDaForca
from palavras import BancoDePalavras


def main():
    janela = tk.Tk()
    jogo = JogoDaForca(BancoDePalavras())
    InterfaceJogo(janela, jogo)
    janela.mainloop()


if __name__ == "__main__":
    main()
