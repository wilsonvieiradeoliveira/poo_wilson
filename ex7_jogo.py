segredo = 7
tentativas = 0

palpite = int(input("Tente adivinhar (1-10): "))
tentativas += 1

while palpite != segredo:
    if palpite > segredo:
        print("Menor!")
    else:
        print("Maior!")
    palpite = int(input("Tente de novo: "))
    tentativas += 1

print(f"Parabéns! Você acertou em {tentativas} tentativas!")
