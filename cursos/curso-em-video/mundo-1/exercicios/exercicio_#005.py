# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor. 

from cores import VERMELHO_BOLD, VERDE_BOLD, AMARELO_UNDERLINE, LIMPAR

print(f"Escolha um número para saber seu {VERDE_BOLD}sucessor{LIMPAR} e {VERMELHO_BOLD}antecessor!{LIMPAR}")

numero = int(input(f"{AMARELO_UNDERLINE}Digite um número:{LIMPAR} "))

sucessor = numero + 1
antecessor = numero - 1

print(f"Sucessor: {VERDE_BOLD}{sucessor}{LIMPAR}")
print(f"Antecessor: {VERMELHO_BOLD}{antecessor}{LIMPAR}")