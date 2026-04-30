# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. 

from cores import LIMPAR, VERDE_BACKGROUND, CINZA_BOLD, VERDE_BOLD, VERDE_UNDERLINE

print(f"{VERDE_BACKGROUND}Programa de Reajuste Salarial!{LIMPAR}")

salario_atual = float(input(f"{CINZA_BOLD}Digite o seu salário atual: {VERDE_BOLD}R${LIMPAR}"))

print(f"{VERDE_UNDERLINE}Reajustando seu salário...{LIMPAR}")

reajuste_salario = salario_atual * 1.15

print(f"{CINZA_BOLD}O seu salário recebeu um aumento de {VERDE_BOLD}[10%]{LIMPAR}")
print(f"{CINZA_BOLD}Salário reajustado: {VERDE_BOLD}R${VERDE_UNDERLINE}{reajuste_salario:.2f}{LIMPAR}")