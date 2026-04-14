# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 

print("Veja quantos dólares você consegue comprar na cotação atual!")

saldo_reais = int(input("Insira seu saldo atual: R$"))

cotacao_dolar = 4.98 # Cotação da data 14/04/2026
saldo_convertido = saldo_reais / cotacao_dolar

print(f"Com R${saldo_reais:.2f}, você consegue comprar: ${saldo_convertido:.2f}")
