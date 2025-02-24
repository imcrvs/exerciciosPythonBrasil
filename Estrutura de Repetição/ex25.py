n = int(input("Digite o número de idades: "))

idades = []

for i in range(n):
    num = int(input("Digite a idade: "))
    idades.append(num)

media = int(sum(idades) / len(idades))

if media >= 0 and media <= 25:
    print(f"Com a média de {media}, a turma é jovem!")
elif media > 25 and media <= 60:
    print(f"Com a média de {media}, a turma é Adulta!")
else:
    print(f"Com a média de {media}, a turma é idosa!")