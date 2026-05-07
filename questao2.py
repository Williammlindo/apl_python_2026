n1 = float(input("Digite o primeiro numero:"))
n2 = float(input("Digite o segundo numero:"))

print ("1-Media poderada")
print ("2-quadrado da soma")
print ("3-Cubo do menor")

op = int(input("Escolha uma opçao"))

if op == 1:
    print(" Resultado =", (n1*2 + n2*3) / 5 )

elif op ==2:
    print("Resultado =", (n1+n2) **2)

elif op ==3:
    print("Resultado =", min (n1 , n2 )**3)

else:
    print("Opçao invalida")
