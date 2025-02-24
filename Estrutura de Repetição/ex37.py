maiorAltura = 0
menorAltura = 5.0
maiorPeso = 0
menorPeso = 500

alturas = []
pesos = []
clientes = 0

codigoMaisAlto = 0
codigoMaisBaixo = 0
codigoMaiorPeso = 0
codigoMenorPeso = 0

while True:
    codigo = int(input("Digite o código: "))
    if codigo == 0:
        break

    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))

    if altura > maiorAltura:
        maiorAltura = altura
        codigoMaisAlto = codigo
    if altura < menorAltura:
        menorAltura = altura
        codigoMaisBaixo = codigo
    if peso > maiorPeso:
        maiorPeso = peso
        codigoMaiorPeso = codigo
    if peso < menorPeso:
        menorPeso = peso
        codigoMenorPeso = codigo

    alturas.append(altura)
    pesos.append(peso)
    clientes += 1

if clientes > 0:
    mediaAltura = sum(alturas) / clientes
    mediaPeso = sum(pesos) / clientes
else:
    mediaAltura = mediaPeso = 0

print(f"O código do cliente mais alto é: {codigoMaisAlto}")
print(f"A altura do cliente mais alto é de: {maiorAltura}")
print(f"O código do cliente mais baixo é: {codigoMaisBaixo}")
print(f"A altura do cliente mais baixo é de: {menorAltura}")
print(f"O código do cliente mais gordo é: {codigoMaiorPeso}")
print(f"O peso do cliente mais gordo é de: {maiorPeso}")
print(f"O código do cliente mais magro é: {codigoMenorPeso}")
print(f"O peso do cliente mais magro é de: {menorPeso}")
print(f"A média de altura dos clientes da academia é de: {mediaAltura}")
print(f"A média de peso dos clientes da academia é de: {mediaPeso}")