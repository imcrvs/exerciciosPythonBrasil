turmas = int(input("Digite a quantidade de turmas: "))
qtdAlunos = []

for i in range(turmas):
    while True:
        qtd = int(input("Digite o número de alunos: "))
        if qtd <= 40:
            qtdAlunos.append(qtd)
            break
        else:
            print("Quantidade não pode ser maior que 40!")

media = int(sum(qtdAlunos) / len(qtdAlunos))

print(f"A média de alunos por turma é de: {media}")