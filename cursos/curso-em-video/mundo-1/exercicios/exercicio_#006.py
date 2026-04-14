# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

print("Digite um número para ver seu dobro, triplo e raiz quadrada.")

numero = int(input("Digite o número: "))

dobro = numero * 2 
triplo = numero * 3
raiz_quadrada = numero ** 0.5

print("Analisamos o número informado:")
print(f"Dobro: {dobro}")
print(f"Triplo: {triplo}")
print(f"Raiz quadrada: {raiz_quadrada:.0f}")
