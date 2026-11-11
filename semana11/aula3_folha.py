# Aula 3 — Estagiário e a folha de pagamento completa


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario

    def mostrar(self):
        print(f"{self.nome} - R$ {self.calcular_pagamento():.2f}")


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def calcular_pagamento(self):  # ESTENDE: usa a mãe e soma
        return super().calcular_pagamento() + self.bonus


class Estagiario(Funcionario):
    def mostrar(self):  # SOBRESCREVE: troca o mostrar inteiro
        print(f"Estagiário {self.nome} - bolsa R$ {self.salario:.2f}")


ana = Funcionario("Ana", 2500.00)
bia = Gerente("Bia", 5000.00, 1000.00)
caio = Estagiario("Caio", 1200.00)

equipe = [ana, bia, caio]
total = 0
for pessoa in equipe:
    pessoa.mostrar()
    total = total + pessoa.calcular_pagamento()

print(f"Total da folha: R$ {total:.2f}")
