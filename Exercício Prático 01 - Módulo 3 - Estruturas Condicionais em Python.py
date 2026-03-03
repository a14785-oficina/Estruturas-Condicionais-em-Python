# Estruturas Condicionais em Python

menu = '''
.............................................................
:                           Menu                            :
:...........................................................:
: -- NÍVEL BÁSICO --                                        :
: Exercício B1 - Número Positivo ou Negativo                :
: Exercício B2 - Maior de Idade                             :
: Exercício B3 - Número Par ou Ímpar                        :
: Exercício B4 - Comparação de Dois Números                 :
: Exercício B5 - Password Simples                           :
: -- INTERMÉDIO --                                          :
: Exercício I1 - Classificação de Nota                      :
: Exercício I2 - Classificação de Idade                     :
: Exercício I3 - Múltiplo de 3 e 5                          :
: Exercício I4 - Login com Utilizador e Password            :
: Exercício I5 - Número dentro de intervalo                 :
: -- NÍVEL AVANÇADO --                                      :
: Exercício A1 - Sistema Multibanco Simples                 :
: Exercício A2 - Maior de Quatro Números                    :
: Exercício A3 - Classificação de IMC (Simplificado)        :
: Exercício A4 - Sistema de Desconto                        :
: Exercício A5 - Verificação de Ano Bissexto (Simplificado) :
:...........................................................: 
'''
print(menu)

# Exercício B1 - Número Positivo ou Negativo
# Criar um programa que:
# Peça um número ao utilizador
# Indique se é positivo ou negativo

print("Exercício B1 - Número Positivo ou Negativo")

b1_num = float(input("Introduza um número: "))

if b1_num > 0:
    print("O número é positivo.")
elif b1_num < 0:
    print("O número é negativo.")
elif b1_num == 0:
    print("O número é zero.")

print("---")

# Exercício B2 - Maior de Idade
# Criar um programa que:
# Peça a idade
# Indique se é maior ou menor de idade
# Regra:
# Maior ou igual a 18 → Maior de idade

print("Exercício B2 - Maior de Idade")

b2_idade = int(input("Introduza a sua idade: "))

if b2_idade >= 18:
    print("É maior de idade.")
else:
    print("É menor de idade.")

print("---")

# Exercício B3 - Número Par ou Ímpar
# Criar um programa que:
# Peça um número
# Indique se é par ou ímpar

print("Exercício B3 - Número Par ou Ímpar")

b3_num = int(input("Introduza um número: "))
print(f"O número introduzido é par? {b3_num % 2 == 0} ({b3_num % 2})")

print("---")

# Exercício B4 - Comparação de Dois Números
# Criar um programa que:
# Peça dois números
# Indique qual é o maior

print("Exercício B4 - Comparação de Dois Números")

b4_num1 = float(input("Introduza o primeiro número: "))
b4_num2 = float(input("Introduza o segundo número: "))

if b4_num1 > b4_num2:
    print(f"O número {b4_num1} é maior.")
elif b4_num2 > b4_num1:
    print(f"O número {b4_num2} é maior.")
else:
    print("Os números são iguais.")

print("---")

# Exercício B5 - Password Simples
# Criar um programa que:
# Peça uma password
# Se for "python" → acesso permitido
# Senão → acesso negado

print("Exercício B5 - Password Simples")

b5_password = input(str("Enter Password: "))

if b5_password == "python":
    print("Acesso permitido.")
else:
    print("Acesso negado.")
print("---")

# Exercício I1 - Classificação de Nota
# Criar um programa que:
# Peça uma nota (0 a 20)
# Mostre:
# >= 18 → Excelente
# >= 14 → Bom
# >= 10 → Suficiente
# < 10 → Reprovado

print("Exercício I1 - Classificação de Nota")

i1_nota = int(input("Nota: "))
print(f"Nota introduzida: {i1_nota}")

if i1_nota >= 18:
    print("Excelente")
elif i1_nota >= 14:
    print("Bom")
elif i1_nota >= 10:
    print("Suficiente")
elif i1_nota >= 0:
    print("Reprovado")
else:
    print("A Nota introduzida é inválida. Por favor, insira um valor entre 0 e 20.")

print("---")

# Exercício I2 - Classificação de Idade
# Criar programa que classifique:
# < 13 → Criança
# 13–17 → Jovem
# 18–64 → Adulto
# 65+ → Sénior

print("Exercício I2 - Classificação de Idade")

i2_idade = int(input("i2_idade: "))
if i2_idade <= 0:
    print("A tua idade humana é imposivel!")
elif i2_idade <= 13:
    print("Tu és uma Criança")
elif i2_idade <= 17:
    print("Tu és um Jovem")
elif i2_idade <= 64:
    print("Tu és um Adulto")
