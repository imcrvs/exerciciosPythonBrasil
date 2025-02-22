nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media <= 4.0:
    conceito = "E"
    situacao = "Reprovado"
elif media > 4.0 and media <= 6.0:
    conceito = "D"
    situacao = "Reprovado"
elif media > 6.0 and media <= 7.5:
    conceito = "C"
    situacao = "Aprovado"
elif media > 7.5 and media <= 9.0:
    conceito = "B"
    situacao = "Aprovado"
elif media > 9.0 and media <= 10.0:
    conceito = "A"
    situacao = "Aprovado"
else:
    print("Não é possível calcular!")

nota1
nota2
media
conceito
situacao

print(
    f"\nPrimeira nota: {nota1}",
    f"\nSegunda nota: {nota2}",
    f"\nNota média: {media}",
    f"\nConceito: {conceito}",
    f"\nSituação: {situacao}",
)