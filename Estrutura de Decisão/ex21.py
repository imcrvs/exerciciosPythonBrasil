saque = int(input("Digite o valor do saque (entre R$10,00 e R$600,00): "))

if saque < 10 and saque > 600:
    print("Valor inválido!")
else:
    cem = saque // 100
    saque -= cem * 100
    cinquenta = saque // 50
    saque -= cinquenta * 50 
    dez = saque // 10
    saque -= dez * 10
    cinco = saque // 5
    saque -= cinco * 5
    um = saque
    if cem > 0:
        print(f"{cem} nota(s) de cem")
    if cinquenta > 0:
        print(f"{cinquenta} nota(s) de cinquenta")
    if dez > 0:
        print(f"{dez} nota(s) de dez")
    if cinco > 0:
        print(f"{cinco} nota(s) de cinco")
    if um > 0:
        print(f"{um} nota(s) de um")