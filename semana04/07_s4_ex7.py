# MINI-DESAFIO — Aula 2
# Aluno(nome, pontos=0) + ganhar_pontos(qtd) + situacao() usando a regra dos 60 pontos.


class Aluno:
    def __init__(self, nome, pontos=0):
        self.nome = nome
        self.pontos = pontos

    def ganhar_pontos(self, qtd):
        self.pontos += qtd

    def situacao(self):
        if self.pontos >= 60:
            print(f"{self.nome}: aprovado ({self.pontos} pontos)")
        else:
            print(f"{self.nome}: em recuperação ({self.pontos} pontos)")


a1 = Aluno("Ana", 45)
a2 = Aluno("Bruno")

a1.situacao()
a1.ganhar_pontos(20)
a1.situacao()

a2.situacao()
a2.ganhar_pontos(65)
a2.situacao()
