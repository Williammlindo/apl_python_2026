usuarios = []

while True:
    login = input("Digite o nome de usuario (ou sim para encerrar)")

    if login == "fim":
        break

    senha = input ("digite a senha")
    usuarios = [login] = senha

    print("\n === LOGIN ===")

    login = input("usuario: ")
    senha = input("senha: ")

    if login in usuarios:
        if usuarios[login] == senha:
            print("login realizado com sucesso! ")
        else:
            print("Senha incorreta! ")
    else:
        print("Usuario nao cadastrado! ")