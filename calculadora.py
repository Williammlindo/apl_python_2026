import os

while True:

    opcao = int(input("""Calculadora"
1.Soma
2.Subtraçao
3.Divisao             
4.Multplicaça
0.Sair
Escolha a operação: """))

    if opcao ==0:
        os.system("clear")
        print("Fim")
        break
    num1 = int(input("Digite o primeiro numero:"))
    num2 = int(input("Digite o segundo numero:"))

    if opcao ==1:
        resultA