# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira. 
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6. 

print("="*40)
print(f"{'Leitor de Porção Inteira':^40}")
print("="*40)

numero = str(input("Digite um número: "))
print("-" * 40)

print(f"A porção inteira do número {numero} é {numero[0]}.")