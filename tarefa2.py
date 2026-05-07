peso=float(input("Digite o peso do aluno (kg):"))
altura=float(input("Digite a altura do aluno (m):"))

imc= peso / (altura **2)

print (f"O imc é:{imc:.2f}")

if imc < 18.5:
    print ("Você esta com baixo peso")

elif imc < 25:
    print ("Você esta com peso normal")
   
elif imc < 30:
     print ("Você esta sobrepeso")

elif imc < 35:
    print ("Você esta com obesidade grau 1")

elif imc < 40:
    print ("Você esta com obesidade grau 2")

else:
    print("Você esta com obesidade grau 3")

