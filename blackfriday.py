import os

while True:

    opcao = int(input("""BLACK FRIDAY"
1.A vista Desconto de 15%
2.Debito Desconto de 10%
3.Credito Desconto de 5%         
0.Sair
Escolha a opcao: """))

    if opcao ==0:
        os.system("clear")
        print("Fim")
        break

    Valor = float(input("Digite o valor da compra: "))

    if opcao ==1:
        Desconto = Valor*15/100 
        final = Valor - Desconto
        print(f"O resultado é {Desconto}")
        print(f"O valor final é {final} ")

    elif opcao ==2:
        Desconto = Valor*10/100
        final = Valor - Desconto
        print(f"O resultado é {Desconto}")
        print(f"O valor final é {final} ")

    elif opcao ==3:
        Desconto = Valor*5/100
        final = Valor - Desconto
        print(f"O resultado é {Desconto }")
        print(f"O valor final é {final} ")

    else:
        print("Opcao invalida")
