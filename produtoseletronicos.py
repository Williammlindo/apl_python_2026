produtos = []
resposta = "s"

while resposta == "s":
    produto = input("Diga o nome do produto: ")
    produtos.append(produto)

    resposta = input("Deseja adicionar outro produto? (s/n): ").lower()

    print(produtos)
