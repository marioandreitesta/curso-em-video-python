# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 centavos por Km rodado.
# REFATORADO - MELHORADO A APRESENTAÇÃO E ORGANIZAÇÃO DO CÓDIGO

PRECO_DIA = 60.00
PRECO_KM = 0.15

print("="*40)
print(f"{'LOCADORA DE VEÍCULOS':^40}") 
print("="*40)

dias = int(input("Quantidade de dias de aluguel: "))
km = float(input("Quantidade de Km percorridos: "))

pago_dias = dias * PRECO_DIA
pago_km = km * PRECO_KM
total = pago_dias + pago_km

print("-" * 40)
print("Resumo do Aluguel:")
print(f"-> {dias} dias (R${PRECO_DIA:.2f}/dia): R${pago_dias:>10.2f}")
print(f"-> {km:.1f} Km (R${PRECO_KM:.2f}/Km): R${pago_km:>10.2f}")
print("-" * 40)
print(f"TOTAL A PAGAR: R${'R$':>15}{total:.2f}")

# Refatoração feita com base em sugestões de LLM (Gemini 3 Flash)
# Código original em: exercicios/exercicio#015.py
