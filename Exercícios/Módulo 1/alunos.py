""" 
Objetivo: Criar um sistema básico de gerenciamento de alunos em Python, utilizando listas e dicionários para armazenar e manipular os dados dos alunos.

Requisitos:
Menu Interativo: Implemente um menu com as seguintes opções:
    Cadastrar Novo Aluno:
        Permitir que o usuário digite o nome, curso, matrícula e outras informações relevantes do aluno.
        Armazenar os dados do aluno em um dicionário.
        Adicionar o dicionário do aluno a uma lista que contém todos os alunos cadastrados.
    Listar Alunos Cadastrados:
        Exibir os dados de todos os alunos cadastrados em um formato organizado, incluindo nome, curso e matrícula.
    Sair: Encerrar o programa.
Validação de Dados:
    Matrícula: Verifique se a matrícula informada é um número inteiro e se não está duplicada na lista de alunos.
    Nome e Curso: Verifique se o nome e o curso não estão vazios.
    Imprima mensagens de erro claras para o usuário em caso de dados inválidos.
Dicas:
    Utilize uma lista para armazenar os dicionários que representam os alunos.
    Use a função input() para receber dados do usuário.
    Utilize a função int() para converter a matrícula para o tipo inteiro.
    Use a estrutura for para iterar sobre a lista de alunos e exibir seus dados. 
"""

""" 
Desafios (Opcionais):
Implemente funcionalidades adicionais, como:
    - Atualizar Dados: Editar as informações de um aluno existente.
    - Remover Aluno: Excluir um aluno da lista.
    - Pesquisar Aluno: Encontrar alunos por nome, matrícula ou curso.
    - Calcular Média: Calcular a média das notas de um aluno.
    - Salvar e Carregar Dados: Salvar a lista de alunos em um arquivo e carregar os dados de um arquivo.
"""

import json

alunos = []


def trilha():
    print("-------------------------------------------------")

def cadastrar_aluno():
    novo_aluno = {} # Cria um dicionário vazio para o novo aluno
    trilha()
    novo_aluno["nome"] = input("Nome do aluno: ")
    novo_aluno["curso"] = input("Curso: ")
    try:
        novo_aluno["matricula"] = int(input("Matrícula: ")) # Convertendo para inteiro
    except ValueError:
        print("Valor inválido. Matriculas devem ser apenas números")
        return

    alunos.append(novo_aluno)

def listar_alunos():
    print(alunos)
    print(type(alunos))
    if not alunos:
        trilha()
        print("Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos cadastrados:")
        for aluno in alunos:
            trilha()
            print(f"Nome: {aluno['nome']}\nCurso: {aluno['curso']}\nMatrícula: {aluno['matricula']}")
            
def carregar_dados_arquivo():
    global alunos 
    with open("Exercícios\\Módulo 1\\arquivo.txt", "r") as arquivo_json:
        alunos = json.load(arquivo_json)
        
    print(alunos)
    print(type(alunos))

def salvar_alunos_arquivo():
    with open("Exercícios\\Módulo 1\\arquivo.txt", "w") as arquivo_json:
        json.dump(alunos, arquivo_json)

while True:
    trilha()
    print("[1] Cadastrar novo aluno                        |")
    print("[2] Listar alunos cadastrados                   |")
    print("[3] Atualizar dados de um aluno                 |")
    print("[4] Pesquisar por um aluno                      |")
    print("[5] Calcular média                              |")
    print("[6] Carregar dados                              |")
    print("[7] Salvar dados                                |")
    print("[0] Listar alunos cadastrados                   |")
    try: 
        opcao = int(input("Escolha sua opção: "))
        
        if opcao < 0 or opcao > 7:
            trilha()
            print("Opção inválida!")
    except ValueError:
        trilha()
        print("Opção inválida!")
    
    if opcao == 1:
        cadastrar_aluno()
    
    if opcao == 2:
        listar_alunos()
    
    if opcao == 6:
        carregar_dados_arquivo()
       
    if opcao == 7:
        salvar_alunos_arquivo()
       
    try: 
        if opcao == 0:
            trilha()
            print("Saindo do programa...")
            trilha()
            break
    except NameError:
        print("Error!! AAAA")