SENHA = "python123"
tentativas = 3
 
while tentativas > 0:
    digitada = input("Senha: ")
    if digitada == SENHA:
        print("Acesso liberado!")
        break   # sai do loop na hora
    tentativas = tentativas - 1
    print(f"Errou! Restam {tentativas}.")
