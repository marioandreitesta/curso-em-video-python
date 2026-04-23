# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

nome_cidade = input('Digite o nome da sua cidade: ').strip()

nome_cidade = nome_cidade.upper()

if nome_cidade.startswith('SANTO') == True:
    print('O nome da cidade digitado começa com "Santo"')
else:
    print('O nome da sua cidade não começa com "Santo"')

