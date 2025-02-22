valorHora = float(input("Quanto você ganha por hora: "))
horasMes = int(input("Quantas horas você trabalha por mês: "))

salarioBruto = valorHora * horasMes
ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - ir - inss - sindicato

print(f"+ Salário Bruto: R${salarioBruto}")
print(f"- IR (11%): R${ir}")
print(f"- INSS (8%): R${inss}")
print(f"- Sindicato (5%): R${sindicato}")
print(f"= Salário Líquido: R${salarioLiquido}")