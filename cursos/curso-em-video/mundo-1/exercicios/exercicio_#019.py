# Um professor que sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido. 

from random import choice

DIV = 47

print("="*DIV)
print("SORTEADOR DE ALUNOS".center(DIV))
print("="*DIV)

aluno0 = input("Escreva o nome do primeiro aluno: ")
aluno1 = input("Escreva o nome do segundo aluno: ")
aluno2 = input("Escreva o nome do terceiro aluno: ")
aluno3 = input("Escreva o nome do quarto aluno: ")
print("-"*DIV)

ALUNOS = aluno0, aluno1, aluno2, aluno3

print(f"-> O aluno(a) sorteado foi: {choice(ALUNOS)}")