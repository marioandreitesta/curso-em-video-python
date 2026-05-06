""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou o tempo de alistamento.
Seu programa deverá mostrar o tempo que falta ou que passou do prazo. """

ANO_ATUAL = 2026

def receber_ano_nascimento() -> int:
    
    while True:
        
        try:
            ano_nasc = int(input("Informe seu ano de nascimento: "))
            limite_nasc: int =  1931
            
            if ano_nasc >= ANO_ATUAL or ano_nasc < limite_nasc:
                print("❌| Data inválida...")
            else:
                return ano_nasc

        except ValueError:
            print("❌| Isto não é um número!")

def validar_servico_militar(ano_nasc: int) -> None:

    idade_usuario: int = ANO_ATUAL - ano_nasc
    diferenca_anos: int = abs(18 - idade_usuario)

    if idade_usuario == 18:
        return print("É hora do alistamento, procura a Junta de Serviço Militar mais próxima!")
    elif idade_usuario > 18:
        return print(f"Prazo ultrapassado há {diferenca_anos}, compareça imediatamente a uma Junta de Serviço Militar.")
    else:
        return print(f"Idade insuficiente para alistamento, falta {diferenca_anos} ano(s) para o alistamento.")
  

ano_nasc: int = receber_ano_nascimento()
validar_servico_militar(ano_nasc)