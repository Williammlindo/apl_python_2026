primeiro_termo = int(input("Digite o primeiro termo: "))
quantidade = int(input("Digite a quantidade de termos: "))
razao = int(input("Digite a razão: "))

termo = primeiro_termo

for cont in range(quantidade):
    print(termo)
    termo += razao