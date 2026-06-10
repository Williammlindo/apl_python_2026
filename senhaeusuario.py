for tentativas in range(1,4):
    usuario = input("Usuario: ")
    senha = input("Senha: ")
    if usuario == "aluno" and senha == "12345":
        print("Acesso liberado seja bem vindo ")
        break
else:
    print("Acesso negado tente novamente ")

if tentativas == 3:
    print("Voce tentou mais de 3 vezes ")