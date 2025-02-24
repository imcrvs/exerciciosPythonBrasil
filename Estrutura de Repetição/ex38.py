salarioInicial = float(input("Digite o salário inicial do funcionário: "))
anoAtual = int(input("Digite o ano atual: "))

anoContratacao = 1995
percentualAumento = 1.5 / 100

salarioAtual = salarioInicial

for ano in range(1996, anoAtual + 1):
    aumento = salarioAtual * percentualAumento
    salarioAtual += aumento
    percentualAumento *= 2

print(f"O salário do funcionário em {anoAtual} é de R$ {salarioAtual:.2f}")
