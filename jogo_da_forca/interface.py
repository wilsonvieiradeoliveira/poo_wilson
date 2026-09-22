"""Interface gráfica do jogo da forca."""

import string
import tkinter as tk
from tkinter import messagebox

from jogo import normalizar_letra


class InterfaceJogo:
    COR_FUNDO = "#F5F2EA"
    COR_CARTAO = "#FFFFFF"
    COR_TEXTO = "#253238"
    COR_PRIMARIA = "#176B87"
    COR_ACERTO = "#2E7D32"
    COR_ERRO = "#B23A48"
    COR_NEUTRA = "#DCE4E7"

    def __init__(self, janela, jogo):
        self.janela = janela
        self.jogo = jogo
        self.botoes_letras = {}

        self._configurar_janela()
        self._montar_interface()
        self._vincular_teclado()
        self.atualizar_interface()

    def _configurar_janela(self):
        self.janela.title("Jogo da Forca")
        self.janela.geometry("1000x760")
        self.janela.minsize(820, 680)
        self.janela.configure(bg=self.COR_FUNDO)

    def _montar_interface(self):
        cabecalho = tk.Frame(self.janela, bg=self.COR_PRIMARIA, padx=24, pady=16)
        cabecalho.pack(fill="x")

        tk.Label(
            cabecalho,
            text="JOGO DA FORCA",
            font=("Arial", 28, "bold"),
            bg=self.COR_PRIMARIA,
            fg="white",
        ).pack(side="left")

        self.rotulo_erros = tk.Label(
            cabecalho,
            font=("Arial", 16, "bold"),
            bg=self.COR_PRIMARIA,
            fg="white",
        )
        self.rotulo_erros.pack(side="right")

        conteudo = tk.Frame(self.janela, bg=self.COR_FUNDO, padx=24, pady=18)
        conteudo.pack(fill="both", expand=True)
        conteudo.grid_columnconfigure(0, weight=1)
        conteudo.grid_columnconfigure(1, weight=2)
        conteudo.grid_rowconfigure(0, weight=1)

        quadro_forca = tk.Frame(conteudo, bg=self.COR_CARTAO, padx=10, pady=10)
        quadro_forca.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
        self.canvas = tk.Canvas(
            quadro_forca,
            width=320,
            height=340,
            bg=self.COR_CARTAO,
            highlightthickness=0,
        )
        self.canvas.pack(expand=True)

        painel = tk.Frame(conteudo, bg=self.COR_CARTAO, padx=22, pady=18)
        painel.grid(row=0, column=1, sticky="nsew", padx=(12, 0))

        self.rotulo_categoria = tk.Label(
            painel,
            font=("Arial", 16, "bold"),
            bg=self.COR_CARTAO,
            fg=self.COR_PRIMARIA,
        )
        self.rotulo_categoria.pack(pady=(4, 18))

        self.rotulo_palavra = tk.Label(
            painel,
            font=("Courier New", 34, "bold"),
            bg=self.COR_CARTAO,
            fg=self.COR_TEXTO,
            wraplength=560,
            justify="center",
        )
        self.rotulo_palavra.pack(fill="x", pady=(12, 20))

        self.rotulo_mensagem = tk.Label(
            painel,
            text="Escolha uma letra",
            font=("Arial", 17, "bold"),
            bg=self.COR_CARTAO,
            fg=self.COR_TEXTO,
            wraplength=540,
        )
        self.rotulo_mensagem.pack(pady=(0, 12))

        self.rotulo_usadas = tk.Label(
            painel,
            font=("Arial", 14),
            bg=self.COR_CARTAO,
            fg="#52636B",
        )
        self.rotulo_usadas.pack(pady=(0, 18))

        teclado = tk.Frame(painel, bg=self.COR_CARTAO)
        teclado.pack(expand=True)
        for indice, letra in enumerate(string.ascii_uppercase):
            botao = tk.Button(
                teclado,
                text=letra,
                width=3,
                height=1,
                font=("Arial", 16, "bold"),
                bg=self.COR_NEUTRA,
                fg=self.COR_TEXTO,
                activebackground="#B8DCE7",
                relief="flat",
                cursor="hand2",
                command=lambda escolha=letra: self.jogar(escolha),
            )
            botao.grid(row=indice // 7, column=indice % 7, padx=4, pady=4)
            self.botoes_letras[letra] = botao

        rodape = tk.Frame(self.janela, bg=self.COR_FUNDO, padx=24)
        rodape.pack(fill="x", pady=(0, 18))
        tk.Button(
            rodape,
            text="NOVA PARTIDA",
            font=("Arial", 17, "bold"),
            bg=self.COR_PRIMARIA,
            fg="white",
            activebackground="#12566C",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=24,
            pady=10,
            command=self.nova_partida,
        ).pack()

    def _vincular_teclado(self):
        self.janela.bind("<Key>", self._ao_pressionar_tecla)

    def _ao_pressionar_tecla(self, evento):
        if evento.char and evento.char.isalpha():
            self.jogar(evento.char)

    def jogar(self, letra):
        resultado = self.jogo.tentar_letra(letra)
        if resultado == "invalida":
            return
        if resultado == "repetida":
            self.rotulo_mensagem.config(text=f"A letra {letra.upper()} já foi usada.", fg=self.COR_TEXTO)
            return

        self.atualizar_interface()
        if self.jogo.venceu:
            self.rotulo_mensagem.config(text="Você venceu! Parabéns!", fg=self.COR_ACERTO)
            messagebox.showinfo("Vitória!", f"Parabéns! A palavra era {self.jogo.palavra}.")
        elif self.jogo.perdeu:
            self.rotulo_palavra.config(text=" ".join(self.jogo.palavra))
            self.rotulo_mensagem.config(text=f"Fim de jogo! A palavra era {self.jogo.palavra}.", fg=self.COR_ERRO)
            messagebox.showinfo("Fim de jogo", f"A palavra era {self.jogo.palavra}.")
        elif resultado == "correta":
            self.rotulo_mensagem.config(text="Boa! Essa letra está na palavra.", fg=self.COR_ACERTO)
        else:
            self.rotulo_mensagem.config(text="Essa letra não está na palavra.", fg=self.COR_ERRO)

    def nova_partida(self):
        self.jogo.nova_partida()
        self.rotulo_mensagem.config(text="Escolha uma letra", fg=self.COR_TEXTO)
        self.atualizar_interface()

    def atualizar_interface(self):
        self.rotulo_categoria.config(text=f"CATEGORIA: {self.jogo.categoria}")
        self.rotulo_palavra.config(text=self.jogo.palavra_oculta)
        self.rotulo_erros.config(text=f"ERROS: {self.jogo.erros}/{self.jogo.maximo_erros}")

        usadas = "  ".join(sorted(self.jogo.letras_tentadas)) or "—"
        self.rotulo_usadas.config(text=f"Letras usadas: {usadas}")

        for letra, botao in self.botoes_letras.items():
            if letra not in self.jogo.letras_tentadas:
                botao.config(state="normal", bg=self.COR_NEUTRA, fg=self.COR_TEXTO)
            else:
                acertou = any(
                    caractere.isalpha() and normalizar_letra(caractere) == letra
                    for caractere in self.jogo.palavra
                )
                cor = self.COR_ACERTO if acertou else self.COR_ERRO
                botao.config(state="disabled", disabledforeground="white", bg=cor)

        if self.jogo.terminou:
            for botao in self.botoes_letras.values():
                botao.config(state="disabled")

        self._desenhar_forca()

    def _desenhar_forca(self):
        self.canvas.delete("all")
        cor = self.COR_TEXTO
        largura = 6

        # Estrutura da forca.
        self.canvas.create_line(35, 315, 285, 315, fill=cor, width=largura)
        self.canvas.create_line(85, 315, 85, 35, fill=cor, width=largura)
        self.canvas.create_line(82, 38, 235, 38, fill=cor, width=largura)
        self.canvas.create_line(232, 38, 232, 75, fill=cor, width=4)
        self.canvas.create_line(85, 85, 130, 38, fill=cor, width=4)

        partes = (
            lambda: self.canvas.create_oval(202, 75, 262, 135, outline=cor, width=largura),
            lambda: self.canvas.create_line(232, 135, 232, 225, fill=cor, width=largura),
            lambda: self.canvas.create_line(232, 155, 192, 195, fill=cor, width=largura),
            lambda: self.canvas.create_line(232, 155, 272, 195, fill=cor, width=largura),
            lambda: self.canvas.create_line(232, 225, 197, 280, fill=cor, width=largura),
            lambda: self.canvas.create_line(232, 225, 267, 280, fill=cor, width=largura),
        )
        for desenhar in partes[: self.jogo.erros]:
            desenhar()
