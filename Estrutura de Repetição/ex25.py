pontuacao = 0

q1 = input("Telefonou para a Vítima? ")
if q1 == "S" or q1 == "s":
    pontuacao += 1
q2 = input("Esteve no local do crime? ")
if q2 == "S" or q2 == "s":
    pontuacao += 1
q3 = input("Mora perto da vitima? ")
if q3 == "S" or q3 == "s":
    pontuacao += 1
q4 = input("Devia para a vitima? ")
if q4 == "S" or q4 == "s":
    pontuacao += 1
q5 = input("Já trabalhou para a vítima? ")
if q5 == "S" or q5 == "s":
    pontuacao += 1

if pontuacao < 2:
    print("Inocente!")
elif pontuacao == 2:
    print("Suspeito!")
elif pontuacao == 3 or pontuacao == 4:
    print("Cúmplice!")
elif pontuacao == 5:
    print("Assassino!")