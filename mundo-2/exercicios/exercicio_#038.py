# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

def receber_numeros() -> list[int]:
    
    while True:
        
            entrada: str = input("Digite dois números inteiros separados por espaço: ")
            lista: list[str] = entrada.split()

            if len(lista) != 2:
                print(f"❌| Você digitou {len(lista)}, é preciso de dois números")
                continue

            try:
                numeros: list[int] = list(map(int, lista))
                return numeros

            except ValueError:
              print("❌| Use apenas números. Ex: 10, 2")


def comparar_numeros(numeros: list[int]) -> tuple[int, int]:

    primeiro_num: int = numeros[0]
    segundo_num: int = numeros[1]
            
    if  primeiro_num > segundo_num:
        maior_num: int = primeiro_num
        menor_num: int = segundo_num
    elif primeiro_num < segundo_num:
        maior_num: int = segundo_num
        menor_num: int = primeiro_num
    else:
        print("❌| Não existe valor maior, ambos são iguais.")

    return maior_num, menor_num


def exibir_resultado(numeros: list[int], maior_num, menor_num) -> None:
    
    DIV = 40

    print("=" * DIV)
    print("COMPARAÇÃO ENTRE DOIS NÚMEROS".center(DIV))
    print("=" * DIV)
    print(f"Números escolhidos: {numeros}")
    print(f"O maior número é: {maior_num}")
    print(f"O menor número é: {menor_num}")

numeros: list[int] = receber_numeros()
resultado: tuple[int, int] = comparar_numeros(numeros)


if resultado is not None:
    maior_num, menor_num = resultado
    exibir_resultado(numeros, maior_num, menor_num)
