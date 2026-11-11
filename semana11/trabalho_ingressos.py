# Trabalho avaliativo — código-base (Ingressos de cinema)


class Ingresso:
    def __init__(self, filme, preco):
        self.filme = filme
        self.preco = preco

    def valor_final(self):
        return self.preco

    def mostrar(self):
        print(f"{self.filme} - R$ {self.valor_final():.2f}")


class MeiaEntrada(Ingresso):
    def valor_final(self):
        return self.preco / 2


class IngressoVIP(Ingresso):
    def __init__(self, filme, preco, poltrona):
        super().__init__(filme, preco)
        self.poltrona = poltrona

    def mostrar(self):
        super().mostrar()
        print(f"   Poltrona: {self.poltrona}")


comum = Ingresso("Duna", 30.00)
meia = MeiaEntrada("Duna", 30.00)
vip = IngressoVIP("Duna", 60.00, "F12")
comum.mostrar()
meia.mostrar()
vip.mostrar()
