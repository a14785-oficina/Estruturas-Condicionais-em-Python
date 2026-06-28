# TP01 — Introdução à Programação e Python

**Disciplina:** Programação e Sistemas de Informação (PSI) — Módulo 3
**Trabalho Prático:** 01
**Turma:** 1.º I — N.º 14785
**Ano Letivo:** 2025/2026

Primeiros passos em Python: saída de dados, entrada de dados, tipos de variáveis e operações aritméticas simples.

---

## Ficheiros

| Ficheiro | Enunciado |
|---|---|
| `01.py` | Escrever "Hello World", nome, curso e escola |
| `02.py` | Pedir nome e idade — mensagem personalizada e tipos de variáveis |
| `03.py` | Pedir ano de nascimento — calcular e mostrar a idade |

---

## Exercícios

### 01.py — Hello World e Identificação

Enunciado: Criar um programa que escreva Hello World, Olá Mundo, o teu nome, o teu curso e a tua escola.

```python
print("Hello World!")
print("Ola Mundo!")
print("---")
print("Joao Paulo")
print("GPSI")
print("OFICINA")
```

---

### 02.py — Nome, Idade e Tipos

Enunciado: Criar um programa que pergunte o nome e a idade, mostre uma mensagem personalizada e indique o tipo de cada variável.

```python
nome = input("Qual e o teu nome? ")
print("Nome introduzido: ", nome)
print("---")
idade = input("Quantos anos tens? ")
print("Idade introduzida: ", idade)
print("---")
print("Ola,", nome, "tens", idade, "anos!")
print("---")
print("Tipo de nome: ", type(nome))
print("Tipo de idade: ", type(idade))
```

Nota: `input()` devolve sempre `str`, mesmo quando o utilizador introduz um número.

---

### 03.py — Ano de Nascimento e Cálculo de Idade

Enunciado: Criar um programa que pergunte o nome e o ano de nascimento e calcule a idade aproximada usando `int()`.

```python
nome = input("Qual e o teu nome? ")
print("Nome introduzido: ", nome)
print("---")
ano_nascimento = input("Em que ano nasceste? ")
print("Ano de nascimento introduzido: ", ano_nascimento)
print("---")
print("Ola", nome, ", nasceste no ano", ano_nascimento, "!")
print("---")
print("Ola,", nome, "tens", 2026 - int(ano_nascimento), "anos!")
print("---")
print("Tipo de nome: ", type(nome))
print("Tipo de ano_nascimento: ", type(ano_nascimento))
```

Nota: `int(ano_nascimento)` converte a string para inteiro. Sem esta conversão, `2026 - ano_nascimento` geraria um `TypeError`.

---

## Conceitos Abordados

| Conceito | Descrição |
|---|---|
| `print()` | Saída de dados para a consola |
| `input()` | Entrada de dados — devolve sempre `str` |
| `type()` | Devolve o tipo de uma variável |
| `int()` | Converte string para inteiro |
| Concatenação | Junção de strings e variáveis com `,` |
| Aritmética | Subtração: `2026 - int(ano)` |

---

## Como Executar

Pré-requisito: Python 3.x — [python.org](https://www.python.org/)

```bash
git clone https://github.com/a14785-oficina/introducao-ao-python.git
cd introducao-ao-python
python3 01.py
```

---

## Navegação — Módulo 3

| Posição | Repositório |
|---|---|
| Seguinte | [TP02 — Variáveis e Tipos de Dados](https://github.com/a14785-oficina/variaveis-e-tipos-de-dados) |
| Portfólio | [oficina-jpc](https://github.com/a14785-oficina/oficina-jpc) |

---

*PSI — Módulo 3 — Programação Estruturada — OFICINA — 2025/2026*
