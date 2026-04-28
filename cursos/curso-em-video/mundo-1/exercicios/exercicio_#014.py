# Escreva um programa que converta uma temperatura digitando em graus Celcius e converta para graus Fahrenheit. 

from cores import LIMPAR, VERMELHO_BOLD, CINZA_BOLD, PRETO_BACKGROUND

print(f"{PRETO_BACKGROUND}Conversor de Celsius para Fahrenheit!{LIMPAR}")

graus_celsius = float(input(f"{CINZA_BOLD}Digite a temperatura {VERMELHO_BOLD}[C°]{CINZA_BOLD}: "))
graus_fahrenheit = (graus_celsius * 1.8) + 32

print(f"{LIMPAR}{CINZA_BOLD}Temperatura em graus Fahrenheit: {VERMELHO_BOLD}{graus_fahrenheit:.1f}{CINZA_BOLD}°F{LIMPAR}")
