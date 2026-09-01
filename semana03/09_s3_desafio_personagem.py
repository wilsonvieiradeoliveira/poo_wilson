class Personagem:
    def atacar(self, alvo):
        alvo.vida -= self.ataque

    def esta_vivo(self):
        return self.vida > 0


def simular_batalha(nome_heroi, vida_heroi, ataque_heroi, nome_vilao, vida_vilao, ataque_vilao):
    heroi = Personagem()
    heroi.nome = nome_heroi
    heroi.vida = vida_heroi
    heroi.ataque = ataque_heroi

    vilao = Personagem()
    vilao.nome = nome_vilao
    vilao.vida = vida_vilao
    vilao.ataque = ataque_vilao

    while heroi.esta_vivo() and vilao.esta_vivo():
        heroi.atacar(vilao)
        if not vilao.esta_vivo():
            return heroi.nome
        vilao.atacar(heroi)
        if not heroi.esta_vivo():
            return vilao.nome


# Combinação 1: ataque e vida iguais para os dois
vencedor1 = simular_batalha("Aria", 100, 15, "Dragão", 100, 15)
print(f"Combinação 1 (mesmo ataque, mesma vida): vencedor = {vencedor1}")

# Combinação 2: vilão com ataque bem maior, mesma vida
vencedor2 = simular_batalha("Aria", 100, 15, "Dragão", 100, 30)
print(f"Combinação 2 (vilão com ataque maior): vencedor = {vencedor2}")

# Combinação 3: herói com o dobro de vida, mas ataque mais fraco
vencedor3 = simular_batalha("Aria", 200, 10, "Dragão", 100, 20)
print(f"Combinação 3 (herói com mais vida, ataque menor): vencedor = {vencedor3}")

# Anotações dos resultados:
# - Com ataque e vida iguais, quem ataca primeiro (o herói) leva vantagem e vence.
# - Quando o vilão bate bem mais forte, ele vence mesmo apanhando primeiro a cada turno.
# - Dobrar a vida do herói compensa um ataque mais fraco: ele aguenta turnos suficientes
#   para vencer mesmo causando menos dano por golpe.
