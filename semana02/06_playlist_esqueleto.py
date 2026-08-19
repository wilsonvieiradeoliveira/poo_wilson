playlist = []
 
def adicionar():
    titulo = input("Título: ")
    artista = input("Artista: ")
    playlist.append({"titulo": titulo, "artista": artista})
 
while True:
    opcao = input("1 Adicionar  2 Listar  3 Sair: ")
    if opcao == "1":
        adicionar()
    elif opcao == "3":
        break