elif i2_idade <= 120:
    print("Tu és um Sénior")
else:
    print("A tua idade humana é icrível! (Sénior com mais de 120 anos)")

print("---")

# Exercício I3 - Múltiplo de 3 e 5
# Criar programa que:
# Peça um número
# Indique:
# Múltiplo de 3
# Múltiplo de 5
# Múltiplo de ambos
# Nenhum

print("Exercício I3 - Múltiplo de 3 e 5")

i3_num = int(input("Introduza um número: "))

if i3_num % 3 == 0 and i3_num % 5 == 0:
    print("O número é múltiplo de ambos (3 e 5).")
elif i3_num % 3 == 0:
    print("O número é múltiplo de 3.")
elif i3_num % 5 == 0:
    print("O número é múltiplo de 5.")
else:
    print("O número não é múltiplo de nenhum.")

print("---")

# Exercício I4 - Login com Utilizador e Password
# Sistema com:
# Utilizador correto: admin
# Password correta: 1234
# Verificar ambos.

print("Exercício I4 - Login com Utilizador e Password")

i4_username = input("User Name: ")
i4_password = input("Password: ")
if i4_username == "admin" and i4_password == "1234":
    print("Login bem-sucedido.")
else:
    print("Login incorreto. Verifique o nome de utilizador e a password.")

print("---")

# Exercício I5 - Número dentro de intervalo
# Criar programa que:
# Peça um número
# Indique se está entre 10 e 20

print("Exercício I5 - Número dentro de intervalo")

i5_num = float(input("Introduza um número: "))
if 10 <= i5_num <= 20:
    print("O número está entre 10 e 20.")
else:
    print("O número não está entre 10 e 20.")

print("---")

# Exercício A1 - Sistema Multibanco Simples
# Criar programa que:
# Defina saldo inicial = 1000
# Peça valor a levantar
# Se saldo suficiente → autorizado
# Senão → saldo insuficiente

print("Exercício A1 - Sistema Multibanco Simples")

a1_saldo = 1000
a1_valor_levantar = float(input("Valor a levantar: "))

if a1_saldo >= a1_valor_levantar:
    print("Levantamento autorizado.")
else:
    print("Saldo insuficiente.")

print("---")

# Exercício A2 - Maior de Quatro Números
# Criar programa que:
# Peça 4 números
# Mostre o maior

print("Exercício A2 - Maior de Quatro Números")

a2_num1 = float(input("Introduza o primeiro número: "))
a2_num2 = float(input("Introduza o segundo número: "))
a2_num3 = float(input("Introduza o terceiro número: "))
a2_num4 = float(input("Introduza o quarto número: "))

a2_maior = a2_num1
if a2_num2 > a2_maior:
    a2_maior = a2_num2
if a2_num3 > a2_maior:
    a2_maior = a2_num3
if a2_num4 > a2_maior:
    a2_maior = a2_num4

print(f"O maior número é: {a2_maior}")

print("---")

# Exercício A3 - Classificação de IMC (Simplificado)
# Fórmula:
# IMC = peso / (altura × altura)
# Classificação:
# < 18.5 → Baixo peso
# 18.5–24.9 → Normal
# 25–29.9 → Excesso de peso
# >= 30 → Obesidade

print("Exercício A3 - Classificação de IMC (Simplificado)")

a3_peso = float(input("Peso (kg): "))
a3_altura = float(input("Altura (m): "))
a3_imc = a3_peso / (a3_altura * a3_altura)

if a3_imc < 18.5:
    print("Baixo peso")
elif a3_imc < 25:
    print("Normal")
elif a3_imc < 30:
    print("Excesso de peso")
else:
    print("Obesidade")

print("---")

# Exercício A4 - Sistema de Desconto
# Criar programa que:
# Peça valor da compra
# Aplicar desconto:
# >= 100 → 10%
# >= 50 → 5%
# < 50 → sem desconto
# Mostrar valor final.

print("Exercício A4 - Sistema de Desconto")

a4_compra = float(input("Valor da compra: "))
if a4_compra >= 100:
    a4_desconto = a4_compra * 0.1
elif a4_compra >= 50:
    a4_desconto = a4_compra * 0.05
else:
    a4_desconto = 0

a4_compra_final = a4_compra - a4_desconto
print(f"Valor final da compra: {a4_compra_final}")

print("---")

# Exercício A5 - Verificação de Ano Bissexto (Simplificado)
# Criar programa que:
# Peça um ano
# Verifique se é divisível por 4

# Se for → Ano bissexto
# Senão → Ano normal

print("Exercício A5 - Verificação de Ano Bissexto (Simplificado)")

a5_ano = int(input("Introduza um ano: "))
if a5_ano % 4 == 0:
    print("Ano bissexto.")
else:
    print("Ano normal.")

print("---")