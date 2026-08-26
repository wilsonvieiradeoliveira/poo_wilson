class Perfil:
    def seguir(self):
        self.seguidores += 1
 
p = Perfil()
p.usuario = "ana_dev"
p.seguidores = 0
 
p.seguir()
p.seguir()
p.seguir()
print(f"{p.usuario} tem {p.seguidores} seguidores")
