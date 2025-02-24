n = int(input("Digite a quantidade de números: "))

numeros = []

for i in range(n):
    while True:
        num = float(input("Digite um número entre 0 e 1000: "))
        if 0 <= num <= 1000:
            numeros.append(num)
            break
        else:
            print("Número inválido! Digite um valor entre 0 e 1000.")

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

print(
    f"\nO menor número é: {menor}"
    f"\nO maior número é: {maior}"
    f"\nA soma dos números é: {soma}"
)