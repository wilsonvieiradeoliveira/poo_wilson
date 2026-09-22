"""Banco de palavras usado pelo jogo da forca."""

from random import Random


PALAVRAS = (
    ("ANIMAIS", "GIRAFA"),
    ("ANIMAIS", "TARTARUGA"),
    ("ANIMAIS", "PINGUIM"),
    ("ANIMAIS", "BORBOLETA"),
    ("ALIMENTOS", "ABACAXI"),
    ("ALIMENTOS", "CHOCOLATE"),
    ("ALIMENTOS", "PÃO DE QUEIJO"),
    ("ALIMENTOS", "AÇAÍ"),
    ("LUGARES", "BIBLIOTECA"),
    ("LUGARES", "CACHOEIRA"),
    ("LUGARES", "PRAÇA"),
    ("LUGARES", "AEROPORTO"),
    ("TECNOLOGIA", "COMPUTADOR"),
    ("TECNOLOGIA", "TECLADO"),
    ("TECNOLOGIA", "PROGRAMAÇÃO"),
    ("TECNOLOGIA", "ROBÔ"),
    ("NATUREZA", "ARCO-ÍRIS"),
    ("NATUREZA", "OCEANO"),
    ("NATUREZA", "MONTANHA"),
    ("NATUREZA", "ÁRVORE"),
)


class BancoDePalavras:
    """Fornece palavras aleatórias e evita repetição enquanto for possível."""

    def __init__(self, palavras=PALAVRAS, sorteador=None):
        if not palavras:
            raise ValueError("O banco de palavras não pode estar vazio.")

        self._palavras = tuple(palavras)
        self._sorteador = sorteador or Random()
        self._disponiveis = []

    def sortear(self):
        if not self._disponiveis:
            self._disponiveis = list(self._palavras)
            self._sorteador.shuffle(self._disponiveis)

        categoria, palavra = self._disponiveis.pop()
        return categoria, palavra
