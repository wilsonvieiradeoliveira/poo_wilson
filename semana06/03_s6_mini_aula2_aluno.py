"""
Mini-desafio — Aula 2

Classe Aluno com @property de nota, validando 0 a 100 (a mesma regra do
curso). Commit sugerido: "@property com validação"
"""


class Aluno:
    def __init__(self, nome, nota=0):
        self.nome = nome
        self.__nota = nota

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nova):
        if 0 <= nova <= 100:
            self.__nota = nova
        else:
            print(f"Nota inválida ({nova}): precisa estar entre 0 e 100.")


aluno = Aluno("Marina")
print(f"Nota inicial de {aluno.nome}: {aluno.nota}")

aluno.nota = 87
print(f"Depois de aluno.nota = 87: {aluno.nota}")

aluno.nota = 150
print(f"Depois de aluno.nota = 150 (deve continuar 87): {aluno.nota}")

aluno.nota = -10
print(f"Depois de aluno.nota = -10 (deve continuar 87): {aluno.nota}")
