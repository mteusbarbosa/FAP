
""" Desenvolva um programa em Python que receba a altura e o peso de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e depois classifique o resultado em faixas ou categorias conforme descrito abaixo. 
    O programa deve incluir validação de dados para a altura e o peso, aceitando apenas valores dentro dos intervalos especificados.
    
Especificações:
1. Validação da altura:
     Deve ser maior que 0.6 metros e menor que 2.5 metros.
     Se o valor inserido estiver fora desse intervalo, o programa deve solicitar a altura novamente até que um valor válido seja fornecido.
2. Validação do peso:
    Deve ser maior que 15 kg e menor que 250 kg.
    Se o valor inserido estiver fora desse intervalo, o programa deve solicitar peso novamente até que um valor válido seja fornecido.
3. Cálculo do IMC:
    Fórmula: IMC = peso / (altura ** 2)
4. Classificação do IMC:
    Abaixo de 18.5: Abaixo do peso
    Entre 18.5 e 24.9: Peso normal
    Entre 25 e 29.9: Sobrepeso
    Entre 30 e 34.9: Obesidade grau I
    Entre 35 e 39.9: Obesidade grau II
    Acima de 40: Obesidade grau III
"""

def calculo_imc(altura: float, peso: float):
    return peso / (altura ** 2)

def classificacao_imc(imc):
    match imc:
        case imc if imc < 18.5:
            return "você está abaixo do peso normal"
        case imc if 18.5 <= imc < 25:
            return "você está com o peso normal"
        case imc if 25 <= imc < 30:
            return "você está com Sobrepeso"
        case imc if  30 <= imc < 35:
            return "você está com obesidade grau I"
        case imc if  35 <= imc < 40:
            return "você está com obesidade grau II"
        case imc if  40 <= imc :
            return "você está com obesidade grau III"
        case _:
            return "IMC inválido"


alturaMetros = float(0)

print("Qual a sua altura em metros?")
alturaMetros = float(input())

while alturaMetros < 0.6 or alturaMetros > 2.5:
    print("A altura que você informou não é válida, insira uma altura entre 0.6 metros e 2.5 metros")
    alturaMetros = float(input())

pesoKg = float(0)

print("Qual o seu peso em kilogramas?")
pesoKg = float(input())

while pesoKg < 15 or pesoKg > 250:
    print("O peso que você informou não é válido, insira um peso entre 15kg e 250kg")
    pesoKg = float(input())

print("Você mede %.2f metros de altura e pesa %.2f kg" % (alturaMetros, pesoKg))

IMC = calculo_imc(alturaMetros, pesoKg)
categoriaImc = classificacao_imc(IMC)

print("Seu IMC é de %.2f e %s." % (IMC, categoriaImc))
# print("Seu IMC é de %.2f e " + categoriaImc + "." % (IMC))
