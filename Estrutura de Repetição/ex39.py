maisAlto = 0
maisBaixo = 500

numeroMaisAlto = 0
numeroMaisBaixo = 0

for i in range(1, 11):
    numero = int(input("Digite o numero do aluno: "))
    altura = float(input("Digite a altura do aluno (em centímetros): "))
    if altura > maisAlto:
        maisAlto = altura
        numeroMaisAlto = numero
    if altura < maisBaixo:
        maisBaixo = altura
        numeroMaisBaixo = numero

print(f"O número do aluno mais alto é: {numeroMaisAlto}")
print(f"A altura do aluno mais alto e de: {maisAlto}")
print(f"O número do aluno mais baixo é: {numeroMaisBaixo}")
print(f"A altura do aluno mais baixo é de: {maisBaixo}")