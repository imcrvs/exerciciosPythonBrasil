valorHora = float(input("Digite o valor da hora: "))
horasMes = float(input("Quantas horas você trabalha por mês: "))

salarioBruto = valorHora * horasMes

if salarioBruto <= 900:
    ir = salarioBruto
elif salarioBruto > 900 and salarioBruto <= 1500:
    ir = salarioBruto * 0.05
elif salarioBruto > 1500 and salarioBruto <= 2500:
    ir = salarioBruto * 0.10
else:
    ir = salarioBruto * 0.20

inss = salarioBruto * 0.10
fgts = salarioBruto * 0.11
totalDescontos = ir + inss
salarioLiquido = salarioBruto - totalDescontos

print(
    f"\nSalário Bruto     : R${salarioBruto:.2f}",
    f"\n(-) IR (5%)       : R${ir:.2f}",
    f"\n(-) INSS ( 10%)   : R${inss:.2f}",
    f"\nFGTS (11%)        : R${fgts:.2f}",
    f"\nTotal de descontos: R${totalDescontos:.2f}",
    f"\nSalário Liquido   : R${salarioLiquido:.2f}",
)