"""
Esqueleto do trabalho da semana 7 — classe Produto

Mini-desafio da aula 3: __preco como property que recusa preço negativo.
Este arquivo é só o ponto de partida — __estoque, vender(qtd), repor(qtd)
e o menu completo da lojinha entram no trabalho da semana 7 (10 pts).
Commit sugerido: "@property na Arena"
"""


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = 0
        self.preco = preco  # já passa pelo setter na criação

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo):
        if novo >= 0:
            self.__preco = novo
        else:
            print(f"Preço inválido ({novo}): não pode ser negativo.")


produto = Produto("Caderno", 12.5)
print(f"{produto.nome}: R$ {produto.preco:.2f}")

produto.preco = -5
print(f"Depois de tentar preco = -5 (deve continuar 12.50): R$ {produto.preco:.2f}")

produto.preco = 15.9
print(f"Depois de preco = 15.9: R$ {produto.preco:.2f}")

# TODO (semana 7): __estoque protegido por @property (nunca negativo),
# vender(qtd) e repor(qtd) com validação, e o menu da lojinha
# (cadastrar, listar catálogo, vender, repor, sair).
