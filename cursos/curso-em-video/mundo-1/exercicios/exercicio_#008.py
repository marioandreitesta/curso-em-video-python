# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. 

print("Conversor de Metros!")

metros = float(input("Digite a metragem que deseja converter: "))
centimetros = metros * 100
milimetros = metros * 1000

print(f"{metros:.0f} metro(s) em:")
print(f"Centímetros: {centimetros:.0f}cm")
print(f"Milímetros: {milimetros:.0f}mm")