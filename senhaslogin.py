logins = []
senhas = []

while True:
    usuario = input("Digite o nome do usuario (Ou fim para encerrar): ")

    if usuario == "fim":
        break

    senha = input("Digite a senha: ")

    logins.append(usuario)
    senhas.append(senha)

print("\n=== LOGIN ===")
usuario = input("Usuario: ")
senha = input("Senha: ")

if usuario in logins:
    posicao = logins.index(usuario)

    if senhas[posicao] == senha:
        print("Login realizado com sucesso! ")
    else:
        print("Senha incorreta! ")
else:
    print("Usuario nao cadastrado! ")

