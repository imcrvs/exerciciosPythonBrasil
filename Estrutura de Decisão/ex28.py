tipo = input("Digite o tipo da carne comprada: ")
qtd = float(input("Digite a quantidade de carne comprada: "))
pagamento = input("Dinheiro ou Cartão Tabajara (D ou C): ")

valor = 0

if tipo == "Filé Duplo":
    if qtd <= 5:
        valor += qtd * 4.9
    else:
        valor += qtd * 5.8

if tipo == "Alcatra":
    if qtd <= 5:
        valor += qtd * 5.9
    else:
        valor += qtd * 6.8

if tipo == "Picanha":
    if qtd <= 5:
        valor += qtd * 6.9
    else:
        valor += qtd * 7.8

if pagamento == "D" or pagamento == "d":
    tipoPgt = "Dinheiro"
    desconto = 0
elif pagamento == "C" or pagamento == "c":
    tipoPgt = "Cartão Tabajara"
    desconto = valor * 5 / 100

valorTotal = valor - desconto

print(
    f"\nCupom Fiscal",
    f"\nTipo de carne comprada: R${tipo}"
    f"\nQuantidade de carne: R${qtd}"
    f"\nPreço total da compra: R${valor}"
    f"\nTipo de pagamento: R${tipoPgt}"
    f"\nDesconto: R${desconto}"
    f"\nValor a pagar: R${valorTotal}"
)