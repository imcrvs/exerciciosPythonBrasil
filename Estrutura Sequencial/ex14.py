peso = float(input("Digite a pesagem dos peixes: "))

limite = 50

if peso > limite:
    excesso = peso - limite
    multa = excesso * 4
    print(f"Multa de {multa} aplicada a pesagem do peixe!")
else:
    print("Não será aplicada multa!")