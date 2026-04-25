# Faça um programa que leia um ano qualquer e mostre se ele é bissexto. 
DIV = 27

print('VERIFICADOR DE ANO BISSEXTO')
print('-' * DIV)

try:
    ano = int(input('Digite o ano: '))

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano {ano} é bissexto!')
    else:
        print('Esse ano não é bissexto.')
except ValueError:
    print('Isso não é número, tente novamente.')