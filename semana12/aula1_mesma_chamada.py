# Aula 1 — Mesma chamada, respostas diferentes


class Animal:
    def falar(self):
        print("...")


class Cachorro(Animal):
    def falar(self):
        print("Au au!")


class Gato(Animal):
    def falar(self):
        print("Miau!")


class Vaca(Animal):
    def falar(self):
        print("Muuu!")


bichos = [Cachorro(), Gato(), Vaca()]
for bicho in bichos:
    bicho.falar()  # a MESMA chamada para todos
