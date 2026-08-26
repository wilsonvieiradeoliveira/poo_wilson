class Aluno:
    def mostrar_boletim(self):
        print(f"{self.nome}: {self.pontos} pontos")
 
    def ganhar_pontos(self, qtd):
        self.pontos += qtd
 
a1 = Aluno()
a1.nome = "Ana"
a1.pontos = 50
 
a1.mostrar_boletim()
a1.ganhar_pontos(15)
a1.mostrar_boletim()
