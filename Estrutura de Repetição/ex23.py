n = int(input("Digite o valor de N: "))

primos = []
divisoes = 0

for num in range(1, n + 1):
    if num < 2:
        continue
    if num == 2:
        primos.append(num)
        divisoes += 1
        continue
    if num % 2 == 0:
        divisoes += 1
        continue
    
    divisores = 1
    limite = int(num ** 0.5) + 1

    primo = True

    for i in range (3, limite, 2):
        divisores += 1
        if num % i == 0:
            primo = False
            break
    if primo:
        primos.append(num)
    
    divisoes += divisores

print(f"Números primos entre 1 e {n}: {primos}")
print(f"Total de divisões realizadas: {divisoes}")