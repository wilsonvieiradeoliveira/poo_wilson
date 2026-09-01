# MINI-DESAFIO — Aula 3 — Desafio extra 1: Desconto padrão
# aplicar_desconto() usa Produto.desconto_padrao quando o percentual não é informado.


class Produto:
    desconto_padrao = 5  # de CLASSE: regra igual pra todo produto, salvo indicação contrária

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir(self):
        print(f"{self.nome}: R$ {self.preco}")

    def aplicar_desconto(self, pct=None):
        if pct is None:
            pct = Produto.desconto_padrao
        desconto = self.preco * pct / 100
        self.preco -= desconto


p1 = Produto("Mouse gamer", 89.90)
p2 = Produto("Headset", 149.90)

p1.exibir()
p1.aplicar_desconto()  # usa o desconto padrão (5%)
p1.exibir()

p2.exibir()
p2.aplicar_desconto(20)  # percentual informado, ignora o padrão
p2.exibir()
