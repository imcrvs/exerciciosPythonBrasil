n = int(input("Digite um número: "))

if n <= 1:
    print(f"O número {n} não é um número primo!")
else:
    if n == 2:
        print(f"O número {n} é um número primo!")
    else:
        primo = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if primo:
            print(f"{n} é primo!")
        else:
            print(f"{n} não é primo!")