idade = int(input("Sua idade: "))
jogo = input("Nome do jogo: ")
 
if idade >= 18:
    print(f"{jogo}: liberado, qualquer classificação.")
elif idade >= 16:
    print(f"{jogo}: liberado até classificação 16.")
else:
    print(f"{jogo}: apenas classificação livre a 14.")
