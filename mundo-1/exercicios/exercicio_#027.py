# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 

from cores import AZUL_BOLD, CINZA_BOLD, LIMPAR

DIV = 40

print('' * DIV)
nome_usuario = input(f'{AZUL_BOLD}Digite seu nome completo: {CINZA_BOLD}').strip()
print(f'{LIMPAR}' * DIV)

nome_dividido = nome_usuario.split()

print(f'{CINZA_BOLD}Seu primeiro nome é: {AZUL_BOLD}{nome_dividido[0]}')
print(f'{CINZA_BOLD}Seu último nome é: {AZUL_BOLD}{nome_dividido[-1]}{LIMPAR}')