class Personagem:
    total_criados = 0

    def __init__(self, nome, ataque=15):
        self.nome = nome
        self.vida = 100
        self.ataque = ataque
        Personagem.total_criados += 1


p1 = Personagem("Aria")
p2 = Personagem("Dragão", 40)
p3 = Personagem("Goblin", 8)

print(f"Total de personagens criados: {Personagem.total_criados}")
