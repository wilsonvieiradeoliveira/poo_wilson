class Produto:
    pass
 
p1 = Produto()
p1.nome = "Mouse gamer"
p1.preco = 89.90
 
p2 = Produto()
p2.nome = "Headset"
p2.preco = 149.90
 
p3 = Produto()
p3.nome = "Teclado"
p3.preco = 199.00
 
catalogo = [p1, p2, p3]
for produto in catalogo:
    print(f"{produto.nome}: R$ {produto.preco}")
