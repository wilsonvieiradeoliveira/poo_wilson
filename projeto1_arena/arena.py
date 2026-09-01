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
        print(f"{self.nome} - vida: {self.vida} - ataque: {self.ataque} - {vivo}")


personagens = []


def criar_personagem():
    nome = input("Nome do personagem: ").strip()
    ataque_txt = input("Ataque (Enter para usar o padrão 15): ").strip()
    if ataque_txt.isdigit():
        personagens.append(Personagem(nome, int(ataque_txt)))
    else:
        personagens.append(Personagem(nome))
    print(f"{nome} criado!")


def listar_personagens():
    if len(personagens) == 0:
        print("Nenhum personagem criado ainda.")
        return
    for i, p in enumerate(personagens):
        print(f"{i} - ", end="")
        p.status()


def escolher_personagem(mensagem):
    while True:
        listar_personagens()
        indice = input(mensagem).strip()
        if indice.isdigit() and int(indice) < len(personagens):
            return personagens[int(indice)]
        print("Índice inválido, tente novamente.")


def batalha():
    if len(personagens) < 2:
        print("Crie pelo menos 2 personagens antes de batalhar.")
        return

    lutador1 = escolher_personagem("Índice do 1º personagem: ")
    lutador2 = escolher_personagem("Índice do 2º personagem: ")

    # a arena cura os dois antes de cada luta
    lutador1.vida = 100
    lutador2.vida = 100

    while lutador1.esta_vivo() and lutador2.esta_vivo():
        lutador1.atacar(lutador2)
        print(f"{lutador1.nome} atacou {lutador2.nome}!")
        if not lutador2.esta_vivo():
            print(f"{lutador1.nome} venceu!")
            break
        lutador2.atacar(lutador1)
        print(f"{lutador2.nome} atacou {lutador1.nome}!")
        if not lutador1.esta_vivo():
            print(f"{lutador2.nome} venceu!")
            break


while True:
    print()
    opcao = input("1 Criar personagem  2 Listar  3 Batalha  4 Sair: ").strip()
    if opcao == "1":
        criar_personagem()
    elif opcao == "2":
        listar_personagens()
    elif opcao == "3":
        batalha()
    elif opcao == "4":
        break
