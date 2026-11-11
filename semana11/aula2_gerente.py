# Aula 2 — Gerente: estender um cálculo


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

    def calcular_pagamento(self):  # estende o cálculo da mãe
        return super().calcular_pagamento() + self.bonus


ana = Funcionario("Ana", 2500.00)
bia = Gerente("Bia", 5000.00, 1000.00)
ana.mostrar()
bia.mostrar()
