n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Qual operação deseja executar (+, -, * ou /): ")

if op == "+":
    resultado = n1 + n2
elif op == "-":
    resultado = n1 - n2
elif op == "*":
    resultado = n1 * n2
elif op == "/":
    resultado = n1 / n2
else:
    print("Operador inválido!")

if resultado % 2 == 0:
    print("Número par!")
else:
    print("Número ímpar!")

if resultado >= 0:
    print("Número positivo!")
else:
    print("Número negativo!")

if resultado % 1 == 0:
    print("Número inteiro!")
else:
    print("Número decimal!")