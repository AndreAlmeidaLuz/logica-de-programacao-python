""" Entrada de dados do usuário
"""

nome = input("Whats or name? ")
idade = input("Qual sua idade? ")

anos_nascimento = 2022 - int(idade)

print()
print(f'{nome} tem {idade} anos e nasceu em {anos_nascimento}')