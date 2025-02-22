int1 = int(input("Digite o primeiro número inteiro: "))
int2 = int(input("Digite o segundo número inteiro: "))
real = float(input("Digite um número real: "))

a = (int1 * 2) + (real / 2)
b = (int1 * 3) + real
c = real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {a}")
print(f"A soma do triplo do primeiro com o terceiro é: {b}")
print(f"O terceiro elevado ao cubo é: {c}")