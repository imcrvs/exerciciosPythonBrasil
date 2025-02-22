user = input("Digite o seu usuário: ")
password = input("Digite a sua senha: ")

while user == password:
    print("Nome de usuário não pode ser igual a senha: ")
    user = input("Digite o seu usuário: ")
    password = input("Digite a sua senha: ")