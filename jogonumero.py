import random

numero_sorteado = random.randint(1,10)

for tentativas in range(3):
    palpite = int(input("Diga seu palpite: "))
    if palpite == numero_sorteado:
        print("Parabens voce acertou ! ")
        break
    else:
        print("Voce errou tente novamente ")

        if palpite > numero_sorteado:
            print("Tente um numero menor")
        else:
            print("Tente um numero maior")

        if tentativas ==2:
            print("FIM DE JOGO")