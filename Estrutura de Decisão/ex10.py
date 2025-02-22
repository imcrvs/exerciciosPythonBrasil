entrada = input("Em qual turno você estuda (M, V ou N): ")

if entrada == "M" or entrada == "m":
    print("Bom dia!")
elif entrada == "V" or entrada == "v":
    print("Boa tarde!")
elif entrada == "N" or entrada == "n":
    print("Boa noite!")
else:
    print("Valor inválido!")