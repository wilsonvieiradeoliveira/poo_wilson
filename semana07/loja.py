"""
Trabalho da semana 7 — Lojinha com classe Produto (10 pts)

Evolução do 06_loja.py da semana 6 (que só tinha __preco como property):
- Aula 1: __estoque entra como segunda property protegida, também recusando
  valores negativos, e exibir() formata o preço com R$ e duas casas (:.2f).
- Aula 2: vender(qtd) e repor(qtd) com validação de quantidade e estoque
  suficiente, cada recusa com sua própria mensagem, e vender() devolvendo
  True/False para quem chamou saber se a venda aconteceu.
- Aula 3: menu da lojinha (cadastrar, listar, vender, repor, sair), na mesma
  arquitetura do arena.py da semana 5 — catalogo = [] no lugar de
  personagens = [], escolha de produto pelo número (com o -1 de sempre).
- Aula 4: validações de borda (catálogo vazio, opção inválida, número fora
  da lista) e o extra valor_total_do_estoque() — o mesmo Produto usado aqui
  vai direto para o Projeto Integrador em Flask.
"""


class Produto:
    def __init__(self, nome, preco, estoque=0):
        self.nome = nome
        self.__preco = 0
        self.__estoque = 0
        self.preco = preco  # já passa pelo setter na criação
        self.estoque = estoque

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor >= 0:
            self.__preco = valor
        else:
            print(f"Preço inválido ({valor}): não pode ser negativo.")

    @property
    def estoque(self):
        return self.__estoque

    @estoque.setter
    def estoque(self, valor):
        if valor >= 0:
            self.__estoque = valor
        else:
            print(f"Estoque inválido ({valor}): não pode ser negativo.")

    def exibir(self):
        print(f"{self.nome} | R$ {self.preco:.2f} | estoque: {self.estoque}")

    def vender(self, qtd):
        if qtd <= 0:
            print(f"Quantidade inválida ({qtd}): a venda precisa ser de uma quantidade positiva.")
            return False
        if qtd > self.__estoque:
            print(f"Estoque insuficiente para vender {qtd} de {self.nome} (disponível: {self.__estoque}).")
            return False
        self.__estoque -= qtd
        print(f"Venda de {qtd} {self.nome} confirmada. Estoque restante: {self.__estoque}.")
        return True

    def repor(self, qtd):
        if qtd <= 0:
            print(f"Quantidade inválida ({qtd}): a reposição precisa ser de uma quantidade positiva.")
            return
        self.__estoque += qtd
        print(f"Reposição de {qtd} {self.nome} confirmada. Estoque atual: {self.__estoque}.")


produto = Produto("Caderno", 12.5, 10)
produto.exibir()

print("\nTeste dos 4 cenários de vender()/repor():")
produto.repor(5)      # repor válido
produto.repor(-2)     # repor inválido
produto.vender(3)     # vender válido
produto.vender(999)   # vender sem estoque suficiente

# TODO (aula 3): menu da lojinha (cadastrar, listar, vender, repor, sair).
