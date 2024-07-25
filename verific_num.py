# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

# Solicitar a entrada de um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))
# Verificar se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
