"""
Exercício 6 — Perfil protegido (s6_ex6)

Classe Perfil com __seguidores como property: o setter recusa números
negativos.
"""


class Perfil:
    def __init__(self, usuario, seguidores=0):
        self.usuario = usuario
        self.__seguidores = seguidores

    @property
    def seguidores(self):
        return self.__seguidores

    @seguidores.setter
    def seguidores(self, novo):
        if novo >= 0:
            self.__seguidores = novo
        else:
            print(f"Valor inválido ({novo}): seguidores não pode ser negativo.")


perfil = Perfil("@aria_dev")
print(f"{perfil.usuario} tem {perfil.seguidores} seguidores")

perfil.seguidores = 1500
print(f"Depois de ganhar seguidores: {perfil.seguidores}")

perfil.seguidores = -200
print(f"Tentativa de deixar negativo (deve continuar 1500): {perfil.seguidores}")
