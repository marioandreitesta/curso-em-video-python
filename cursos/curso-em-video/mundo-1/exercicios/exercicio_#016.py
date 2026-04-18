# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira. 
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6. 

from math import trunc

print("="*40)
print(f"{'CONSULTE A PORÇÃO INTEIRA DE UM NÚMERO':^40}")
print("="*40)

numero = float(input("Digite um número: "))
print("-" * 40)

porcao_int = trunc(numero)

print(f"Porção inteira do número é: {porcao_int}")