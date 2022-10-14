user = input("Digite seu nome: ")
password = input("Digite sua senha: ")

user_bd = 'andre'
password_bd = '123456'

if(user == user_bd and password == password_bd):
    print("você está logado!")

else:
    print("Usuário ou senha incorretos!")