valor = float(input("Valor da compra:"))
print("1-A vista")
print("2-Debito")
print("3-Credito")

op =int(input("Forma de pagamento:"))

if op ==1:
    total = valor * 0.85

elif op ==2:
    total = valor * 0.90

elif op ==3:
    total = valor * 0.95

else:
    print("Opçao invalida")
    total = valor

print("Valor final é:",total)
