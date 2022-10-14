nome = "André"
idade = 24
altura = 1.82
peso = 83
ano_atual = 2022
data_nascimento = ano_atual - idade
imc = peso / (altura*altura)

print(f'{nome} tem {idade} anos de idade, {altura} de altura e pesa {peso}kg')
print(f'O imc de {nome} é: {imc:.2f}')
print(f'{nome} nasceu em {data_nascimento}')