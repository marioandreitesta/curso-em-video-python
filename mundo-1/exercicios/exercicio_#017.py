# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa. 

from cores import LIMPAR, ROXO_BOLD, AMARELO_BOLD, CINZA_BOLD

DIV = 40

print(f"{ROXO_BOLD}-{LIMPAR}"*DIV)
print(f"{CINZA_BOLD}CALCULADORA DE HIPOTENUSA{LIMPAR}".center(DIV))
print(f"{ROXO_BOLD}-{LIMPAR}"*DIV)

cateto_oposto = float(input(f"{CINZA_BOLD}Digite o comprimento do cateto oposto: {AMARELO_BOLD}"))
cateto_adjacente = float(input(f"{CINZA_BOLD}Digite o comprimento do cateto adjacente: {AMARELO_BOLD}"))
soma_catetos  = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
hipotenusa = soma_catetos ** 0.5

print(f"{LIMPAR}{ROXO_BOLD}-{LIMPAR}"*DIV)
print(f"{ROXO_BOLD}Processando...{LIMPAR}".center(DIV))
print(f"{ROXO_BOLD}-{LIMPAR}"*DIV)

print(f"{CINZA_BOLD}O comprimento da hipotenusa é: {ROXO_BOLD}{hipotenusa:.2f}{LIMPAR}")