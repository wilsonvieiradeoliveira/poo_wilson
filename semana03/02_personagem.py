class Personagem:
    def atacar(self, alvo):
        alvo.vida -= self.ataque
        print(f"{self.nome} atacou {alvo.nome}!")
 
    def esta_vivo(self):
        return self.vida > 0
 
    def status(self):
        print(f"{self.nome} - vida: {self.vida}")
 
heroi = Personagem()
heroi.nome = "Aria"
heroi.vida = 100
heroi.ataque = 15
 
vilao = Personagem()
vilao.nome = "Dragão"
vilao.vida = 100
vilao.ataque = 10
 
while heroi.esta_vivo() and vilao.esta_vivo():
    heroi.atacar(vilao)
    if not vilao.esta_vivo():
        print(f"{heroi.nome} venceu!")
        break
    vilao.atacar(heroi)
    if not heroi.esta_vivo():
        print(f"{vilao.nome} venceu!")
        break
    heroi.status()
    vilao.status()
