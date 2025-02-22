tamanhoArquivo = float(input("Digite o tamanho do arquivo para download: "))
velocidadeLink = int(input("Digite a velocidade do seu link de internet: "))

tempoDownload = (tamanhoArquivo / velocidadeLink) * 60

print(f"O download será feito em: {tempoDownload}")