area = float(input("Digite o tamanho da área a ser pintada (m²): "))

litros_necessarios = area / 3

latas_necessarias = litros_necessarios // 18
if litros_necessarios % 18 != 0:
    latas_necessarias += 1

preco_total = latas_necessarias * 80

print(f"Quantidade de latas: {int(latas_necessarias)}")
print(f"Preço total: R$ {preco_total:.2f}")
