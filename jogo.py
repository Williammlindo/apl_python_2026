
nome_produto = input("Digite o nome do produto: ")
preco = input("Digite o preco do produto: ")
estoque = input("Digite o estoque do produto: ")
promocao = input("O produto esta em promocao? (S|N): ").lower() =="s"

dados_produto = [nome_produto,preco,estoque,promocao]

print("---------Dados do produto----------")    
print(f"Nome:{dados_produto(0)}")
print(f"Preco:{dados_produto(1)}")
print(f"Estoque:{dados_produto(2)}")
print(f"Promoçao:{dados_produto(3)}")
print(f"Promoçao.: "{'sim' if dados_produto})