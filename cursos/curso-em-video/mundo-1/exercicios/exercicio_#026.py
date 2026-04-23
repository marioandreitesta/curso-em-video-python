# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez. 
DIV = 40

frase = input('Digite uma frase: ').strip()
print('' * DIV)

frase_formatada = frase.lower()
contando_a = frase.count('a')

print(f'Quantas vezes a palavra "A" aparece na frase: {contando_a}')
print(f'Posição da primeira aparição: {frase_formatada.find('a')}')
print(f'Posição da última aparição: {frase_formatada.rfind('a')}')