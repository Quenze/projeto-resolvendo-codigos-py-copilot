# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicitar a entrada dos dois números do usuário
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))

# Solicitar a operação desejada
operacao = input("Digete a operação que deseja realizar (+, -, *, /): ")
# Realizar a operação com base na escolha do usuário
if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(abs(num1 - num2))
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    print(num1 / num2)
else:
    print("Operação inválida")


