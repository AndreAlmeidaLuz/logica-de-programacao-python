num1 = input("digite o primeiro numero: ")
num2 = input("digite o segundo numero: ")

#isnumeric isdigit isdecimal

#verificar se a variavel tem só numero e positivos
#retorna um booleano
#print(num1.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)

else:
    print("Conta não realizada, verifique se os números foram digitados corretamente")