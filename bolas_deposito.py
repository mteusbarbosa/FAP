"""
Descrição:
Você deve criar um programa em Python que calcula quantas bolas cabem em um depósito tridimensional com dimensões especificadas pelo usuário. 
O programa deve considerar diferentes tipos de bolas, com tamanhos predefinidos, e também permitir que o usuário insira um tamanho personalizado de bola. 
O cálculo deve ser feito utilizando uma estimativa pelo volume. 

Objetivos:
Desenvolver habilidades em manipulação de entradas e saídas em Python.
Praticar o uso de condicionais, loops e funções.
Entender a aplicação de fórmulas geométricas e conceitos de empacotamento de esferas.

Instruções:

Entrada de Dados:
O programa deve solicitar ao usuário as dimensões do depósito: comprimento, largura e altura (em centímetros).
O programa pode já ter uma lista de tipos de bolas com tamanhos predefinidos, por ex.:
Bola de Basquete Adulto (24 cm)
Bola de Basquete Infantil (22 cm)
Bola de Futebol Oficial (22 cm)
Bola de Vôlei (21 cm)
Bola de Handball (19 cm)
Bola de Futebol de Salão (20 cm).
O usuário deve poder selecionar um dos tipos predefinidos ou escolher a opção "Outro tamanho de bola" para inserir um diâmetro personalizado (em centímetros).

Cálculo dos Volumes:
Calcular o volume do depósito.
Calcular o volume da bola - considere que a bola está 'cheia'. Uma simplificação seria considerar a bola como um 'cubo' que tem lados do tamanho do diâmetro da bola. 

Saída de Dados:
Exibir ao usuário o número aproximado de bolas que caberiam no depósito

Requisitos Técnicos:
Utilize funções para modularizar o código, incluindo funções para:
Entrada de dados
Cálculo dos volumes
Estimativa pelo volume
Exibição dos resultados
Comente o código para explicar cada parte do processo.
Garanta que o programa lida com entradas inválidas e fornece mensagens de erro apropriadas.
Dicas:
Utilize a função input() para receber dados do usuário.
Use condicionais (if, elif, else) para controlar o fluxo do programa.
Utilize operadores matemáticos e a biblioteca math para cálculos precisos.
Teste o programa com diferentes entradas para garantir que os resultados estão corretos.
"""

import math

mensagem_erro = "Entrada inválida. Por favor, insira números válidos."

def receber_valores_armazem(): 
    while True:
        try:
            comprimento = float(input("Digite o comprimento do armazém em metros: "))
            largura = float(input("Digite a largura do armazém em metros: "))
            altura = float(input("Digite a altura do armazém em metros: "))
            if comprimento > 0 and largura > 0 and altura > 0:
                return comprimento, largura, altura
            else:
                print("As dimensões devem ser maiores que zero. Tente novamente.")
        except ValueError:
            print(mensagem_erro)
            
def valor_diametro(bolaescolhida):
    if bolaescolhida == 7:
        while True:
            try:
                diametro_bola = float(input("Qual o diâmetro da bola em centímetros?"))

                if diametro_bola > 0 and diametro_bola < 100:
                    return diametro_bola
                else:
                    print("Valor não suportado. Tente novamente.")
            except ValueError:
                print(mensagem_erro)
        
    match bolaescolhida:
        case 1:
            return 24
        case 2:
            return 22
        case 3:
            return 22
        case 4:
            return 21
        case 5:
            return 19
        case 6:
            return 20
            
def diametro_bola():
    while True:
        try:
            escolha = int(input("Selecione uma das bolas listadas:\n1 - Bola de Basquete Adulto (24 cm)\n2 - Bola de Basquete Infantil (22 cm)\n3 - Bola de Futebol Oficial (22 cm)\n4 - Bola de Vôlei (21 cm)\n5 - Bola de Handball (19 cm)\n6 - Bola de Futebol de Salão (20 cm)\n7 - Outro valor\n"))    
            if escolha > 0 and escolha < 8 :
                diametro = valor_diametro(escolha)
                return diametro
            else:
                print("As dimensões devem ser maiores que zero. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")
            
def calcular_volumes(altura, comprimento, largura, diametro):
    raio = diametro/2
    volume_armazem = altura * comprimento * largura
    volume_bola = (4/3) * math.pi * math.pow(raio, 3)
    return volume_armazem, volume_bola

def calcular_numero_bolas(volume_armazem, volume_bola):
    bola_metro_cubico = volume_bola/1000000
    return volume_armazem / bola_metro_cubico
    
        

comprimento, largura, altura = receber_valores_armazem()
diametro = diametro_bola()
volumeArmazem, volumeBola = calcular_volumes(altura, comprimento, largura, diametro)
numero_bolas = calcular_numero_bolas(volumeArmazem, volumeBola)

print("Comprimento: %.2f metros\nLargura: %.2f metros\nAltura: %.2f metros" % (comprimento, largura, altura))
print("Diametro: %.0f", diametro)
print("Volume armazem: %.2f metroc cúbicos\nVolume bola: %.02f centímetros cúbicos" % (volumeArmazem, volumeBola))

print("Quantidade de bolas que cabem no armazém: %.0f" % (numero_bolas))