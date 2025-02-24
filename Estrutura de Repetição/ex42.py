intervalo1 = []
intervalo2 = []
intervalo3 = []
intervalo4 = []

while True:
    numero = float(input("Digite um número: "))
    if numero >= 0 and numero <= 25:
        intervalo1.append(numero)
    elif numero >= 26 and numero <= 50:
        intervalo2.append(numero)
    elif numero >= 51 and numero <= 75:
        intervalo3.append(numero)
    elif numero >= 76 and numero <= 100:
        intervalo4.append(numero)
    elif numero < 0:
        break

print(
    f"\nNumeros no intervalo de 0-25: {len(intervalo1)}"
    f"\nNúmeros no intervalo de 26-50: {len(intervalo2)}"
    f"\nNúmeros no intervalo de 51-75: {len(intervalo3)}"
    f"\nNúmeros no intervalo de 76-100: {len(intervalo4)}"
)
