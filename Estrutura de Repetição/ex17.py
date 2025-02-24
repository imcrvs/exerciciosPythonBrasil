numero = int(input("Digite um número: "))
fatorial = 1

for i in range (numero, 1, -1):
    fatorial *= i

print(f"O fatorial de {numero} é: {fatorial}")