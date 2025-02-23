data = input("Digite uma data no formato dd/mm/aaaa: ")

dia, mes, ano = data.split("/")

dia, mes, ano = int(dia), int(mes), int(ano)

if ano < 0:
    print("Ano inválido!")
else:
    if mes < 1 or mes > 12:
        print("Mês inválido!")
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        if dia > 0 and dia <= 31:
            print("Data válida!")
        else:
            print("Dia inválido!")
    elif mes in [4,6, 9, 11]:
        if dia > 0 and dia <= 30:
            print("Data válida!")
        else:
            print("Data inválida!")
    