segredo = 7
tentativas = 0
max_tentativas = 5
acertou = False

while tentativas < max_tentativas:
    palpite = int(input("Tente adivinhar (1-10): "))
    tentativas += 1
    if palpite == segredo:
        acertou = True
        break
    elif palpite > segredo:
        print("O segredo é menor!")
    else:
        print("O segredo é maior!")

if acertou:
    print(f"Parabéns! Você acertou em {tentativas} tentativas!")
else:
    print(f"Gamer Over! O número secreto era {segredo}")

