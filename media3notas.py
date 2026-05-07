nota1 = float(input("Digite a Primeira nota:"))
nota2 = float(input("Digite a Segunda nota:"))
nota3 = float(input("Digite a Terceira nota:"))

media = (nota1 + nota2 + nota3 ) / 3

print (f"a media é: {media}")

if media >=7: 
    print ("você passou")
elif media >=4:
    print ("você ficou de prova final")
else:
    print("você reprovou")