altura = float(input("Digite a sua altura: "))
sexo = input("Você é homem ou mulher: ")

if sexo == "homem":
    pesoIdeal = (72.7 * altura) - 58
    print(f"O seu peso ideal é: {pesoIdeal}")
elif sexo == "mulher":
    pesoIdeal = (62.1 * altura) - 44.7
    print(f"O seu peso ideal é: {pesoIdeal}")
else:
    print("Tente novamente!")