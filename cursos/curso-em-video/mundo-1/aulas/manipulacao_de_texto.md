# Manipulação de Texto em Python (Strings)

Nesta aula, vamos aprender como o Python lida com textos, que chamamos tecnicamente de **Strings**. Para o Python, uma string é uma cadeia de caracteres em uma sequência ordenada.

---

## 1. Fatiamento de Strings (Slicing)
Fatiar é "pegar pedaços" da string. Imagine que a frase `CURSO EM VIDEO` está em uma grade onde cada letra (incluindo espaços) ocupa uma posição começando do **0**.

```python
frase = 'Curso em Vídeo'
```

*   **`frase[9]`**: Pega o caractere na posição 9 (`V`).
*   **`frase[9:13]`**: Pega do 9 até o 12 (o 13 é excluído). Resultado: `Víde`.
*   **`frase[9:14]`**: Pega do 9 até o 13. Resultado: `Vídeo`.
*   **`frase[0:5:2]`**: Começa no 0, vai até o 4, pulando de 2 em 2. Resultado: `Crs`.
*   **`frase[:5]`**: Começa do início até o 4.
*   **`frase[15:]`**: Começa do 15 e vai até o final.
*   **`frase[9::3]`**: Começa no 9 e vai até o final pulando de 3 em 3.

---

## 2. Análise de Strings
Formas de examinar o conteúdo de uma string.

*   **`len(frase)`**: Comprimento (Length) da string. Quantos caracteres ela tem?
*   **`frase.count('o')`**: Conta quantas vezes a letra 'o' aparece.
*   **`frase.count('o', 0, 13)`**: Conta 'o' do início até a posição 12.
*   **`frase.find('deo')`**: Diz em qual posição começou a sequência 'deo'. Se não encontrar, retorna `-1`.
*   **`'Curso' in frase`**: Retorna `True` ou `False` se a palavra existe na string.

---

## 3. Transformação
Métodos que alteram (momentaneamente) a forma da string.

*   **`frase.replace('Python', 'Android')`**: Substitui uma palavra por outra.
*   **`frase.upper()`**: Tudo em MAIÚSCULAS.
*   **`frase.lower()`**: Tudo em minúsculas.
*   **`frase.capitalize()`**: Só a primeira letra da string fica em maiúscula.
*   **`frase.title()`**: A primeira letra de cada palavra fica em maiúscula.
*   **`frase.strip()`**: Remove todos os espaços inúteis no início e no fim da string.
    *   `frase.rstrip()`: Remove espaços apenas da direita (Right).
    *   `frase.lstrip()`: Remove espaços apenas da esquerda (Left).

---

## 4. Divisão e Junção
Lidando com as palavras separadamente.

*   **`frase.split()`**: Divide a string em uma lista de palavras, baseando-se nos espaços.
    *   Ex: `['Curso', 'em', 'Vídeo']`
*   **`'-'.join(frase)`**: Junta os elementos de uma lista usando o separador '-' (ou qualquer outro).
    *   Ex: `Curso-em-Vídeo`

---

## Dica de Ouro: Imutabilidade
As strings em Python são **imutáveis**. Isso significa que se você fizer `frase.upper()`, a variável `frase` original continua igual. Para mudar de verdade, você precisa atribuir o resultado de volta:
`frase = frase.upper()`
