# Aula 4 — Código do treino (mesmo formato do trabalho)


class Pedido:
    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor

    def total(self):
        return self.valor

    def mostrar(self):
        print(f"{self.cliente} - R$ {self.total():.2f}")


class PedidoDelivery(Pedido):
    def __init__(self, cliente, valor, taxa):
        super().__init__(cliente, valor)
        self.taxa = taxa

    def total(self):
        return super().total() + self.taxa


class PedidoBalcao(Pedido):
    pass


p1 = PedidoBalcao("Lia", 30.00)
p2 = PedidoDelivery("Rui", 30.00, 8.00)
p1.mostrar()
p2.mostrar()
