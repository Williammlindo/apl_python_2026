quant_pares = 0
for cont in range(10):
    numero = int(input("Digite 10 numeros:"))            
    if numero % 2 == 0:
        quant_pares +=1

print(f"Tem {quant_pares} numeros pares")
