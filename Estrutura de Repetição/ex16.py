primeiro = 0
segundo = 1

while primeiro <= 500:
    print(primeiro, end=" ")
    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo