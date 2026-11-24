# Aula 2 — Objeto dentro de objeto: o guerreiro TEM uma arma


class Arma:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

    def descrever(self):
        return f"{self.nome} (dano {self.dano})"


class Guerreiro:
    def __init__(self, nome, arma):
        self.nome = nome
        self.arma = arma  # o guerreiro TEM uma arma

    def atacar(self):
        print(f"{self.nome} ataca com {self.arma.descrever()}!")


espada = Arma("Espada", 30)
thor = Guerreiro("Thor", espada)
print(thor.arma.dano)
thor.atacar()

machado = Arma("Machado", 45)
thor.arma = machado  # trocar a peça
thor.atacar()
