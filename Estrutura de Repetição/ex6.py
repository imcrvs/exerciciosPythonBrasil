firstNumber = int(input("Digite o primeiro número: "))
secondNumber = int(input("Digite o segundo número: "))
thirdNumber = int(input("Digite o terceiro número: "))

if firstNumber > secondNumber and firstNumber > thirdNumber:
    print(f"O maior número é: {firstNumber}")
elif secondNumber > firstNumber and secondNumber > thirdNumber:
    print(f"O maior número é: {secondNumber}")
elif thirdNumber > firstNumber and thirdNumber > secondNumber:
    print(f"O maior número é: {thirdNumber}")
else:
    print("Os números são iguais.")