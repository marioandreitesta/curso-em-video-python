# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

from cores import LIMPAR, VERMELHO_BOLD, PRETO_BACKGROUND, VERDE_BOLD, CINZA_BOLD

nome = input(f'{PRETO_BACKGROUND}Digite seu nome completo: {LIMPAR}').strip()

nome_formatado = nome.upper()
nome_verificador = f'{LIMPAR}SILVA'

if nome_verificador in nome_formatado:
    print(f'{CINZA_BOLD}Seu nome tem a palavra "{VERDE_BOLD}Silva{LIMPAR}"')
else:
        print(f'{CINZA_BOLD}Seu nome não tem "{VERMELHO_BOLD}Silva{LIMPAR}"')