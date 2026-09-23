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


produto = Produto("Caderno", 12.5, 10)
produto.exibir()

print("\nTeste de trapaça:")
produto.preco = -10
produto.estoque = -5
Produto("Caneta inválida", -10)
produto.exibir()

# TODO (aula 2): vender(qtd) e repor(qtd) com validação de quantidade e
# estoque suficiente, cada recusa com sua própria mensagem.
