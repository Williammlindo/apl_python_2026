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

    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))


    if opcao ==1:
        Resultado = num1 + num2
        print(f"O resultado e {Resultado}")

    elif opcao ==2:
        Resultado = num1 - num2
        print(f"O resultado e {Resultado}")

    elif opcao ==3:
        Resultado = num1 / num2
        print(f"O resultado e {Resultado}")

    elif opcao ==4:
        Resultado = num1 * num2
        print(f"O resultado e {Resultado}")

    else:
        print("Opcao invalida")