"""
Exercício 7 — ContaBancaria completa (s6_ex7)

O saldo é property somente-leitura (sem setter): só muda por depositar()
ou sacar(), igual a um banco de verdade (Missão 2 da aula 4). Tentar
"conta.saldo = 999999" gera AttributeError: can't set attribute.
"""


class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False


conta = ContaBancaria(input("Nome do titular: ").strip() or "Titular")

while True:
    opcao = input("1 Depositar  2 Sacar  3 Ver saldo  4 Sair: ").strip()
    if opcao == "1":
        valor_texto = input("Valor a depositar: ").strip()
        try:
            valor = float(valor_texto)
        except ValueError:
            print("Digite um número válido.")
            continue
        if conta.depositar(valor):
            print(f"Depósito de {valor:.2f} realizado. Saldo: {conta.saldo:.2f}")
        else:
            print("Valor de depósito precisa ser maior que zero.")
    elif opcao == "2":
        valor_texto = input("Valor a sacar: ").strip()
        try:
            valor = float(valor_texto)
        except ValueError:
            print("Digite um número válido.")
            continue
        if conta.sacar(valor):
            print(f"Saque de {valor:.2f} realizado. Saldo: {conta.saldo:.2f}")
        else:
            print("Saque negado: valor inválido ou maior que o saldo.")
    elif opcao == "3":
        print(f"Saldo atual: {conta.saldo:.2f}")
    elif opcao == "4":
        print("Até a próxima!")
        break
    else:
        print("Opção inválida. Escolha 1, 2, 3 ou 4.")
