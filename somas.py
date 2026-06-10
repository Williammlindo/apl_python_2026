soma = 0
numero = 0
quantidade = 0
maior_numero = 0

while numero >=0:
    numero = int(input("Digite o numero inteiro: "))
    
    if numero >= 0:
        soma += numero
        quantidade += 1

        if numero > maior_numero:
            maior_numero > numero
print(f"soma: {soma}")

if quantidade > 0:
     print(f"Media:{soma / quantidade:.2f}")
     print(f"O maior numero é {maior_numero}")
else:
    print("Nenhum numero positivo informado")