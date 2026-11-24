# Aula 5 — Formas de pagamento da lanchonete


class Pagamento:
    def __init__(self, valor):
        self.valor = valor

    def taxa(self):
        return 0.00

    def total(self):
        return self.valor + self.taxa()


class Pix(Pagamento):  # sem taxa: usa a da mãe
    pass


class Cartao(Pagamento):
    def taxa(self):
        return self.valor * 0.05  # 5% da maquininha


class Boleto(Pagamento):
    def taxa(self):
        return 3.50


def fechar_pedido(pagamento):  # não sabe (nem precisa saber) qual é a forma
    print(f"Total a pagar: R$ {pagamento.total():.2f}")


formas = [Pix(40.00), Cartao(40.00), Boleto(40.00)]
for forma in formas:
    fechar_pedido(forma)
