a = float(input("Digite o valor de a: "))

if a == 0:
    print("Não é uma equação do segundo grau")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print("Delta menor que 0. Não há raízes reais.")
    elif delta == 0:
        raiz = (-b) / (2 * a)
        print(f"Delta é zero. A raíz é {raiz}")
    else:
        raiz1 = (-b + (delta ** (1 / 2))) / (2 * a)
        raiz2 = (-b - (delta ** (1 / 2))) / (2 * a)
        print(
            f"Delta maior que zero. A raíz 1 é {raiz1}, e a raiz 2 é {raiz2}"
        )