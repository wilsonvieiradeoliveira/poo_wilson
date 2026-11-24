# Aula 3 — Versão COM polimorfismo: cada classe sabe o que fazer


class Notificacao:
    def __init__(self, destino, texto):
        self.destino = destino
        self.texto = texto


class Email(Notificacao):
    def enviar(self):
        print(f"[E-MAIL] Para: {self.destino} | {self.texto}")

    def custo(self):
        return 0.00


class SMS(Notificacao):
    def enviar(self):
        print(f"[SMS] {self.destino}: {self.texto}")

    def custo(self):
        return 0.10


class WhatsApp(Notificacao):
    def enviar(self):
        print(f"[WhatsApp] {self.destino}: {self.texto} ✔✔")

    def custo(self):
        return 0.05


class Push(Notificacao):  # tipo NOVO: só esta classe foi acrescentada
    def enviar(self):
        print(f"[PUSH] {self.destino}: {self.texto}")

    def custo(self):
        return 0.00


avisos = [
    Email("ana@email.com", "Seu pedido saiu"),
    SMS("(11) 99999-0000", "Seu pedido saiu"),
    Push("celular-da-ana", "Seu pedido saiu"),
]
total = 0
for aviso in avisos:
    aviso.enviar()
    total = total + aviso.custo()
print(f"Custo dos envios: R$ {total:.2f}")
