
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
idade = int(idade)
min_idade= 18
max_idade = 30

if(idade >min_idade and idade <max_idade):
    print(f" Parabéns {nome}, Você pode ter um limite de crédito")

else:
    print(f" Desculpe {nome}, Você é menor de idade, não pode pegar limite de crédito!")