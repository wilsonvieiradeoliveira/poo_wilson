# Aula 3 — Uma lista de objetos dentro de outro: o pedido TEM itens


class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []  # o pedido TEM uma lista de itens

    def adicionar(self, item):
        self.itens.append(item)

    def total(self):
        soma = 0
        for item in self.itens:
            soma = soma + item.preco
        return soma


pedido = Pedido("Lia")
pedido.adicionar(Item("X-Burguer", 18.00))
pedido.adicionar(Item("Suco", 7.00))
print(len(pedido.itens))
print(f"Total: R$ {pedido.total():.2f}")
