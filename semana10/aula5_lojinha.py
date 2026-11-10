# Aula 5 — Herança na lojinha virtual


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def preco_final(self):
        return self.preco

    def mostrar(self):
        print(f"{self.nome} - R$ {self.preco_final():.2f}")


class ProdutoFisico(Produto):  # precisa de entrega
    def __init__(self, nome, preco, frete):
        super().__init__(nome, preco)
        self.frete = frete

    def preco_final(self):
        return self.preco + self.frete


caneca = Produto("Caneca Gamer", 35.00)
fone = ProdutoFisico("Fone Bluetooth", 89.90, 15.00)

caneca.mostrar()
fone.mostrar()
