# Um professor que sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido. 

from random import choice
from cores import LIMPAR, VERDE_BOLD, CINZA_BOLD, ROXO_BOLD

DIV = 47

print(f"{CINZA_BOLD}="*DIV)
print("SORTEADOR DE ALUNOS".center(DIV))
print(f"{CINZA_BOLD}={LIMPAR}"*DIV)

aluno0 = input(f"Escreva o nome do primeiro aluno: {CINZA_BOLD}")
aluno1 = input(f"{LIMPAR}Escreva o nome do segundo aluno: {CINZA_BOLD}")
aluno2 = input(f"{LIMPAR}Escreva o nome do terceiro aluno: {CINZA_BOLD}")
aluno3 = input(f"{LIMPAR}Escreva o nome do quarto aluno: {CINZA_BOLD}")
print(f"{CINZA_BOLD}-{LIMPAR}"*DIV)

ALUNOS = aluno0, aluno1, aluno2, aluno3

print(f"{ROXO_BOLD}-> {CINZA_BOLD}O aluno(a) sorteado foi: {VERDE_BOLD}{choice(ALUNOS)}{LIMPAR}")