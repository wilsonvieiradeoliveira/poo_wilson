class Personagem:
    def __init__(self, nome, ataque=15):
        self.nome = nome
        self.vida = 100
        self.ataque = ataque

    def atacar(self, alvo):
        alvo.vida -= self.ataque

    def esta_vivo(self):
        return self.vida > 0

    def status(self):
        vivo = "vivo" if self.esta_vivo() else "derrotado"
        print(f"{self.nome} - vida: {max(0, self.vida)} - ataque: {self.ataque} - {vivo}")


personagens = []


def barra_vida(vida, vida_maxima=100, tamanho=20):
    vida_exibida = max(0, vida)
    preenchido = int(tamanho * vida_exibida / vida_maxima)
    return f"[{'#' * preenchido}{'-' * (tamanho - preenchido)}] {vida_exibida}/{vida_maxima}"


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
        print(f"{posicao} - {p.nome} (vida: {max(0, p.vida)})")
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

    return personagens[num1 - 1], personagens[num2 - 1]  # o famoso -1


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
