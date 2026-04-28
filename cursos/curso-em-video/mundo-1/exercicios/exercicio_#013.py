# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. 

print("Programa de Reajuste Salarial!")

salario_atual = float(input("Digite o seu salário atual: R$"))

print("Reajustando seu salário...")

reajuste_salario = salario_atual * 1.15

print("O seu salário recebeu um aumento de [10%]")
print(f"Salário reajustado: R${reajuste_salario:.2f}")