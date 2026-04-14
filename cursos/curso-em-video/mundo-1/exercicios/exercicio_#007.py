# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print("Digite a nota do aluno para saber sua média!")

primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))
resultado_soma = (primeiraNota + segundaNota) / 2

print("Calculamos sua média:")
print(f"A média desse aluno é {resultado_soma:.1f}")