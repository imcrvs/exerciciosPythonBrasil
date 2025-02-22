area = float(input("Digite o tamanho da área a ser pintada (m²): "))

area_com_folga = area * 1.1

litros_necessarios = area_com_folga / 6

latas = int(litros_necessarios / 18) + (1 if litros_necessarios % 18 > 0 else 0)
custo_latas = latas * 80

galoes = int(litros_necessarios / 3.6) + (1 if litros_necessarios % 3.6 > 0 else 0)
custo_galoes = galoes * 25

latas_mistura = int(litros_necessarios / 18)
restante = litros_necessarios - (latas_mistura * 18)
galoes_mistura = int(restante / 3.6) + (1 if restante % 3.6 > 0 else 0)
custo_mistura = (latas_mistura * 80) + (galoes_mistura * 25)

print(f"\nOpção 1 - Apenas latas de 18 litros:")
print(f"  Quantidade de latas: {latas}")
print(f"  Custo total: R$ {custo_latas:.2f}")

print(f"\nOpção 2 - Apenas galões de 3,6 litros:")
print(f"  Quantidade de galões: {galoes}")
print(f"  Custo total: R$ {custo_galoes:.2f}")

print(f"\nOpção 3 - Mistura de latas e galões:")
print(f"  Quantidade de latas: {latas_mistura}")
print(f"  Quantidade de galões: {galoes_mistura}")
print(f"  Custo total: R$ {custo_mistura:.2f}")
