# MINI-DESAFIO — Aula 1
# Provocar de propósito o TypeError de argumento faltando no s4_ex2.


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir(self):
        print(f"{self.nome}: R$ {self.preco}")


# Esquecendo o argumento "preco" de propósito:
p1 = Produto("Mouse gamer")
p1.exibir()

# Mensagem de erro copiada da execução:
# TypeError: Produto.__init__() missing 1 required positional argument: 'preco'
#
# Tradução: o Python cobra na hora da criação do objeto, e não deixa
# passar batido — muito melhor que descobrir o erro só quando algum
# código tentar usar p1.preco lá na frente.
