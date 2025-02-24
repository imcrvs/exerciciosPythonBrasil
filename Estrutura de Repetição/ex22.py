n = int(input("Digite um número: "))

if n <= 1:
    print(f"O número {n} não é um número primo!")
else:
    if n == 2:
        print(f"O número {n} é um número primo!")
    else:
        primo = True
        divisores = []
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                primo = False
                divisores.append(i)
                if i != n // i:
                    divisores.append(n // i)
        if primo:
            print(f"{n} é primo!")
        else:
            divisores.sort()
            print(f"\n{n} não é primo!\nEle é divisível por: {', '.join(map(str, divisores))}")