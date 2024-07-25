# Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

def is_palindrome(s):
    # Remover espaços e converter para minúsculas
    s = s.replace(" ", "").lower()
    
    # Remover pontuações
    import string
    s = s.translate(str.maketrans('', '', string.punctuation))
    
    # Verificar se a string é igual ao seu reverso
    return s == s[::-1]

# Solicitar a entrada do usuário
entrada = input("Digite uma palavra ou frase: ")

# Verificar se é um palíndromo
if is_palindrome(entrada):
    print(f'"{entrada}" é um palíndromo.')
else:
    print(f'"{entrada}" não é um palíndromo.')
