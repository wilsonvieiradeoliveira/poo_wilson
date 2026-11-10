# Aula 2 — A classe mãe e a primeira classe filha


class Personagem:  # classe MÃE: tudo o que é comum
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def mostrar_status(self):
        print(f"{self.nome} | Vida: {self.vida}")


class Mago(Personagem):  # Mago É UM Personagem
    def lancar_magia(self):
        print(f"{self.nome} lança uma bola de fogo!")


class Guerreiro(Personagem):  # Guerreiro É UM Personagem
    def golpe_de_espada(self):
        print(f"{self.nome} golpeia com a espada!")

class Arqueiro(Personagem):  # Arqueiro É UM Personagem
    def disparar_flecha(self):
        print(f"{self.nome} dispara uma flecha!")



m = Mago("Merlin", 80)
g = Guerreiro("Thor", 120)
a = Arqueiro("Legolas", 100)

m.mostrar_status()   # veio da mãe
m.lancar_magia()     # é só do Mago
g.mostrar_status()   # veio da mãe
g.golpe_de_espada()  # é só do Guerreiro
a.mostrar_status()   # veio da mãe
a.disparar_flecha()  # é só do Arqueiro
