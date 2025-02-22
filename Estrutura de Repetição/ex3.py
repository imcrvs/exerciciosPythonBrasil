nome = input("Digite o nome: ")
while len(nome) <= 3:
    print("O nome deve ser maior que três caracteres!")
    nome = input("Digite o nome: ")

idade = int(input("Digite a idade: "))
while idade > 150 or idade < 0:
    print("A idade deve estar entre 0 e 150!")
    idade = int(input("Digite a idade: "))

salario = float(input("Digite o salário: "))
while salario <= 0:
    print("O Salário deve ser maior que R$0,00")
    salario = float(input("Digite o salário: "))

sexo = input("Digite o sexo (F ou M): ")
while sexo.lower() != "f" and sexo.lower() != "m":
    print("Sexo inválido!")
    sexo = input("Digite o sexo (F ou M): ")

estadoCivil = input("Digite o estado civil (S, C, V ou D): ")
while(
    estadoCivil != "s"
    and estadoCivil != "c"
    and estadoCivil != "V"
    and estadoCivil != "D"
):
    print("Estado civil inválido!")
    estadoCivil = input("Digite o estado civil (S, C, V ou D): ")