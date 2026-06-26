import random

lista = []

nome = input("Digite o nome de quem comprou a rifa(ou FIM para encerrar): ")

while nome != "FIM":
    lista.append(nome)

    nome = input("Digite o nome de quem comprou a rifa(ou FIM para encerrar): ")

if len(lista) >0:
    sorteado = random.choice(lista)
    print("O ganhador foi:", sorteado)
else:
    print("nenhum nome foi cadastrado,")    