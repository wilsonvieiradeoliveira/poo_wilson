"""Regras do jogo da forca, independentes da interface gráfica."""

import unicodedata


def normalizar_letra(texto):
    """Converte uma letra acentuada para sua forma básica em maiúscula."""
    sem_acentos = unicodedata.normalize("NFD", texto.upper())
    return "".join(caractere for caractere in sem_acentos if not unicodedata.combining(caractere))


class JogoDaForca:
    """Mantém o estado de uma rodada e aplica suas regras."""

    def __init__(self, banco_de_palavras, maximo_erros=6):
        if maximo_erros <= 0:
            raise ValueError("O máximo de erros deve ser positivo.")

        self.banco_de_palavras = banco_de_palavras
        self.maximo_erros = maximo_erros
        self.categoria = ""
        self.palavra = ""
        self.letras_tentadas = set()
        self.erros = 0
        self.nova_partida()

    def nova_partida(self):
        self.categoria, self.palavra = self.banco_de_palavras.sortear()
        self.palavra = self.palavra.upper()
        self.letras_tentadas = set()
        self.erros = 0

    @property
    def terminou(self):
        return self.venceu or self.perdeu

    @property
    def venceu(self):
        letras_da_palavra = {
            normalizar_letra(caractere)
            for caractere in self.palavra
            if caractere.isalpha()
        }
        return letras_da_palavra.issubset(self.letras_tentadas)

    @property
    def perdeu(self):
        return self.erros >= self.maximo_erros

    @property
    def tentativas_restantes(self):
        return max(0, self.maximo_erros - self.erros)

    @property
    def palavra_oculta(self):
        exibicao = []
        for caractere in self.palavra:
            if not caractere.isalpha() or normalizar_letra(caractere) in self.letras_tentadas:
                exibicao.append(caractere)
            else:
                exibicao.append("_")
        return " ".join(exibicao)

    def tentar_letra(self, letra):
        """Registra uma jogada e retorna: correta, incorreta, repetida ou inválida."""
        letra_normalizada = normalizar_letra(letra.strip())

        if self.terminou or len(letra_normalizada) != 1 or not letra_normalizada.isalpha():
            return "invalida"
        if letra_normalizada in self.letras_tentadas:
            return "repetida"

        self.letras_tentadas.add(letra_normalizada)
        letras_da_palavra = {
            normalizar_letra(caractere)
            for caractere in self.palavra
            if caractere.isalpha()
        }

        if letra_normalizada in letras_da_palavra:
            return "correta"

        self.erros += 1
        return "incorreta"
