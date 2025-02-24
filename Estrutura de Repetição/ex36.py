tabuada = int(input("Montar tabuada de: "))
inicial = int(input("Começar por: "))
final = int(input("Terminar em: "))

if inicial < final:
    for i in range(inicial, final + 1):
        resultado = tabuada * i
        print(f"{tabuada} x {i} = {resultado}")
else:
    print("O número inicial não pode ser menor que o final!")