"""
Exercício 1 — Trapaceie você mesmo (s6_ex1)

Antes de qualquer cadeado, a classe Personagem (igual à do arena.py da
semana 5) aceita qualquer valor nos atributos. Este script repete as 3
trapaças da apostila e mostra o estado do personagem depois de cada uma,
para deixar claro o problema que o encapsulamento vai resolver.
"""


class Personagem:
    def __init__(self, nome, ataque=15):
        self.nome = nome
        self.vida = 100
        self.ataque = ataque

    def atacar(self, alvo):
        alvo.vida -= self.ataque

    def esta_vivo(self):
        return self.vida > 0

    def status(self):
        vivo = "vivo" if self.esta_vivo() else "derrotado"
        print(f"{self.nome} - vida: {self.vida} - ataque: {self.ataque} - {vivo}")


heroi = Personagem("Aria")
vilao = Personagem("Sombra")

print("=== Antes das trapaças ===")
heroi.status()
vilao.status()

print("\n=== Trapaça 1: heroi.vida = 999999 (imortal) ===")
heroi.vida = 999999
heroi.status()

print("\n=== Trapaça 2: vilao.ataque = 0 (inofensivo) ===")
vilao.ataque = 0
vilao.status()

print("\n=== Trapaça 3: heroi.vida = -50 (não faz sentido) ===")
heroi.vida = -50
heroi.status()

print("\n=== Testando na batalha ===")
vilao.atacar(heroi)
heroi.status()

# ANOTAÇÕES — o que acontece na batalha:
# - As 3 trapaças funcionam sem nenhum aviso ou erro: o Python aceita
#   qualquer valor atribuído a heroi.vida e vilao.ataque, sem checar nada.
# - Com heroi.vida = 999999, o "herói" fica praticamente imortal: seriam
#   necessários milhares de ataques para zerar essa vida.
# - Com vilao.ataque = 0, o método atacar() desconta 0 da vida do alvo:
#   o vilão vira completamente inofensivo.
# - Com heroi.vida = -50, o status mostra vida negativa, o que não faz
#   sentido para um personagem — e esta_vivo() só "acerta" por sorte,
#   porque vida <= 0 já é tratado como derrotado.
# - Conclusão: nada dentro da classe impede esses valores. Qualquer parte
#   do código (ou um erro de digitação) pode quebrar as regras do jogo.
