# Faça um programa que leia três números e mostre qual é o maior e qual é o menor. 

import cores

def pedir_numeros():

    while True:
        entrada = input(f"\n{cores.CINZA_BOLD}Digite {cores.ROXO_BOLD}três{cores.CINZA_BOLD} números separados por espaço: {cores.LIMPAR}")
        lista_numeros = entrada.split()

        if len(lista_numeros) != 3:
            print(f"{cores.VERMELHO_BOLD}Erro:{cores.CINZA_BOLD} Você digitou {cores.VERMELHO_BOLD}{len(lista_numeros)} {cores.CINZA_BOLD}valor(es). É preciso {cores.VERDE_BOLD}três!{cores.LIMPAR}")
            continue

        try:
            numeros = list(map(float, lista_numeros))
            return numeros
        except ValueError:
            print(f"{cores.VERMELHO_BOLD}Error:{cores.CINZA_BOLD} Certifique-se de digitar apenas números. Ex: {cores.VERDE_BOLD}10 4.5 15{cores.LIMPAR}")

def exibir_resultados():

    menor = min(numeros)
    maior = max(numeros)

    print(f"\n{cores.CINZA_BOLD}{'=' * 38}")
    print(f"{cores.CINZA_BOLD}Números digitados: {cores.ROXO_BOLD}{numeros}")
    print(f"{cores.CINZA_BOLD}Menor número: {cores.ROXO_BOLD}{menor}")
    print(f"{cores.CINZA_BOLD}Maior número: {cores.ROXO_BOLD}{maior}")
    print(f"{cores.CINZA_BOLD}{'=' * 38}{cores.LIMPAR}")

print(f"{cores.ROXO_BACKGROUND}Detector de Menor e Maior!{cores.LIMPAR}")
numeros = pedir_numeros()
exibir_resultados()