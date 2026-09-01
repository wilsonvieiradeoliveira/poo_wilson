class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir(self):
        print(f"{self.nome}: R$ {self.preco}")

    def aplicar_desconto(self, pct):
        desconto = self.preco * pct / 100
        self.preco -= desconto


p1 = Produto("Mouse gamer", 89.90)
p2 = Produto("Headset", 149.90)

p1.exibir()
p1.aplicar_desconto(10)
p1.exibir()

p2.exibir()
p2.aplicar_desconto(20)
p2.exibir()
