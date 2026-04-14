# Faça uma programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print("Digite algo para descobrir o tipo primitivo e outras informações sobre ele!")

valor = input("Digite algo: ")

print(f"O tipo primitivo desse valor é: {type(valor)}")
print(f"É alfanumérico? {valor.isalnum()}")
print(f"É alfabético? {valor.isalpha()}")
print(f"É um número? {valor.isnumeric()}")
print(f"É um espaço? {valor.isspace()}")
print(f"Está em maiúsculas? {valor.isupper()}")
print(f"Está em minúsculas? {valor.islower()}")
print(f"Está capitalizada? {valor.istitle()}")
