# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

def receber_numero() -> int:

    while True:
        
        try:
            numero = int(input("Digite um número inteiro: "))
            return numero
        
        except ValueError:
            print("❌| Apenas números inteiros são permitidos!")

def converter_numero(numero: int) -> tuple[int, str]:

    while True:

        try:
            base_conversao = int(input("Escolha a base númerica: "))
            
            binario: str = bin(numero)
            octal: str = oct(numero)
            hexadecimal: str = hex(numero)

            if base_conversao == 1:
                print("Formato Binário!")
                numero_convertido: str = binario
            elif base_conversao == 2:
                print("Fomarto Octal!")
                numero_convertido = octal
            elif base_conversao == 3:
                print("Foarmato Hexadecimal!")
                numero_convertido = hexadecimal
            else:
                print("❌| Escolha entre as opções: [1], [2] e [3]")

            return base_conversao, numero_convertido

        except ValueError:
            print("❌| Apenas números são aceitos nesse campo!")

def exibir_resultado(numero: int, base_conversao: int, numero_convertido: str) -> None:

    print("=" * 55)
    print("CONVERSOR DE NÚMEROS: BINÁRIO, OCTAL & HEXADECIMAL".center(55))
    print("=" * 55)
    print(f"Número escolhido: {numero}")
    print(f"Base selecionada: {base_conversao}")
    print(f"Número convertido: {numero_convertido}")

numero: int = receber_numero()
base_conversao, numero_convertido = converter_numero(numero)
exibir_resultado(numero, base_conversao, numero_convertido)