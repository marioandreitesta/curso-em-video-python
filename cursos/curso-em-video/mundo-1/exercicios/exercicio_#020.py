# O mesmo professor do desafio #019 quer sortear a ordem de apresentação de trabalho dos alunos. 
# Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.

from random import shuffle

DIV = 45

print("="*DIV)
print("LISTA DE APRESENTAÇÃO DOS ALUNOS".center(DIV))
print("="*DIV)

aluno0 = input("Digite o nome do 1° aluno: ")
aluno1 = input("Digite o nome do 2° aluno: ")
aluno2 = input("Digite o nome do 3° aluno: ")
aluno3 = input("Digite o nome do 4° aluno: ")
print("-"*DIV)

alunos = [aluno0, aluno1, aluno2, aluno3]
ordem_alunos = shuffle(alunos)

print("ORDEM DE APRESENTAÇÃO:".center(DIV))
print("-"*DIV)
print(f"1° Lugar: {alunos[0]}")
print(f"2° Lugar: {alunos[1]}")
print(f"3° Lugar: {alunos[2]}")
print(f"4° Lugar: {alunos[3]}")