# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print("Calculador de Descontos!")

preco_produto = float(input("Digite o preço do seu produto: R$"))

preco_final = preco_produto * 0.95
desconto = preco_final - preco_produto

print("-" * 40)

print(f"Preço do produto: R${preco_produto:.2f}")
print(f"Desconto (5%): R${desconto:.2f}")
print(f"Valor final: R${preco_final:.2f}")