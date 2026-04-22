# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas;
# Quantas letras ao todo (sem considerar espaços);
# Quantas letras tem o primeiro nome.

DIV = 44

print('' * DIV)
print('CURIOSIDADES SOBRE O SEU NOME'.center(DIV))
print('' * DIV)

nome = input('Digite seu nome completo: ').strip()
print('-' * DIV)

nome_dividido = nome.split()

print(f'Seu nome em maiúsculo: {nome.upper()}')
print(f'Seu nome em minúsculo: {nome.lower()}')
print(f'Quantidade de letras em seu nome completo: {len(nome)}')
print(f'Quantidade de letras em seu primeiro nome: {len(nome_dividido[0])}')
