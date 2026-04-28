# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. 

from cores import LIMPAR, CINZA_BOLD, VERDE_BOLD, AMARELO_UNDERLINE

print(f"{AMARELO_UNDERLINE}Conversor de Metros!{LIMPAR}")

metros = float(input(f"{CINZA_BOLD}Digite a metragem que deseja converter [m]: {LIMPAR}"))

CENTIMETROS = metros * 100
MILIMETROS = metros * 1000

print(f"{AMARELO_UNDERLINE}{metros:.0f} metro(s) em:{LIMPAR}")
print(f"{CINZA_BOLD}Centímetros: {VERDE_BOLD}{CENTIMETROS:.0f}{LIMPAR}cm")
print(f"{CINZA_BOLD}Milímetros: {VERDE_BOLD}{CENTIMETROS:.0f}{LIMPAR}mm")