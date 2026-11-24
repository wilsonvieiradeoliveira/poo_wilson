# Aula 4 — Consolidação: a playlist TEM músicas


class Musica:
    def __init__(self, titulo, minutos):
        self.titulo = titulo
        self.minutos = minutos


class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar(self, musica):
        self.musicas.append(musica)

    def listar(self):
        for musica in self.musicas:
            print(f"- {musica.titulo}")

    def duracao(self):
        soma = 0
        for musica in self.musicas:
            soma = soma + musica.minutos
        return soma


treino = Playlist("Treino")
treino.adicionar(Musica("Ritmo Forte", 3))
treino.adicionar(Musica("Sem Parar", 4))
treino.adicionar(Musica("Final", 5))
treino.listar()
print(f"Duração: {treino.duracao()} minutos")
