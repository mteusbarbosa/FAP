# Comandos Condicionais

1. Expressões Relacionais
2. Expressões Lógicas
3. Comandos Condicionais

## Expressões Relacionais

Utilizam de valores **booleanos** para realizar uma verificação.

| Operadores Relacionais | Significado        | Exemplo                                                                                                 |
| ---------------------- | ------------------ | ------------------------------------------------------------------------------------------------------- |
| ==                     | igualdade          | retorna verdadeiro quando as expressões forem iguais                                                    |
| !=                     | diferente          | retorna verdadeiro quando as expressões forem diferentes                                                |
| >                      | maior que          | retorna verdadeiro quando a expressão da esquerda tiver valor maior que a expressão da direita          |
| <                      | menor que          | retorna verdadeiro quando a expressão da esquerda tiver valor menor que a expressão da direita          |
| >=                     | maior ou igual que | retorna verdadeiro quando a expressão da esquerda tiver valor maior ou igual que a expressão da direita |
| <=                     | menor ou igual que | retorna verdadeiro quando a expressão da esquerda tiver valor menor ou igual que a expressão da direita |

### Exemplos práticos

```python
#a = 20
#b = 21

a == (10 * 2) # a = 20
# True

a != (10 * 2) # a = 20
# False

a > b
# False

a < b
# True

a >= b
# False

a <= b
# True
```

## Expressões Relacionais com String

Ordem de prioridade dos caracteres do alfabeto

ABC...XYZabc...xyz

```python
"a" > "b" # False
"a" == "a" # True
"a" == "A" # False
"B" < "a" # True
"m" < "c" # False

"abacaxi" < "banana" # True
"banana" < "Caqui" # False
"3" == 3 # False
3 > "4" # TypeError: '>' not supported between instances of 'int' and 'str'
```

## Expressões Lógicas

| Operadores Lógicos | Descrição                                                                          |
| ------------------ | ---------------------------------------------------------------------------------- |
| and                | verifica se os dois operandos possuem valor lógico True (verdadeiro)               |
| or                 | verifica se pelo menos um dos dois operandos possui valor lógico True (verdadeiro) |
| not                | Inverte o valor lógico do operando                                                 |

Tabela Verdade **and**

| <expressão1> | <expressão2> | resultado |
| ------------ | ------------ | --------- |
| True         | True         | True      |
| True         | False        | False     |
| False        | True         | False     |
| False        | False        | False     |

Tabela Verdade **or**

| <expressão1> | <expressão2> | resultado |
| ------------ | ------------ | --------- |
| True         | True         | True      |
| True         | False        | True      |
| False        | True         | True      |
| False        | False        | False     |

Tabela Verdade **not**

| <expressão1> | <expressão2> |
| ------------ | ------------ |
| True         | False        |
| False        | True         |

Expressões Equivalentes

- not(a == b) é equivalente a (a != b)
- not(a > b) é equivalente a (a <= b)
- not(a < b) é equivalente a (a >= b)

## Comandos condicionais

Os programas em Python são estruturados através de indentação, ou seja, os blocos são definidos pelo seu espaçamento (tabs) em relação ao início da linha.

### IF

O if é equivalente o "se" na lingua portuguêsa. Se isso faça isso

```py
if a == b:
    print(a + b)
```

- O bloco de comandos é executado somente se a condição (expressão relacional, expressão lógica ou variável booleana) for verdadeira.
- Na estrutura do comando if sempre há um “:” após a condição

```py
#O programa verifica se um número inteiro é impar
a = int(input("Digite um número inteiro: "))

if ((a % 2) == 1):
print("Número ímpar")

print("Fim do programa")
```

### IF/ELSE IF/ELIF/ELSE

```py
# O programa a seguir verifica se um número inteiro é par ou ímpar
a = int(input("Entre com um número inteiro: "))

if (a % 2) == 0:
print("Número par")
else:
print("Número ímpar")

print("Fim do programa")
```

```py
# O programa a seguir determina o maior entre dois números.
a = float(input("Entre com o primeiro número: "))
b = float(input("Entre com o segundo número: "))

if a > b:
print("O maior número é", a)
else:
print("O maior número é", b)
```

O ELIF é usado dentro de uma cadeia de IFs, testando diversas alternativas

