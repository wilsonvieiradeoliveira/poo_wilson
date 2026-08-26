class Aluno:
    pass
 
a1 = Aluno()
a1.nome = "Ana"
a1.pontos = 75
 
a2 = Aluno()
a2.nome = "Bruno"
a2.pontos = 55
 
for aluno in [a1, a2]:
    if aluno.pontos >= 60:
        print(f"{aluno.nome}: aprovado")
    else:
        print(f"{aluno.nome}: em recuperação")
