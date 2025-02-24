while True:
    numero = int(input("Digite um numero: "))
    if not 0 < numero < 16:
        continue
    fatorial = 1
    for i in range(numero, 1, -1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}")
    if input("Deseja continuar? (S/N): ").upper() != "S":
        break