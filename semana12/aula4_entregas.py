# Aula 4 — Consolidação: prazos de entrega do delivery


class Entrega:
    def __init__(self, pedido):
        self.pedido = pedido

    def prazo(self):
        return "3 dias"


class Moto(Entrega):
    def prazo(self):
        return "40 minutos"


class Bicicleta(Entrega):
    def prazo(self):
        return "1 hora"


class Correio(Entrega):  # usa o prazo da mãe
    pass


def informar(entrega):  # não sabe (nem precisa saber) qual é o tipo
    print(f"Pedido {entrega.pedido}: chega em {entrega.prazo()}")


entregas = [Moto(101), Bicicleta(102), Correio(103)]
for e in entregas:
    informar(e)
