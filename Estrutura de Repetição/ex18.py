n = int(input("Digite a quantidade de números: "))

numeros = []

for i in range(n):
    num = float(input("Digite um número: "))
    numeros.append(num)

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

print(
    f"\nO menor número é: {menor}"
    f"\nO maior número é: {maior}"
    f"\nA soma dos números é: {soma}"
)