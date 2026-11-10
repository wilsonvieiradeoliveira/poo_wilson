# Aula 1 — O PROBLEMA: três classes quase iguais (ainda sem herança)


class Guerreiro:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def mostrar_status(self):
        print(f"{self.nome} | Vida: {self.vida}")

    def golpe_de_espada(self):
        print(f"{self.nome} golpeia com a espada!")


class Mago:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def mostrar_status(self):
        print(f"{self.nome} | Vida: {self.vida}")

    def lancar_magia(self):
        print(f"{self.nome} lança uma bola de fogo!")


class Arqueiro:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def mostrar_status(self):
        print(f"{self.nome} | Vida: {self.vida}")

    def disparar_flecha(self):
        print(f"{self.nome} dispara uma flecha!")


g = Guerreiro("Thor", 120)
m = Mago("Merlin", 80)
a = Arqueiro("Robin", 90)

g.mostrar_status()
m.mostrar_status()
a.mostrar_status()
