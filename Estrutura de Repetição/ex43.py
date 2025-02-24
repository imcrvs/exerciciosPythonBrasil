cardapio = {
    100: 1.20,  # Cachorro Quente
    101: 1.30,  # Bauru Simples
    102: 1.50,  # Bauru com ovo
    103: 1.20,  # Hambúrguer
    104: 1.30,  # Cheeseburguer
    105: 1.00   # Refrigerante
}

total_geral = 0

while True:
    codigo = int(input("Digite o código do item desejado: "))

    if codigo == 0:
        break

    if codigo in cardapio:
        quantidade = int(input("Digite a quantidade desejada: "))
        if quantidade > 0:
            subtotal = cardapio[codigo] * quantidade
            total_geral += subtotal
            print(f"Item adicionado: {quantidade}x Código {codigo} - Total: R${subtotal:.2f}\n")
        else:
            print("Quantidade inválida. Tente novamente.\n")
    else:
        print("Código inválido. Tente novamente.\n")

print(f"Total do pedido: R${total_geral:.2f}")