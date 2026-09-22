"""
Arena v2 — versão blindada com encapsulamento

Evolução do arena.py da semana 5, feita ao longo da semana 6:
- Exercício 2 (s6_ex2): vida virou __vida — o cadeado quebrou o acesso
  direto (listar_personagens e barra_vida paravam de funcionar até virem
  para dentro da classe/usarem a property).
- Exercícios 3 e 4 (s6_ex3, s6_ex4): __vida e __ataque viraram @property
  com validação (vida 0-100, ataque 1-50).
- Exercício 5 (s6_ex5): as duas properties juntas na mesma classe — o
  placar volta a usar heroi.vida normalmente, sem saber que existe cadeado.
- Missão 1 (aula 4): atacar() usa max(0, ...) para a vida nunca ficar
  negativa, e a função teste_de_trapaca() repete as 3 trapaças da aula 1
  para provar que agora todas falham.
"""


class Personagem:
    def __init__(self, nome, ataque=15):
        self.nome = nome
        self.__vida = 100
        self.__ataque = ataque

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, nova):
        if 0 <= nova <= 100:
            self.__vida = nova

    @property
    def ataque(self):
        return self.__ataque

    @ataque.setter
    def ataque(self, novo):
        if 1 <= novo <= 50:
            self.__ataque = novo

    def atacar(self, alvo):
        alvo.vida = max(0, alvo.vida - self.__ataque)

    def esta_vivo(self):
        return self.vida > 0

    def status(self):
        vivo = "vivo" if self.esta_vivo() else "derrotado"
        print(f"{self.nome} - vida: {self.vida} - ataque: {self.ataque} - {vivo}")


personagens = []


def barra_vida(vida, vida_maxima=100, tamanho=20):
    preenchido = int(tamanho * vida / vida_maxima)
    return f"[{'#' * preenchido}{'-' * (tamanho - preenchido)}] {vida}/{vida_maxima}"


def criar_personagem():
    nome = input("Nome do personagem: ").strip()
    ataque_texto = input("Ataque (Enter para usar o padrão 15): ").strip()
    if ataque_texto.isdigit():
        personagens.append(Personagem(nome, int(ataque_texto)))
    else:
        personagens.append(Personagem(nome))
    print(f"{nome} foi criado!")


def listar_personagens():
    if len(personagens) == 0:
        print("Nenhum personagem criado ainda.")
        return
    posicao = 1
    for p in personagens:
        print(f"{posicao} - {p.nome} (vida: {p.vida})")
        posicao += 1


def escolher_lutadores():
    listar_personagens()
    num1_texto = input("Número do 1º lutador: ").strip()
    num2_texto = input("Número do 2º lutador: ").strip()

    if not (num1_texto.isdigit() and num2_texto.isdigit()):
        print("Digite apenas números da listagem.")
        return None

    num1, num2 = int(num1_texto), int(num2_texto)
    if not (1 <= num1 <= len(personagens)) or not (1 <= num2 <= len(personagens)):
        print("Número fora da lista.")
        return None
    if num1 == num2:
        print("Escolha dois personagens diferentes.")
        return None

    return personagens[num1 - 1], personagens[num2 - 1]


def batalha():
    if len(personagens) < 2:
        print("Crie pelo menos 2 personagens antes de batalhar.")
        return

    escolha = escolher_lutadores()
    if escolha is None:
        return
    lutador1, lutador2 = escolha

    print(f"\n=== {lutador1.nome} vs {lutador2.nome} ===")
    while lutador1.esta_vivo() and lutador2.esta_vivo():
        lutador1.atacar(lutador2)
        print(f"{lutador1.nome} atacou {lutador2.nome}!")
        if not lutador2.esta_vivo():
            print(f"\n{lutador1.nome} venceu!")
            break

        lutador2.atacar(lutador1)
        print(f"{lutador2.nome} atacou {lutador1.nome}!")
        if not lutador1.esta_vivo():
            print(f"\n{lutador2.nome} venceu!")
            break

        print(f"{lutador1.nome}: {barra_vida(lutador1.vida)}")
        print(f"{lutador2.nome}: {barra_vida(lutador2.vida)}\n")


def teste_de_trapaca():
    print("=== Teste de trapaça (Missão 1, aula 4) ===")
    heroi = Personagem("Aria")
    vilao = Personagem("Sombra")

    print("\nTrapaça 1: heroi.vida = 999999")
    heroi.vida = 999999
    print(f"vida continua {heroi.vida} -> bloqueada pelo setter (0 <= nova <= 100)")

    print("\nTrapaça 2: vilao.ataque = 0")
    vilao.ataque = 0
    print(f"ataque continua {vilao.ataque} -> bloqueada pelo setter (1 <= novo <= 50)")

    print("\nTrapaça 3: heroi.vida = -50")
    heroi.vida = -50
    print(f"vida continua {heroi.vida} -> bloqueada pelo setter (0 <= nova <= 100)")
    print("\n=== As 3 trapaças da aula 1 falharam. Arena blindada. ===\n")


#teste_de_trapaca()

while True:
    opcao = input("1 Criar  2 Listar  3 Batalha  4 Sair: ").strip()
    if opcao == "1":
        criar_personagem()
    elif opcao == "2":
        listar_personagens()
    elif opcao == "3":
        batalha()
    elif opcao == "4":
        print("Até a próxima!")
        break
    else:
        print("Opção inválida. Escolha 1, 2, 3 ou 4.")
