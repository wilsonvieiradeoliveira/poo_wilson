series = [
    {"nome": "Stranger Things", "nota": 9.0},
    {"nome": "Wandinha", "nota": 8.5},
]
 
busca = input("Nome da série: ")
encontrou = False
for s in series:
    if s["nome"] == busca:
        encontrou = True
 
if encontrou:
    print("Está no catálogo!")
else:
    print("Não está no catálogo.")
