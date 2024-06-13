""" 
Desenvolva uma função em Python que calcule o imposto de renda a ser pago com base no salário de uma pessoa. 

Utilize a tabela de faixas de imposto de renda vigente no Brasil. 

A função deve considerar a alíquota e a parcela a deduzir conforme descrito na tabela a 
seguir:

Base de Cálculo (R$)            Alíquota (%)            Parcela a Deduzir do IR (R$)
Até 2259.20                     0                       0
De 2259.21 até 2826.65          7.5                     169.44
De 2826.66 até 3751.05          15                      381.44
De 3751.06 até 4664.68          22.5                    662.77
Acima de 4664.68                27.5                    896.00

Exemplo de cálculo:

Uma pessoa que ganha R$ 3.000,00 se enquadra na terceira faixa da tabela, com uma alíquota de 15% e uma dedução de R$ 381,44. 
O cálculo do imposto seria: 
Imposto = (3000*0,15) - 381,44

Passos do Exercício:
1. Crie uma função calcular_imposto(salario) que recebe o salário como argumento e retorna o valor do imposto de renda a ser pago.
2. A função deve verificar em qual faixa o salário se enquadra e aplicar a alíquota e dedução correspondentes.
3. Utilize quatro casos hipotéticos para testar a função.
4. Explique graficamente como a tabela funciona.

Obs.: Isso é uma simplificação, pois na realidade, a incidência de alíquotas maiores ocorre nas 
partes 'excedentes' das faixas 'anteriores'. 

Obs.2: Tentem fazer o 'máximo' que puderem. Sei que é um desafio para quem está iniciando, mas é para testarmos e buscarmos discutir, em exemplos 'mais próximos do real', partes da lógica, de comandos, etc 
"""

def calcular_aliquota(salario):
    if salario >= 4664.68:
        return 27.5/100
    if 3751.06 <= salario <= 4664.68:
        return 22.5/100
    if 2826.66 <= salario <= 3751.05:
        return 15/100
    if 2259.21 <= salario <= 3751.05:
        return 7.5/100
    return 0

def calcular_deducao(salario):
    if salario >= 4664.68:
        return 896.00
    if 3751.06 <= salario <= 4664.68:
        return 662.77
    if 2826.66 <= salario <= 3751.05:
        return 381.44
    if 2259.21 <= salario <= 3751.05:
        return 169.44
    return 0

def calcular_imposto(salario):
    aliquota = calcular_aliquota(salario)
    print(aliquota)
    deducao = calcular_deducao(salario)
    return (salario * aliquota ) - deducao

print("Informe o seu salário")
salario = float(input("R$ "))

while salario < 0:
    print("Salário inválido, informe um novo valor")
    salario = float(input("R$ "))

salarioLiquido = calcular_imposto(salario)

print("Salário bruto: %.2f\nValor do imposto: %.2f\nSalário líquido: %.2f" % (salario, salarioLiquido, (salario - salarioLiquido)))
