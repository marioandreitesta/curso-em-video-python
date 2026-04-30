# 🐍 Curso em Vídeo — Python 3

> Repositório de estudos Python — Curso em Vídeo (Guanabara) | Exercícios, anotações e projetos

Documentação da minha jornada pelo curso de Python 3 do professor **Gustavo Guanabara**, disponível gratuitamente pelo [Curso em Vídeo](https://www.cursoemvideo.com/). Este repositório não é apenas um arquivo de exercícios resolvidos — é um registro de evolução, onde cada commit conta uma parte do processo de aprendizado.

Alguns exercícios vão além do proposto nas aulas. Por curiosidade e autodidatismo, foram aplicados recursos como tratamento de erros com `try/except`, validação de entradas, tipagem explícita, modularização e boas práticas de código limpo — conceitos que, embora não sejam requisito do curso naquele ponto, fazem parte de uma postura ativa diante do aprendizado.

---

## 🛠️ Tecnologias e Ferramentas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![VSCode](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Ruff](https://img.shields.io/badge/Ruff-D7FF64?style=for-the-badge&logo=ruff&logoColor=black)
![Claude](https://img.shields.io/badge/Claude-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=google-gemini&logoColor=white)

**Extensões VSCode:** ZubanLS · GitLens · Git Graph

---

## 📚 Sobre o Curso em Vídeo — Python 3

O curso de Python 3 do professor Gustavo Guanabara é uma das referências mais completas e acessíveis para quem está começando na linguagem. Estruturado em quatro módulos progressivos chamados de **Mundos**, o curso conta com mais de 100 exercícios práticos e aulas teóricas bem fundamentadas.

Cada Mundo representa uma camada de profundidade maior na linguagem:

**Mundo 1 — Fundamentos**
Introdução à linguagem Python: tipos primitivos, operadores, entrada e saída de dados, manipulação de strings e primeiros programas. A base para tudo que vem depois.

**Mundo 2 — Estruturas de Controle**
Estruturas de decisão e repetição: `if`, `elif`, `else`, `for`, `while`. O Mundo que ensina o programa a tomar decisões e repetir ações de forma controlada.

**Mundo 3 — Estruturas Compostas**
Tuplas, listas, dicionários, funções, módulos, pacotes e tratamento de erros. A linguagem ganha profundidade e os programas começam a ganhar arquitetura real.

**Mundo 4 — Avançado**
Orientação a Objetos, herança, polimorfismo e conceitos avançados da linguagem. O ponto onde Python revela sua verdadeira expressividade.

Cada Mundo neste repositório contém:
- 📝 `anotacoes/` — resumos teóricos e material de estudo em Markdown
- 💻 `exercicios/` — todos os desafios resolvidos
- 📓 `notebooks/` — notebooks Jupyter com explicações aprofundadas
- 🔧 `refatorações/` — versões melhoradas de exercícios selecionados

---

## 🎯 Objetivo

O objetivo deste repositório é seguir uma linha clara e honesta de aprendizado — sem pular etapas, sem subestimar o simples e sem superestimar o complexo.

Há uma tentação recorrente no aprendizado autodidata de buscar atalhos ou queimar fases por impaciência. Este repositório existe justamente como resistência a esse impulso. Como escreve Robert C. Martin em *Clean Code*: um código bem escrito não é aquele que funciona — é aquele que pode ser lido, entendido e mantido. Essa premissa guia cada exercício aqui registrado, mesmo os mais básicos.

O progresso é documentado com honestidade: o que foi proposto, o que foi entregue, e o que foi além.

---

## 🗺️ Marcos da Jornada

| Mundo | Tema | Status |
|-------|------|--------|
| Mundo 1 | Fundamentos | ✅ Concluído |
| Mundo 2 | Estruturas de Controle | 🔄 Em andamento |
| Mundo 3 | Estruturas Compostas | ⏳ Pendente |
| Mundo 4 | Avançado | ⏳ Pendente |

---

## 📁 Estrutura do Repositório

```
curso-em-video-python/
│
├── mundo-1/
│   ├── anotacoes/          # Resumos teóricos em Markdown
│   ├── exercicios/         # Exercícios resolvidos (#003 ao #035)
│   ├── notebooks/          # Notebooks Jupyter com explicações
│   └── refatorações/       # Versões melhoradas de exercícios
│
├── mundo-2/
│   ├── anotacoes/
│   ├── exercicios/
│   ├── notebooks/
│   └── refatorações/
│
├── mundo-3/                # ⏳ Em breve
└── mundo-4/                # ⏳ Em breve
```

---

## 📋 Norma de Commits

Para manter um histórico de evolução claro e rastreável, todos os commits seguem o padrão **Conventional Commits** adaptado para este repositório.

### Estrutura

```
<tipo>(<escopo>): <descrição curta no imperativo>
```

### Tipos Permitidos

| Tipo | Uso |
|------|-----|
| `estudo` | Adição de anotações, resumos ou conteúdo teórico |
| `exercicio` | Novo exercício resolvido |
| `projeto` | Criação ou atualização de um projeto |
| `refactor` | Refatoração de código existente |
| `fix` | Correção de erro em código ou anotação |
| `docs` | Alterações em documentação (README, comentários) |
| `sql` | Conteúdo relacionado a banco de dados e SQL |
| `poo` | Conteúdo relacionado a Orientação a Objetos |
| `chore` | Tarefas de organização, renomeação de arquivos etc. |

### Exemplos de Commits Reais

```bash
exercicio(#035): analisando triângulo v1.0
refactor(exercicio_#034): adiciona cores ANSI
refactor(exercicio_#029): adiciona proteções, try catch e entrada por usuário
fix(exercicio_#008): corrige localização de constante e output
estudo(anotacoes): adiciona material de boas práticas em python
docs(exercicios): adiciona cores.py
chore(exercicio_#008): organização de variável
```

---

## 🔍 Como Consultar Este Repositório

Este repositório pode ser útil para quem está fazendo o mesmo curso e quer comparar abordagens ou entender soluções alternativas.

**Para navegar pelos exercícios:**
1. Acesse a pasta do Mundo correspondente à sua etapa no curso
2. Os exercícios seguem a numeração original do curso (`exercicio_#003.py`, `exercicio_#004.py`, etc.)
3. O arquivo `cores.py` em `mundo-1/exercicios/` é um módulo auxiliar com constantes ANSI — necessário para rodar os exercícios com cores no terminal

**Para rodar localmente:**
```bash
git clone https://github.com/marioandreitesta/curso-em-video-python.git
cd curso-em-video-python
python mundo-1/exercicios/exercicio_#003.py
```

**Sugestões e correções** são bem-vindas via Issues ou Pull Requests. Se encontrar uma abordagem mais elegante ou identificar algum erro, fique à vontade para abrir uma discussão.

---

## 📬 Contato

<a href="https://github.com/marioandreitesta">
  <img src="https://img.shields.io/badge/GitHub-marioandreitesta-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>
<a href="https://www.linkedin.com/in/marioandreitesta/">
  <img src="https://img.shields.io/badge/LinkedIn-Mario%20Andrei-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

---

<p align="center">
  <sub>Feito com consistência, curiosidade e muitos commits corrigidos. 🐍</sub>
</p>
