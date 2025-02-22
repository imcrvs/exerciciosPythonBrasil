firstNumber = int(input("Digite o primeiro número: "))
secondNumber = int(input("Digite o Segundo número: "))
thirdNumber = int(input("Digite o Terceiro número: "))

if firstNumber > secondNumber and firstNumber > thirdNumber:
    print(f"O maior número é: {firstNumber}")
elif secondNumber > firstNumber and secondNumber > thirdNumber:
    print(f"O maior número é: {secondNumber}")
elif thirdNumber > firstNumber and thirdNumber > secondNumber:
    print(f"O maior número é: {thirdNumber}")

if firstNumber < secondNumber and firstNumber < thirdNumber:
    print(f"O menor número é: {firstNumber}")
elif secondNumber < firstNumber and secondNumber < thirdNumber:
    print(f"O menor número é: {secondNumber}")
elif thirdNumber < firstNumber and thirdNumber < secondNumber:
    print(f"O menor número é: {thirdNumber}")