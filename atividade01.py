tentativas = 0

usuario = input ("usuario:")
senha = input ("senha:")

while usuario != ("aluno") or senha != ("12345"):
    tentativas +=1
    print("acesso negado tente novamente")
    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")

if tentativas >=-3:
    print("voce ja tentou 3 vezes")
    
elif usuario == ("aluno") and senha == ("12345"):
    print("Seja bem vindo")
