# Faça um programa que leia um ano qualquer e mostre se ele é bissexto. 

from cores import LIMPAR, CINZA_BOLD, PRETO_BACKGROUND, VERMELHO_BOLD, VERDE_BOLD

DIV = 27

print(f'{PRETO_BACKGROUND}VERIFICADOR DE ANO BISSEXTO{LIMPAR}')
print(f'{CINZA_BOLD}-{LIMPAR}' * DIV)

try:
    ano = int(input(f'{CINZA_BOLD}Digite o ano: '))

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            print(f'{CINZA_BOLD}O ano {VERDE_BOLD}{ano}{CINZA_BOLD} é bissexto!{LIMPAR}')
    else:
        print(f'{CINZA_BOLD}O ano {VERMELHO_BOLD}{ano}{CINZA_BOLD} não é bissexto!{LIMPAR}')
except ValueError:
    print(f'{VERMELHO_BOLD}Error{CINZA_BOLD}: isso não é um número!{LIMPAR}')