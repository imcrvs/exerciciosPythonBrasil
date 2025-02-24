n = int(input("Quantas notas deseja avaliar: "))

notas = []

for i in range(n):
    num = float(input("Digite a nota: "))
    notas.append(num)

media = sum(notas) / len(notas)

print(f"A média das notas é: {media}")