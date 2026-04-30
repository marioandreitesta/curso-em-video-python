# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 

from cores import CINZA_BOLD, VERDE_BOLD, BRANCO_BACKGROUND, LIMPAR

print(f"{CINZA_BOLD}Veja quantos dólares você consegue comprar na cotação atual!{LIMPAR}")

saldo_reais = int(input(f"{BRANCO_BACKGROUND}Insira seu saldo atual:{LIMPAR} {VERDE_BOLD}R${LIMPAR}"))

cotacao_dolar = 4.98 # Cotação da data 14/04/2026
saldo_convertido = saldo_reais / cotacao_dolar

print(f"{CINZA_BOLD}Com {VERDE_BOLD}R${saldo_reais:.2f}{LIMPAR}, {CINZA_BOLD}você consegue comprar:{LIMPAR} {VERDE_BOLD}${saldo_convertido:.2f}{LIMPAR} {CINZA_BOLD}dólares!{LIMPAR}")
