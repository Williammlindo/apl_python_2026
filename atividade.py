soma = 0
numero = 0
quantidade = 0
maior_numero = 0
while numero >=0:
    numero = int(input("Digite umnumero inteiro:"))
    soma += numero
    quantidade += 1
    if numero >maior_numero:
        maior_numero = numero

print(f"soma:{soma}")
print(f"media:{soma / quantidade:.2f}")
print(f"o maior numero é : {maior_numero}")