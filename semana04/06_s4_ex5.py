class Perfil:
    def __init__(self, usuario):
        self.usuario = usuario
        self.seguidores = 0

    def seguir(self):
        self.seguidores += 1


p = Perfil("ana_dev")
p.seguir()
p.seguir()
p.seguir()
print(f"{p.usuario} tem {p.seguidores} seguidores")
