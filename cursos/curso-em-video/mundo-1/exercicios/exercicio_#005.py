# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor. 

print("Escolha um número para saber seu sucessor e antecessor!")

numero = int(input("Digite um número: "))

sucessor = numero + 1
antecessor = numero - 1

print(f"Sucessor: {sucessor}")
print(f"Antecessor: {antecessor}")