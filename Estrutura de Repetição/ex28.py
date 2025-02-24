qtd = int(input("Digite a quantidade de CDs: "))

valorTotal = []

for i in range(qtd):
    valor = float(input("Valor do CD: "))
    valorTotal.append(valor)

media = sum(valorTotal) / len(valorTotal)

print(f"A média de preço é: R${media}")