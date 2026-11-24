# Aula 1 — "É um" × "tem um": o carro TEM um motor


class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        print(f"Motor de {self.potencia} cv ligado: vrum!")


class Carro:
    def __init__(self, modelo, potencia):
        self.modelo = modelo
        self.motor = Motor(potencia)  # o carro TEM um motor


fusca = Carro("Fusca", 50)
print(fusca.modelo)
fusca.motor.ligar()
