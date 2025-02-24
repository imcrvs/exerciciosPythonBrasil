candidatos = {
    1: "José",
    2: "João",
    3: "Maria",
    4: "Ana"
}

votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_candidato4 = 0
votos_nulos = 0
votos_brancos = 0
total_votos = 0

while True:
    voto = int(input("Digite o código do candidato (1 a 4), 5 para Nulo, 6 para Branco ou 0 para encerrar: "))

    if voto == 0:
        break
    elif voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    elif voto == 4:
        votos_candidato4 += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_brancos += 1
    else:
        print("Código inválido! Digite um código entre 1 e 6 ou 0 para sair.")
        continue

    total_votos += 1

if total_votos > 0:
    percentual_nulos = (votos_nulos / total_votos) * 100
    percentual_brancos = (votos_brancos / total_votos) * 100
else:
    percentual_nulos = percentual_brancos = 0

print("\nResultados da eleição:")
print(f"{candidatos[1]}: {votos_candidato1} votos")
print(f"{candidatos[2]}: {votos_candidato2} votos")
print(f"{candidatos[3]}: {votos_candidato3} votos")
print(f"{candidatos[4]}: {votos_candidato4} votos")
print(f"Votos nulos: {votos_nulos} ({percentual_nulos:.2f}%)")
print(f"Votos em branco: {votos_brancos} ({percentual_brancos:.2f}%)")
print(f"Total de votos: {total_votos}")
