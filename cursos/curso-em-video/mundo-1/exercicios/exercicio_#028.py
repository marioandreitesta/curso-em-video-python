# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O Programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randrange
from cores import LIMPAR, CINZA_BOLD, VERDE_BOLD, VERMELHO_BOLD, CIANO_BOLD, VERMELHO_BACKGROUND

DIV = 35

print('' * DIV)
print(f'{CINZA_BOLD}TENTE ADVINHAR O NÚMERO DE {CIANO_BOLD}0{LIMPAR}{CIANO_BOLD} A {CIANO_BOLD}10{LIMPAR}')
print('-' * DIV)

try:
    resposta_usuario = int(input(f'{CINZA_BOLD}Em qual {CIANO_BOLD}número{CINZA_BOLD} estou pensando? '))

    numero_aleatorio = randrange(0,10)

    if resposta_usuario == numero_aleatorio:
        print(f'Você {VERDE_BOLD}acertou{CINZA_BOLD}! O número era {VERDE_BOLD}{numero_aleatorio}')
    elif resposta_usuario > 5:
        print(f'{VERMELHO_BACKGROUND}Oops! Esse número é maior que 5, tente novamente.{LIMPAR}')    
    else:
        print(f'{CINZA_BOLD}Você {VERMELHO_BOLD}errou{CINZA_BOLD}, o número era {CIANO_BOLD}{numero_aleatorio}{LIMPAR}')

except ValueError:
    print(f'{VERMELHO_BACKGROUND}Oops! O valor digitado não é um número, tente novamente.{LIMPAR}')