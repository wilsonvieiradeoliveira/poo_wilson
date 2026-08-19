produtos = [
    {"nome": "Mouse gamer", "preco": 89.90},
    {"nome": "Headset", "preco": 149.90},
    {"nome": "Teclado mecânico", "preco": 199.00},
]
 
for p in produtos:
    print(f'{p["nome"]}: R$ {p["preco"]}')
