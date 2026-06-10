soma = 0
nome_mais_barato = ""
preco_mais_barato = ""
for cont in range (5):
    nome = input("Nome do medicamento:")
    preco = float(input("Preço do medicamento:"))
    soma += preco
    if cont == 0:
        nome_mais_barato = nome
        preco_mais_barato = preco
    elif preco < preco_mais_barato:
        nome_mais_barato = nome
        preco_mais_barato = preco

print(f"A media dos preços é:{soma/5:.2f}")
print(f"O remedio mais barato é:{nome_mais_barato} é seu preço é {preco_mais_barato}")
