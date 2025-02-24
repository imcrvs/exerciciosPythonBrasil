print('Lojas Tabajara')
i = 1
total = 0
while True:
    preco = float(input('Produto %d: R$ ' %i))
    if preco == 0:
        break
    total += preco
    i += 1

print('Total: R$ %.2f' % total)
dinheiro = float(input('Digite o valor fornecido pelo cliente: '))
troco = dinheiro - total
print('Troco: R$ %.2f' % troco)