temps = []

while True:
    entrada = input("Digite a temperatura (ou 'fim' para encerrar): ")
    
    if entrada == 'fim' or entrada == "FIM":
        break
    
    try:
        temperatura = float(entrada)
        temps.append(temperatura)
    except ValueError:
        print("Por favor, digite um número válido.")

if len(temps) > 0:
    maior = max(temps)
    menor = min(temps)
    media = sum(temps) / len(temps)

    print(f"A maior temperatura registrada foi de: {maior}")
    print(f"A menor temperatura registrada foi de: {menor}")
    print(f"A média das temperaturas foi de: {media}")
else:
    print("Nenhuma temperatura registrada.")
