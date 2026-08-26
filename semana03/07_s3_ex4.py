class Produto:
    def exibir(self):
        print(f"{self.nome}: R$ {self.preco}")
 
    def aplicar_desconto(self, pct):
        desconto = self.preco * pct / 100
        self.preco -= desconto
 
p1 = Produto()
p1.nome = "Mouse gamer"
p1.preco = 89.90
 
p2 = Produto()
p2.nome = "Headset"
p2.preco = 149.90
 
p1.exibir()
p1.aplicar_desconto(10)
p1.exibir()
p2.exibir()
p2.aplicar_desconto(20)
p2.exibir()
