salarioAtual = float(input("Digite o salário atual do colaborador: "))

if salarioAtual <= 280:
    salarioNovo = salarioAtual * 1.2
    percentual = "20%"
elif salarioAtual > 280 and salarioAtual <= 700:
    salarioNovo = salarioAtual * 1.15
    percentual = "15%"
elif salarioAtual > 700 and salarioAtual <= 1500:
    salarioNovo = salarioAtual * 1.10
    percentual = "10%"
else:
    salarioNovo = salarioAtual * 1.05
    percentual = "5%"

valorAumento = salarioNovo - salarioAtual

print(f"O salário antes do reajuste é: R${salarioAtual:.2f}")
print(f"O percentual a ser aumentado é de: {percentual}")
print(f"Será feito um aumento no valor de: R${valorAumento:.2f}")
print(f"O novo salário será de: R${salarioNovo:.2f}")