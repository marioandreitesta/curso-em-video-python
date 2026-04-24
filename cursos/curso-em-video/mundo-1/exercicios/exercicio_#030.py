# Faça um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
DIV = 27

print('ESSE NÚMERO É PAR OU ÍMPAR?'.center(DIV))
print('-' * DIV)

try:
    numero = int(input('Digite um número: '))

    if numero % 2 == 0:
        print('Esse número é PAR!')
    else:
        print('Esse número é ÍMPAR!')
except ValueError:
    print('Isso não é um número, tente novamente!')

