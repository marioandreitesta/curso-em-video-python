# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite. 

DIV = 30
LIMITE_RADAR = 80
VALOR_POR_KM = 7

print('=' * DIV)
print('RADAR DE VELOCIDADE 80KM/H'.center(DIV))
print('=' * DIV)

try:
    velocidade = float(input('Digite a velocidade do carro [Km/h]: '))
    print('-' * DIV)


    if velocidade > LIMITE_RADAR:
        excesso = velocidade - LIMITE_RADAR
        multa = excesso * VALOR_POR_KM
        print(f'Você ultrapassou o limite de velocidade! [{velocidade:.0f}Km/h]')
        print(f'O valor de sua multa é: R${multa:.2f}')
    elif velocidade <= 0:
        print('Error: Velocidade inválida!')
    else:
        print('Tenha uma boa viagem!')
except ValueError:
    print('Oops! Isso não é um número, tente novamente!')

# Refatorei usando um padrão do curso, que é receber os dados do usuário; (Linha 14)
# Adicionei uma proteção contra números negativos e inercia; (Linha 23)
# Adicionei um try catch para imprimir uma mensagem quando o valor não for número. (Linha 13 à 28)