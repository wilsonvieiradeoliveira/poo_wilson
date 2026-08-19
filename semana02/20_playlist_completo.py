playlist = []


def adicionar():
    titulo = input("Título: ")
    artista = input("Artista: ")
    playlist.append({"titulo": titulo, "artista": artista})


def listar():
    if len(playlist) == 0:
        print("Nenhuma música ainda.")
    else:
        for m in playlist:
            print(f"{m['titulo']} — {m['artista']}")


def remover():
    titulo = input("Título da música a remover: ")
    for m in playlist:
        if m["titulo"] == titulo:
            playlist.remove(m)
            print("Removida!")
            return
    print("Música não encontrada.")


while True:
    print(f"Sua playlist tem {len(playlist)} músicas")
    opcao = input("1 Adicionar  2 Listar  3 Remover  4 Sair: ")
    if opcao == "1":
        adicionar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        remover()
    elif opcao == "4":
        break
