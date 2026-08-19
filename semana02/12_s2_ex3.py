def eh_maior(idade):
    return idade >= 18
 
idade = int(input("Sua idade: "))
if eh_maior(idade):
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
