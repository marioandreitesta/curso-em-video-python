# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite. 

from random import randrange
from cores import LIMPAR, VERMELHO_BOLD, VERDE_BOLD, CINZA_BOLD, AMARELO_BOLD

DIV = 27
VELOCIDADE_CARRO = randrange(10, 220)   
LIMITE_RADAR = 80
VALOR_MULTA = (VELOCIDADE_CARRO - LIMITE_RADAR) * 7

print('' * DIV)
print(f'{CINZA_BOLD}RADAR DE VELOCIDADE {VERMELHO_BOLD}80{CINZA_BOLD}KM/H{LIMPAR}')
print(f'{AMARELO_BOLD}-{LIMPAR}' * DIV)

if VELOCIDADE_CARRO > LIMITE_RADAR:
    print(f'{CINZA_BOLD}Você {VERMELHO_BOLD}ultrapassou{CINZA_BOLD} o limite de velocidade! {VERMELHO_BOLD}[{VELOCIDADE_CARRO}Km/h]{LIMPAR}')
    print(f'{CINZA_BOLD}Multa: {VERDE_BOLD}R${VERMELHO_BOLD}{VALOR_MULTA:.2f}{LIMPAR}')
else:
    print(f'{CINZA_BOLD}Tenha uma {VERDE_BOLD}boa viagem{CINZA_BOLD}!{LIMPAR}')