```py
ra = input("Entre com o RA de um aluno: ")
if ra == "155446":
print("Gabriel Siqueira")
elif ra == "192804":
print("Alexsandro Alexandrino")
elif ra == "209823":
print("Ana Paula Dantas")
elif ra == "188948":
print("Klairton Brito")
 # ...
elif ra == "999999":
print("...")
else:
print("Aluno não encontrado")

```

## Exercícios

1. Escreva um programa, que dados três números inteiros, imprima o menor deles.

```py
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

if a <= b and a <= c:
    print(a)
elif b <= c:
    print(b)
else:
    print(c)
```

2. Escreva um programa que, dados três números inteiros, imprima os números em ordem crescente.

```py
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

 if (a <= b <= c):
print(a, b, c)
elif (a <= c <= b):
print(a, c, b)
elif (b <= a <= c):
print(b, a, c)
elif (b <= c <= a):
print(b, c, a)
elif (c <= a <= b):
print(c, a, b)
else:
print(c, b, a)
```

Outra forma de resolver a questão 2:

```py
a = int(input("Entre com o primeiro número: "))
b = int(input("Entre com o segundo número: "))
c = int(input("Entre com o terceiro número: "))

x1 = min(a, b, c)
x3 = max(a, b, c)
x2 = a + b + c - x1 - x2

print(x1, x2, x3)
```

3. Escreva um programa que, dadas duas datas, determine qual delas ocorreu cronologicamente primeiro. Para cada uma das duas datas, leia três números referentes ao dia, mês e ano, respectivamente.

```py
dia1 = int(input("Entre com o dia da primeira data: "))
mes1 = int(input("Entre com o mês da primeira data: "))
ano1 = int(input("Entre com o ano da primeira data: "))

dia2 = int(input("Entre com o dia da segunda data: "))
mes2 = int(input("Entre com o mês da segunda data: "))
ano2 = int(input("Entre com o ano da segunda data: "))

if ano1 < ano2:
print(dia1, mes1, ano1, sep="/")
elif ano2 < ano1:
print(dia2, mes2, ano2, sep="/")
elif mes1 < mes2:
print(dia1, mes1, ano1, sep="/")
elif mes2 < mes1:
print(dia2, mes2, ano2, sep="/")
elif dia1 < dia2:
print(dia1, mes1, ano1, sep="/")
else:
print(dia2, mes2, ano2, sep="/")
```

4. Escreva um programa que calcule as raízes de uma equação de segundo grau. O seu programa deve receber três números a, b e c, sendo que a equação é definida como ax2 + bx + c = 0. O seu programa também deve tratar o caso em que a = 0.

```py
a = float(input("Entre com o coeficiente a: "))
b = float(input("Entre com o coeficiente b: "))
c = float(input("Entre com o coeficiente c: "))


if a == 0: # equação do primeiro grau
    if b == 0:
        print("Não existe raiz.")
    else:
        raiz = (-c / b)
        print("A raiz é:", raiz)
else: # equação do segundo grau
    delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("Não existem raízes reais.")
elif delta > 0:
    raiz1 = (-b + delta ** (1 / 2)) / (2 * a)
    raiz2 = (-b - delta ** (1 / 2)) / (2 * a)
    print("As raízes são:", raiz1, "e", raiz2)
else:
    raiz = -b / (2 * a)
    print("A raiz é:", raiz)
```

5. Escreva um programa que simula o jogo conhecido como “Pedra, Papel e Tesoura” de um jogador A contra um jogador B. O programa deve ler a escolha do jogador A e a escolha do jogador B. Por fim, o programa deve indicar quem foi o vencedor.

```py
jogadorA = input("Entre com a primeira escolha: ")
jogadorB = input("Entre com a segunda escolha: ")

if jogadorA == "pedra":
    if jogadorB == "pedra":
        print("Empate")
    elif jogadorB == "tesoura":
        print("O jogador A ganhou")
    else:
        print("O jogador B ganhou")
elif jogadorA == "tesoura":
    if jogadorB == "pedra":
        print("O jogador B ganhou")
    elif jogadorB == "tesoura":
        print("Empate")
    else:
        print("O jogador A ganhou")
else: # jogadorA == "papel"
    if jogadorB == "pedra":
        print("O jogador A ganhou")
    elif jogadorB == "tesoura":
        print("O jogador B ganhou")
    else:
        print("Empate")
```
