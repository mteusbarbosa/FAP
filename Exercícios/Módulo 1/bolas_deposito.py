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

# Difinição da mensagem de erro padrão
mensagem_erro = "Entrada inválida. Por favor, insira números válidos."

# Função para receber os valores do armazém
def receber_valores_armazem(): 
    # Permanece no loop até que o usuário insira um valor válido
    while True:
        # Tenta receber o valor do comprimento, largura e altura do armazém
        try:
            comprimento = float(input("Digite o comprimento do armazém em centímetros: "))
            largura = float(input("Digite a largura do armazém em centímetros: "))
            altura = float(input("Digite a altura do armazém em centímetros: "))
            # Se o usuário inseriu um valor válido, sai do loop
            if comprimento > 0 and largura > 0 and altura > 0:
                return comprimento, largura, altura
            else:
                print("As dimensões devem ser maiores que zero. Tente novamente.")
        # Se o usuário inseriu um valor inválido, exibe a mensagem de erro
        except ValueError:
            print(mensagem_erro)

# Função para receber o diâmetro da bola 
def valor_diametro(bolaescolhida):
    if bolaescolhida == 7:
        while True:
            try:
                diametro_bola = float(input("Qual o diâmetro da bola em centímetros? "))

                if diametro_bola > 0 and diametro_bola < 100:
                    return diametro_bola
                else:
                    print("Valor não suportado. Tente novamente.")
            except ValueError:
                print(mensagem_erro)

    # Retorno das bolas pré-definidas
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

# Função para selecionar a bola
def diametro_bola():
    while True:
        try:
            escolha = int(input("1 - Bola de Basquete Adulto\n2 - Bola de Basquete Infantil\n3 - Bola de Futebol Oficial\n4 - Bola de Vôlei\n5 - Bola de Handball\n6 - Bola de Futebol de Salão\n7 - Outro valor\nSelecione uma das bolas listadas: "))    
            if escolha > 0 and escolha < 8 :
                diametro = valor_diametro(escolha)
                return diametro
            else:
                print("As dimensões devem ser maiores que zero. Tente novamente.")
        except ValueError:
            print(mensagem_erro)


# Função para calcular o volume do armazém
def calcular_volumes(altura, comprimento, largura, diametro):
    raio = diametro/2
    volume_armazem = altura * comprimento * largura
    volume_bola = (4/3) * math.pi * raio**3
    return volume_armazem, volume_bola

# Função para calcular o número de bolas que cabem no armazém
def calcular_numero_bolas(volume_armazem, volume_bola):
    return volume_armazem // volume_bola

# Main
comprimento, largura, altura = receber_valores_armazem()
diametro = diametro_bola()
volumeArmazem, volumeBola = calcular_volumes(altura, comprimento, largura, diametro)
numero_bolas = calcular_numero_bolas(volumeArmazem, volumeBola)

# Prints finais / debug

#print("Comprimento: %.2f cm\nLargura: %.2f cm\nAltura: %.2f cm" % (comprimento, largura, altura))
# print("Diametro da bola: ", diametro)
#print("Volume armazem: %.2f cm³\nVolume bola: %.02f cm³" % (volumeArmazem, volumeBola))
print("\nQuantidade de bolas que cabem no armazém: %.0f bolas" % (numero_bolas))
