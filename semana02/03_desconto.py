def preco_com_desconto(preco, percentual):
    desconto = preco * percentual / 100
    return preco - desconto
 
#print(preco_com_desconto(100, 10))   # 45.0
print(preco_com_desconto(89.90, 25))   # 67.425
