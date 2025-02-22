morango = float(input("Quantos kilos de morango: "))
maca = float(input("Quantos kilos de maçã: "))

valor = 0

if morango <= 5:
    valor += morango * 2.5
else:
    valor += morango * 2.2

if maca <= 5:
    valor += maca * 1.8
else:
    valor += maca * 1.5

if (morango + maca) > 8 or valor > 25:
    valor -= valor * 10 / 100

print(f"Valor total a pagar: R${valor:.2f}")