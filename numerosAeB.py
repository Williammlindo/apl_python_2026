a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))


if a < b:
    soma = 0
    for i in range (a, + b + 1):
        soma +=i
    
    print("A soma dos intervalos é: ",soma)
else:
    print("ERRO")
