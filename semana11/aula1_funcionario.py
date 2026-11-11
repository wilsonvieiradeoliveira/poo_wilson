# Aula 1 — A classe mãe do sistema de RH


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario

    def mostrar(self):
        print(f"{self.nome} - R$ {self.calcular_pagamento():.2f}")


ana = Funcionario("Ana", 2500.00)
ana.mostrar()
