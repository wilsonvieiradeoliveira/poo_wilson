
aluno = {
  "nome": "Ana",
  "idade": 15,
  "curso": "Info",
}
 
print(aluno["nome"])

print(aluno["idade"])       # ler: 15
aluno["idade"] = 16         # alterar (fez aniversário!)
aluno["nota"] = 9.5         # chave nova? É criada na hora
 
# percorrer chaves e valores:
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
