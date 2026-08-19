USUARIO = "admin"
SENHA = "python123"

usuario_digitado = input("Usuário: ")
senha_digitada = input("Senha: ")

if usuario_digitado == USUARIO and senha_digitada == SENHA:
    print("Acesso liberado!")
else:
    print("Usuário ou senha incorretos.")
