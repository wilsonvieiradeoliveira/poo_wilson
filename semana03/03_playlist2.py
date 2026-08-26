class Musica:
    def exibir(self):
        print(f"{self.titulo} — {self.artista}")
 
playlist = []
 
def adicionar():
    m = Musica()
    m.titulo = input("Título: ")
    m.artista = input("Artista: ")
    playlist.append(m)
 
def listar():
    if len(playlist) == 0:
        print("Nenhuma música ainda.")
    else:
        for m in playlist:
            m.exibir()
 
while True:
    opcao = input("1 Adicionar  2 Listar  3 Sair: ")
    if opcao == "1":
        adicionar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        break
