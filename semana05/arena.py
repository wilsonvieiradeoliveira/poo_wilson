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


while True:
    opcao = input("1 Criar  2 Listar  3 Batalha  4 Sair: ").strip()
    if opcao == "1":
        criar_personagem()
    elif opcao == "2":
        listar_personagens()
    elif opcao == "3":
        if len(personagens) < 2:
            print("Crie pelo menos 2 personagens antes de batalhar.")
    elif opcao == "4":
        print("Até a próxima!")
        break
    else:
        print("Opção inválida. Escolha 1, 2, 3 ou 4.")
