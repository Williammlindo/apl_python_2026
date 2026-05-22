for tentativas in range(1,4):
    usuario = input ("usuario:")
    senha = input ("senha:")
    if usuario == "aluno" and senha == "12345":
        print("Acesso liberado")
        break
    else:
        print("acesso negado tente novamente")

if tentativas ==3:
    print("Voce tentou 3 vezes")