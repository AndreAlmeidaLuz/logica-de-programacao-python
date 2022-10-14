user = input("Digite seu usuário: ")
qtd_caracteres = len(user)

print(user, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print("digite um nome maior que 6 caracteres")

else:
    print("Cadastrado no sistema!")