import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao Gerador de senhas!")
n_letras = int(input("Quantas letras você gostaria na sua senha?\n"))
n_simbolos = int(input(f"Quantos símbolos você gostaria?\n"))
n_numeros = int(input(f"Quantos números você gostaria?\n"))

lista_senha=[]

for letra in range(1, n_letras + 1):
        lista_senha.append(random.choice(letras))

for numero in range(1, n_numeros + 1):
        lista_senha.append(random.choice(numeros))

for simbolo in range(1, n_simbolos + 1):
        lista_senha.append(random.choice(simbolos))

random.shuffle(lista_senha)
senha = "".join(lista_senha)

print(f"Sua senha é: {senha}")