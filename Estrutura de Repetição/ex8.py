numeros = []

for i in range (5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

media = sum(numeros) / len(numeros)

print(
    f"\nA soma dos números é: ", sum(numeros),
    f"\nA media dos números é: {media}"
)