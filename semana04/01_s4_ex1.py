class Musica:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def exibir(self):
        print(f"{self.titulo} — {self.artista}")


m1 = Musica("Houdini", "Dua Lipa")
m2 = Musica("Flowers", "Miley Cyrus")
m3 = Musica("Paint The Town Red", "Doja Cat")

m1.exibir()
m2.exibir()
m3.exibir()
