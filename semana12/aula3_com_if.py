# Aula 3 — Versão SEM polimorfismo: tudo decidido com if


def enviar(tipo, destino, texto):
    if tipo == "email":
        print(f"[E-MAIL] Para: {destino} | {texto}")
    elif tipo == "sms":
        print(f"[SMS] {destino}: {texto}")
    elif tipo == "whatsapp":
        print(f"[WhatsApp] {destino}: {texto} ✔✔")
    else:
        print("Tipo desconhecido!")


def custo(tipo):
    if tipo == "email":
        return 0.00
    elif tipo == "sms":
        return 0.10
    elif tipo == "whatsapp":
        return 0.05
    else:
        return 0.00


enviar("email", "ana@email.com", "Seu pedido saiu")
enviar("push", "celular-da-ana", "Seu pedido saiu")
print(custo("sms"))
