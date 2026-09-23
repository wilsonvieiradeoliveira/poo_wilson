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


catalogo = []


def cadastrar_produto():
    nome = input("Nome do produto: ").strip()
    preco_texto = input("Preço (use ponto para decimais, ex.: 4.50): ").strip()
    try:
        preco = float(preco_texto)
    except ValueError:
        print("Preço inválido. Digite um número usando ponto para decimais (ex.: 4.50).")
        return

    estoque_texto = input("Estoque inicial (Enter para 0): ").strip()
    estoque = int(estoque_texto) if estoque_texto.isdigit() else 0

    catalogo.append(Produto(nome, preco, estoque))
    print(f"{nome} cadastrado!")


def listar_catalogo():
    if len(catalogo) == 0:
        print("Catálogo vazio. Cadastre um produto primeiro.")
        return
    posicao = 1
    for produto in catalogo:
        print(f"{posicao} - ", end="")
        produto.exibir()
        posicao += 1


def escolher_produto():
    listar_catalogo()
    if len(catalogo) == 0:
        return None

    num_texto = input("Número do produto: ").strip()
    if not num_texto.isdigit():
        print("Digite apenas o número da listagem.")
        return None

    num = int(num_texto)
    if not (1 <= num <= len(catalogo)):
        print("Número fora da lista.")
        return None

    return catalogo[num - 1]  # o -1 de sempre


def vender_produto():
    produto = escolher_produto()
    if produto is None:
        return

    qtd_texto = input("Quantidade a vender: ").strip()
    if not qtd_texto.isdigit():
        print("Digite uma quantidade válida.")
        return

    produto.vender(int(qtd_texto))


def repor_produto():
    produto = escolher_produto()
    if produto is None:
        return

    qtd_texto = input("Quantidade a repor: ").strip()
    if not qtd_texto.isdigit():
        print("Digite uma quantidade válida.")
        return

    produto.repor(int(qtd_texto))


while True:
    opcao = input("1 Cadastrar  2 Listar  3 Vender  4 Repor  5 Sair: ").strip()
    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_catalogo()
    elif opcao == "3":
        vender_produto()
    elif opcao == "4":
        repor_produto()
    elif opcao == "5":
        print("Até a próxima!")
        break
    else:
        print("Opção inválida. Escolha 1, 2, 3, 4 ou 5.")
