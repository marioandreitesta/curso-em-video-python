# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa;
# Pergunte o valor da casa, o salário do comprador do comprador e em quantos anos ele vai pagar;
# A prestação mensal não pode exceder 30% do seu salário ou então empréstimo será negado. 

ANO = 12
print("CONSULTOR DE EMPRÉSTIMO BANCÁRIO")

def consultar_valor_imovel() -> float:
    while True:
        try:
            valor_imovel = float(input("Digite o valor do imóvel desejado: "))
            if valor_imovel <= 0:
                print("🚫 | Valor inválido, tente novamente!")
            else:
                return valor_imovel
        except ValueError:
            print("⚠️ | Apenas números são permitidos!")

def consultar_renda() -> float:
    while True:
        try:
            renda_comprador = float(input("Informe sua renda mensal: "))
            if renda_comprador <= 0:
                print("🚫 | Valor inválido, tente novamente!")
            else:
                return renda_comprador
        except ValueError:
            print("⚠️ | Apenas números são permitidos!")

def avaliar_prazo_pagamento() -> int:
    while True:
        try:
            prazo_pagamento = int(input("Informe em quantos anos deseja pagar o imóvel: "))
            if prazo_pagamento <= 0:
                print("🚫 | Valor inválido, tente novamente!")
            elif prazo_pagamento > 8:
                print("❌ | Prazo limite excedido, tente novamente.")
            else:
                return prazo_pagamento
        except ValueError:
            print("⚠️ | Apenas números são permitidos!")

def avaliar_emprestimo(valor_imovel: float, renda_comprador: float, prazo_pagamento: int) -> tuple[int, float] | None:
    limite_prestacoes: float = renda_comprador * 0.30
    prestacoes_imovel: float = valor_imovel / (prazo_pagamento * ANO)
    if prestacoes_imovel > limite_prestacoes:
        print("❌ | Empréstimo negado!")
        return None
    return prazo_pagamento, prestacoes_imovel

def exibir_resultado(valor_imovel: float, renda_comprador: float, prazo_pagamento: int, prestacoes_imovel: float) -> None:
    print("✔️ | Empréstimo Aprovado!")
    print(f"Valor do imóvel   : R${valor_imovel:.2f}")
    print(f"Renda mensal      : R${renda_comprador:.2f}")
    print(f"Prazo de pagamento: {prazo_pagamento} anos")
    print(f"Prestações        : R${prestacoes_imovel:.2f}")

valor_imovel: float    = consultar_valor_imovel()
renda_comprador: float = consultar_renda()
prazo_pagamento: int = avaliar_prazo_pagamento()

resultado: tuple[int, float] | None = avaliar_emprestimo(valor_imovel, renda_comprador, prazo_pagamento)

if resultado is not None:
    prazo, prestacoes = resultado
    exibir_resultado(valor_imovel, renda_comprador, prazo, prestacoes)
