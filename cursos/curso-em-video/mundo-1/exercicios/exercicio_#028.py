# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O Programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randrange

DIV = 35

print('' * DIV)
print('TENTE ADVINHAR O NÚMERO DE 0 A 10')
print('-' * DIV)

try:
    resposta_usuario = int(input('Em qual número estou pensando? '))

    numero_aleatorio = randrange(0,10)

    if resposta_usuario == numero_aleatorio:
        print(f'Você acertou! O número era {numero_aleatorio}')
    elif resposta_usuario > 5:
        print('Oops! Esse número é maior que 5, tente novamente.')    
    else:
        print(f'Você errou, o número era {numero_aleatorio}')

except ValueError:
    print('Oops! O valor digitado não é um número, tente novamente.')