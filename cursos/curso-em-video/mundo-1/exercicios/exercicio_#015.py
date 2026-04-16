# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 centavos por Km rodado. 

print("Calculadora de Gastos (Aluguel de Carros)")

dias_alugados = int(input("Para começar, informe quantos dias você alugou o carro: "))
km_percorridos = float(input("Agora, digite quantos quilômetros você percorreu: "))

print("Estamos calculando o seu gasto...")
print("-" * 40)

preco_diaria = 60
preco_km = 0.15

custo_aluguel = dias_alugados * preco_diaria
custo_quilometragem = km_percorridos * preco_km
custo_total = custo_aluguel + custo_quilometragem

print(f"Você alugou o carro por {dias_alugados} dias, pelo valor de R${preco_diaria:.2f}")
print(f"O custo do aluguel é: R${custo_aluguel:.2f}")
print(f"O custo por quilômetros rodados é: R${custo_quilometragem:.2f}")
print(f"Custo final: R${custo_total:.2f}")

