preco = float(input("Digite o preço do pão: "))
qtd = 1

print(f"Preço do pão: R${preco}")

while qtd < 51:
    print(f"{qtd} - R${qtd * preco:.2f}")
    qtd += 1