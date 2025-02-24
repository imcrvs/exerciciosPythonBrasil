# Faça um programa que leia 5 números e informe o maior número.

numeros = []

for i in range (5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

print("O maior número da lista é: ", max(numeros))