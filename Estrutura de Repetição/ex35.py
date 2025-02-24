n = int(input("Digite o valor de N: "))

primos = []

for num in range(1, n + 1):
    if num < 2:
        continue
    if num == 2:
        primos.append(num)
        continue
    if num % 2 == 0:
        continue
    
    limite = int(num ** 0.5) + 1

    primo = True

    for i in range (3, limite, 2):
        if num % i == 0:
            primo = False
            break
    if primo:
        primos.append(num)

print(f"Números primos entre 1 e {n}: {primos}")