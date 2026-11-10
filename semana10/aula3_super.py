# Aula 3 — super(): a filha com um atributo a mais


class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def mostrar_status(self):
        print(f"{self.nome} | Vida: {self.vida}")


class Guerreiro(Personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)  # a mãe cuida de nome e vida
        self.forca = forca            # a filha cuida do que é dela


class Mago(Personagem):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.mana = mana


class Arqueiro(Personagem):
    def __init__(self, nome, vida, flechas):
        super().__init__(nome, vida)
        self.flechas = flechas


g = Guerreiro("Thor", 120, 30)
m = Mago("Merlin", 80, 100)
a = Arqueiro("Robin", 90, 12)

m.mostrar_status()
print(m.mana)
print(g.forca)
print(a.flechas)
