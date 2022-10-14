"""Operadores condicionais
"""


nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
idade = int(idade)
idade_limite = 18


if(idade >=idade_limite):
    print (f" Parabéns {nome}, Você pode ter um limite de crédito")

else:
    print(f" Desculpe {nome}, Você é menor de idade, não pode pegar limite de crédito!")