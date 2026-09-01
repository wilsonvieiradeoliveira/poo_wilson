# MINI-DESAFIO — Aula 3 — Desafio extra 2: Matrículas automáticas
# O contador de classe alimenta a matrícula (atributo de instância) de cada aluno.


class Aluno:
    total_criados = 0  # de CLASSE: contador compartilhado

    def __init__(self, nome):
        Aluno.total_criados += 1
        self.nome = nome
        self.matricula = Aluno.total_criados  # de INSTÂNCIA: única de cada aluno


a1 = Aluno("Ana")
a2 = Aluno("Bruno")
a3 = Aluno("Carla")

for aluno in [a1, a2, a3]:
    print(f"Matrícula {aluno.matricula}: {aluno.nome}")
