# Aula 5 — O carrinho da lojinha TEM produtos


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Carrinho:
    def __init__(self):
        self.produtos = []  # o carrinho TEM uma lista de produtos

    def adicionar(self, produto):
        self.produtos.append(produto)

    def total(self):
        soma = 0
        for produto in self.produtos:
            soma = soma + produto.preco
        return soma


carrinho = Carrinho()
carrinho.adicionar(Produto("Caneca Gamer", 35.00))
carrinho.adicionar(Produto("Fone Bluetooth", 89.90))
print(len(carrinho.produtos))
print(f"Total: R$ {carrinho.total():.2f}")
