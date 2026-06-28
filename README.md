# EXPA01 — Exercícios de Estruturas Condicionais em Python

**Disciplina:** Programação e Sistemas de Informação (PSI) — Módulo 3
**Exercício Prático:** 01
**Turma:** 1.º I — N.º 14785
**Ano Letivo:** 2025/2026

15 exercícios organizados em três níveis de dificuldade, centrados em estruturas condicionais `if / elif / else`. O programa apresenta um menu e executa cada exercício com interação do utilizador.

---

## Ficheiros

| Ficheiro | Descrição |
|---|---|
| `Exercicio Pratico 01 - Modulo 3 - Estruturas Condicionais em Python.py` | Programa completo com menu e todos os 15 exercícios |
| `README.md` | Este ficheiro |

---

## Exercícios

### Nível Básico

| Código | Título | Descrição |
|---|---|---|
| B1 | Número Positivo ou Negativo | Classifica um número como positivo, negativo ou zero |
| B2 | Maior de Idade | Verifica se o utilizador tem 18 ou mais anos |
| B3 | Número Par ou Ímpar | Usa `%` para determinar paridade |
| B4 | Comparação de Dois Números | Indica qual dos dois números é maior |
| B5 | Password Simples | Valida acesso com a password `"python"` |

### Nível Intermédio

| Código | Título | Descrição |
|---|---|---|
| I1 | Classificação de Nota | Excelente (>=18) — Bom (>=14) — Suficiente (>=10) — Reprovado (<10) |
| I2 | Classificação de Idade | Criança / Jovem / Adulto / Sénior (com validação acima de 120 anos) |
| I3 | Múltiplo de 3 e 5 | Verifica múltiplos de 3, de 5, de ambos ou de nenhum |
| I4 | Login com Utilizador e Password | Autenticação com `admin` / `1234` |
| I5 | Número dentro de Intervalo | Verifica se um número está entre 10 e 20 (inclusivo) |

### Nível Avançado

| Código | Título | Descrição |
|---|---|---|
| A1 | Sistema Multibanco Simples | Saldo inicial 1000 euros — verifica se o levantamento é possível |
| A2 | Maior de Quatro Números | Determina o maior entre 4 valores sem `max()` |
| A3 | Classificação de IMC | `IMC = peso / altura²` — 4 categorias clínicas |
| A4 | Sistema de Desconto | 10% (>=100 euros) — 5% (>=50 euros) — 0% (<50 euros) |
| A5 | Verificação de Ano Bissexto | Determina se um ano é bissexto (divisível por 4) |

---

## Conceitos Abordados

```python
# Estrutura base
if condicao:
    ...
elif outra_condicao:
    ...
else:
    ...

# Operadores utilizados
>    >=    <    <=    ==    !=       # relacionais
and    or    not                    # lógicos
%                                   # módulo — paridade e múltiplos
10 <= valor <= 20                   # encadeamento de comparações (I5)

# Fórmula IMC (A3)
imc = peso / (altura * altura)
```

---

## Como Executar

Pré-requisito: Python 3.x — [python.org](https://www.python.org/)

```bash
git clone https://github.com/a14785-oficina/exercicios-estruturas-condicionais.git
cd exercicios-estruturas-condicionais
python3 "Exercicio Pratico 01 - Modulo 3 - Estruturas Condicionais em Python.py"
```

---

## Navegação — Módulo 3

| Posição | Repositório |
|---|---|
| Anterior | [TP04 — Estruturas Condicionais](https://github.com/a14785-oficina/estruturas-condicionais) |
| Seguinte | [EXPA02 — Ciclos While e For](https://github.com/a14785-oficina/ciclos-while-e-for) |
| Portfólio | [oficina-jpc](https://github.com/a14785-oficina/oficina-jpc) |

---

*PSI — Módulo 3 — Programação Estruturada — OFICINA — 2025/2026*
