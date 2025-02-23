lado1 = float("Digite o primeiro lado do triângulo: ")
lado2 = float("Digite o segundo lado do triângulo: ")
lado3 = float("Digite o terceiro lado do triângulo: ")

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado2 + lado3 > lado1:
    if lado1 == lado2 and lado2 == lado3:
        print("É um triângulo equilátero!")
    if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("É um triângulo Isósceles!")
    else:
        print("É um triângulo Escaleno!")
else:
    print("Não é um triângulo.")