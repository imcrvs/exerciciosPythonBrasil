numero = int(input("Gostaria de ver a tabuada de qual número: "))
limite = int(input("Até qual número da tabuada gostaria de ver: "))

for tabuada in range(0, limite + 1):
    resultado = numero * tabuada
    print(f"{numero} x{ tabuada} = {numero*tabuada}")