# Boas Práticas em Python para Iniciantes

Este guia apresenta as principais convenções e boas práticas para escrever código Python limpo e organizado, seguindo o guia de estilo oficial (PEP 8).

---

## 1. Como Separar e Organizar o Código

### Espaços em Branco

- Use **4 espaços** (não tabulação) para indentar o código.
- Deixe **duas linhas em branco** entre definições de funções e classes de nível superior.
- Deixe **uma linha em branco** entre métodos dentro de uma classe.
- Use espaços ao redor de operadores (`=`, `+`, `==`, etc.):

```python
# Correto
x = 1 + 2
nome = "Maria"

# Incorreto
x=1+2
nome="Maria"
```

### Quebras de Linha

- Linhas devem ter no máximo **79 caracteres** (para facilitar a leitura).
- Para dividir uma linha longa, use parênteses ou `\`:

```python
# Correto
frase = (
    "Esta é uma frase muito longa que precisa "
    "ser dividida em várias linhas."
)

# Ou
total = 1 + 2 + 3 + 4 + \
        5 + 6 + 7
```

---

## 2. Como Criar Constantes

No Python, não existem constantes verdadeiras (imutáveis por padrão), mas a convenção é:

- Escreva os nomes das constantes em **MAIÚSCULAS** com `_` separando palavras.
- Geralmente, constantes ficam no **topo do arquivo**.

```python
# Constantes no topo do arquivo
PI = 3.14159
TAXA_JUROS = 0.05
CAMINHO_ARQUIVO = "dados/usuarios.txt"
MAX_TENTATIVAS = 3

# Uso no código
raio = 5
area = PI * raio ** 2
```

**Importante:** O Python não impede que você mude o valor da constante, mas o uso de MAIÚSCULAS avisa a outros programadores que aquele valor não deve ser alterado.

---

## 3. Como Criar Funções

### Estrutura Básica

Use a palavra-chave `def`, seguida do nome da função em **letras minúsculas** com `_` separando palavras (snake_case):

```python
def saudacao(nome):
    """Exibe uma saudação personalizada."""
    print(f"Olá, {nome}!")
```

### Nomeando Funções

- Use **snake_case**: `calcular_media`, `exibir_resultado`, `validar_entrada`.
- O nome deve ser **descritivo** — diga o que a função faz.
- Verbos são bem-vindos: `get_`, `calcular_`, `verificar_`, `exibir_`.

```python
# Correto
def calcular_area_circulo(raio):
    return 3.14159 * raio ** 2

# Incorreto (não descritivo)
def func1(r):
    return 3.14159 * r ** 2
```

### Funções com Múltiplos Argumentos

```python
def calcular_media(nota1, nota2, nota3):
    """Calcula a média de três notas."""
    media = (nota1 + nota2 + nota3) / 3
    return media

resultado = calcular_media(7.5, 8.0, 9.5)
print(resultado)
```

### Valores Padrão (Default Arguments)

```python
def exibir_mensagem(texto, vezes=1):
    """Exibe uma mensagem uma ou mais vezes."""
    for _ in range(vezes):
        print(texto)

exibir_mensagem("Olá")            # Imprime uma vez
exibir_mensagem("Oi", vezes=3)    # Imprime três vezes
```

### Documentação (Docstrings)

Adicione uma string de documentação logo após `def` para explicar o que a função faz:

```python
def somar(a, b):
    """
    Soma dois números e retorna o resultado.

    Parâmetros:
        a (int/float): Primeiro número.
        b (int/float): Segundo número.

    Retorna:
        int/float: Soma de a e b.
    """
    return a + b
```

---

## 4. Comentários

- Comentários devem ser frases completas e úteis.
- Use `#` seguido de um espaço.
- Evite comentários óbvios.

```python
# Correto
# Calcula o desconto de 10% sobre o valor total
desconto = valor * 0.10

# Incorreto (comentário óbvio)
# Soma a e b
soma = a + b
```

---

## 5. Organização Geral de um Arquivo Python

A ordem recomendada de um arquivo Python é:

```
1. Shebang (opcional):       #!/usr/bin/env python3
2. Docstring do módulo
3. Imports (bibliotecas)
4. Constantes
5. Definição de funções
6. Código principal (main)
```

Exemplo de estrutura completa:

```python
#!/usr/bin/env python3
"""
Módulo para cálculos matemáticos básicos.
"""

# Imports
import math

# Constantes
PI = 3.14159
GRAVIDADE = 9.81

# Funções
def calcular_area_circulo(raio):
    """Retorna a área de um círculo."""
    return PI * raio ** 2

def calcular_velocidade(distancia, tempo):
    """Retorna a velocidade média."""
    return distancia / tempo

# Código principal
if __name__ == "__main__":
    raio = 5
    area = calcular_area_circulo(raio)
    print(f"A área do círculo é: {area}")
```

---

## Resumo das Convenções

| O que é | Convenção | Exemplo |
|---------|-----------|---------|
| Função | `snake_case` | `calcular_media()` |
| Constante | `MAIÚSCULAS` | `TAXA_JUROS = 0.05` |
| Variável | `snake_case` | `nome_usuario = "Ana"` |
| Indentação | 4 espaços | `    print("oi")` |
| Arquivo | `snake_case` | `meu_script.py` |

---

*Baseado na PEP 8 — Guia de Estilo para Python*
