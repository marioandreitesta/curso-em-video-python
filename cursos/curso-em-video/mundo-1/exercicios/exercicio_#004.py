# Faça uma programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

import cores

def colorir_booleano(valor_booleano):
    if valor_booleano:
        return f"{cores.VERDE_BOLD}True{cores.LIMPAR}"
    else:
        return f"{cores.VERMELHO_BOLD}False{cores.LIMPAR}"

print(f"{cores.PRETO_BACKGROUND}Digite algo para descobrir o tipo primitivo e outras informações sobre ele!{cores.LIMPAR}")

valor = input("Digite algo: ")

print(f"O tipo primitivo desse valor é: {colorir_booleano(valor.isalpha())}")
print(f"É alfanumérico? {colorir_booleano(valor.isalnum)}")
print(f"É alfabético? {colorir_booleano(valor.isalpha())}")
print(f"É um número? {colorir_booleano(valor.isnumeric())}")
print(f"É um espaço? {colorir_booleano(valor.isspace())}")
print(f"Está em maiúsculas? {colorir_booleano(valor.isupper())}")
print(f"Está em minúsculas? {colorir_booleano(valor.islower())}")
print(f"Está capitalizada? {colorir_booleano(valor.istitle())}")
