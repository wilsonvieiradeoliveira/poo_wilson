# Aula 4 — Sobrescrita: a filha faz do jeito dela


class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def mostrar_status(self):
        print(f"{self.nome} | Vida: {self.vida}")

    def atacar(self):
        print(f"{self.nome} dá um soco.")


class Guerreiro(Personagem):
    def atacar(self):  # sobrescreve o atacar() da mãe
        print(f"{self.nome} golpeia com a espada!")


class Mago(Personagem):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.mana = mana

    def atacar(self):  # sobrescreve o atacar() da mãe
        print(f"{self.nome} lança uma bola de fogo!")

    def mostrar_status(self):
        super().mostrar_status()  # aproveita a linha da mãe...
        print(f"   Mana: {self.mana}")  # ...e acrescenta a sua


class Arqueiro(Personagem):  # não sobrescreve nada
    pass


g = Guerreiro("Thor", 120)
m = Mago("Merlin", 80, 100)
a = Arqueiro("Robin", 90)

g.atacar()
m.atacar()
a.atacar()
m.mostrar_status()
