class Jogo:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota


jogos = [
    Jogo("Minecraft", 9.5),
    Jogo("Valorant", 8.0),
    Jogo("Hollow Knight", 9.8),
]

for jogo in jogos:
    print(f"{jogo.nome} - nota {jogo.nota}")
