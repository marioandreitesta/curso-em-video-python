# Escreva um programa que converta uma temperatura digitando em graus Celcius e converta para graus Fahrenheit. 

print("Conversor de Celsius para Fahrenheit!")

graus_celsius = float(input("Digite a temperatura [C°]:"))
graus_fahrenheit = (graus_celsius * 1.8) + 32

print(f"Temperatura em graus Fahrenheit: {graus_fahrenheit:.1f}°F")
