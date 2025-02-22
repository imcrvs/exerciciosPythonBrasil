firstNumber = int(input("Digite o primeiro número: "))
secondNumber = int(input("Digite o segundo número: "))

if firstNumber > secondNumber:
    print(f"O maior número é: {firstNumber}")
elif firstNumber < secondNumber:
    print(f"O maior número é: {secondNumber}")
else:
    print("Os números são iguais.")