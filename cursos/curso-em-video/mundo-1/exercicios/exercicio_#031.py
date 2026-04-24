# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas. 

DIV = 29
CUSTO_KM = 0.50
CUSTO_KM_PROMO = 0.45

print('CALCULE O CUSTO DE SUA VIAGEM'.center(DIV))
print('-' * DIV)

try:
    distancia = float(input('Digite a distância [Km]: '))

    if distancia <= 200:
        custo_viagem = distancia * CUSTO_KM
        print(f'O custo da sua viagem é: R${custo_viagem:.2f}')
    else:
        custo_viagem = distancia * CUSTO_KM_PROMO
        print(f'O custo da sua viagem é: R${custo_viagem:.2f}')
except ValueError:
    print('Error: isso não é um número!')
