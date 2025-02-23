preco1 = float(input("Digite o valor do primeiro produto: "))
preco2 = float(input("Digite o valor do segundo produto: "))
preco3 = float(input("Digite o valor do terceiro número: "))

if preco1 < preco2 and preco1 < preco3:
    print("Compre o primeiro produto.")
elif preco2 < preco1 and preco2 < preco3:
    print("Compre o segundo produto.")
else:
    print("Compre o terceiro produto.")