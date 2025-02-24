n = int(input('Digite a quantidade de eleitores: '))

candidato1 = 0
candidato2 = 0
candidato3 = 0

for i in range(n):
    while True:
        voto = int(input("Digite o votoo (1, 2 ou 3): "))
        if voto == 1:
            candidato1 += 1
            break
        elif voto == 2:
            candidato2 += 1
            break
        elif voto == 3:
            candidato3 += 1
            break
        else:
            print("Voto inválido! Digite 1, 2 ou 3.")

print(f"O total de votos do candidato 1 é de: {candidato1}")
print(f"O total de votos do candidato 2 é de: {candidato2}")
print(f"O total de votos do candidato 3 é de: {candidato3}")