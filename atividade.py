soma = 0
numero = 1
quantidade = 0
maior_numero = 0
while numero >=0:
    numero = int(input("Digite os numeros inteiros"))

    if numero >0:
        soma += numero
        quantidade +=1
    if numero > maior_numero:
        maior_numero = numero
print(f"Soma: {soma}")

if quantidade >0:
    print(f"Media: {soma / quantidade}")
    print(f"Maior numero: {maior_numero}")
else:
    print("Nenhum numero inteiro informado")