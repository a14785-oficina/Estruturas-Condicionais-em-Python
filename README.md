# TP01 -- Introducao a Programacao e Python

**Disciplina:** Programacao e Sistemas de Informacao (PSI) -- Modulo 3
**Trabalho Pratico:** 01
**Turma:** 1.o I -- N.o 14785
**Ano Letivo:** 2025/2026

Primeiros passos em Python: saida de dados, entrada de dados, tipos de variaveis e operacoes aritmeticas simples.

---

## Ficheiros

| Ficheiro | Enunciado |
|---|---|
| `01.py` | Escrever "Hello World", nome, curso e escola |
| `02.py` | Pedir nome e idade -- mensagem personalizada e tipos de variaveis |
| `03.py` | Pedir ano de nascimento -- calcular e mostrar a idade |

---

## Exercicios

### 01.py -- Hello World e Identificacao

Enunciado: Criar um programa que escreva Hello World, Ola Mundo, o teu nome, o teu curso e a tua escola.

```python
print("Hello World!")
print("Ola Mundo!")
print("---")
print("Joao Paulo")
print("GPSI")
print("OFICINA")
```

---

### 02.py -- Nome, Idade e Tipos

Enunciado: Criar um programa que pergunte o nome e a idade, mostre uma mensagem personalizada e indique o tipo de cada variavel.

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

Nota: `input()` devolve sempre `str`, mesmo quando o utilizador introduz um numero.

---

### 03.py -- Ano de Nascimento e Calculo de Idade

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

Nota: `int(ano_nascimento)` converte a string para inteiro. Sem esta conversao, `2026 - ano_nascimento` geraria um `TypeError`.

---

## Conceitos Abordados

| Conceito | Descricao |
|---|---|
| `print()` | Saida de dados para a consola |
| `input()` | Entrada de dados -- devolve sempre `str` |
| `type()` | Devolve o tipo de uma variavel |
| `int()` | Converte string para inteiro |
| Concatenacao | Juncao de strings e variaveis com `,` |
| Aritmetica | Subtracao: `2026 - int(ano)` |

---

## Como Executar

Pre-requisito: Python 3.x -- [python.org](https://www.python.org/)

```bash
git clone https://github.com/a14785-oficina/Trabalho-Pratico-01-M3.git
cd Trabalho-Pratico-01-M3
python3 01.py
```

---

## Navegacao -- Modulo 3

| Posicao | Repositorio |
|---|---|
| Anterior | Inicio do Modulo 3 |
| Seguinte | [TP02 -- Variaveis e Tipos de Dados](https://github.com/a14785-oficina/Trabalho-Pratico-02-M3) |
| Portfolio | [oficina-jpc](https://github.com/a14785-oficina/oficina-jpc) |

---

*PSI -- Modulo 3 -- Programacao Estruturada -- OFICINA -- 2025/2026*
