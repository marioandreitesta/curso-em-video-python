# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

DIV = 40

print('' * DIV)
print('SEPARANDO DIGITOS DE UM NÚMERO'.center(DIV))
print('=' * DIV)

numero = int(input('Digite um número: '))
print('-' * DIV)

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')