# Aula 2 — Sistema de notificações


class Notificacao:
    def __init__(self, destino, texto):
        self.destino = destino
        self.texto = texto

    def enviar(self):
        print(f"Enviando para {self.destino}: {self.texto}")


class Email(Notificacao):
    def enviar(self):
        print(f"[E-MAIL] Para: {self.destino} | {self.texto}")


class SMS(Notificacao):
    def enviar(self):
        print(f"[SMS] {self.destino}: {self.texto}")


class WhatsApp(Notificacao):
    def enviar(self):
        print(f"[WhatsApp] {self.destino}: {self.texto} ✔✔")


def disparar(notificacao):  # aceita QUALQUER notificação
    notificacao.enviar()


avisos = [
    Email("ana@email.com", "Seu pedido saiu"),
    SMS("(11) 99999-0000", "Seu pedido saiu"),
    WhatsApp("(11) 98888-0000", "Seu pedido saiu"),
]
for aviso in avisos:
    disparar(aviso)
