'''
Crie um programa em Python que implemente o sistema de gerenciamento de alunos usando 
uma abordagem procedural (sem orientação a objetos). O programa deve incluir as 
seguintes funcionalidades:
1. Cadastrar um novo aluno (nome, matrícula, curso, notas)
2. Listar todos os alunos cadastrados (exibindo nome, matrícula, curso, notas e média)
3. Editar informações de um aluno existente (busca por matrícula)
4. Excluir um aluno do sistema (busca por matrícula)
5. Calcular e exibir a média das notas de cada aluno

Requisitos:

- Use uma lista de dicionários para armazenar os dados dos alunos.
- Implemente um menu interativo para o usuário escolher as operações.
- Use funções para organizar o código.
- Calcule a média das notas sempre que necessário.

Para ambos os exercícios:
- Comente seu código explicando as partes importantes.
- Trate possíveis erros (como entrada inválida do usuário).
- Use boas práticas de programação Python (PEP 8).

Bônus: Implemente a funcionalidade de salvar e carregar os dados dos alunos 
em um arquivo, tanto na versão procedural quanto na orientada a objetos.
'''
#Importação da biblioteca json
import os
import json
from tabulate import tabulate

alunos = {}

#Função para exibir separadores
def trilha():
  terminal_size = os.get_terminal_size()
  print("-" * terminal_size.columns)

# Função para cadastrar ou editar nota dos alunos
def obter_nota(nome_nota, nota_atual=None):
    while True:
        try:
            if nota_atual is not None:
                entrada = input(f"Nota do {nome_nota} atual ({nota_atual}): ")
                if entrada:
                    nota = float(entrada)
                else:
                    return nota_atual
            else:
                nota = float(input(f"Nota do {nome_nota}: "))

            if nota < 0 or nota > 10:
                print("A nota deve estar entre 0 e 10.")
                continue

            return nota
        except ValueError:
            print("Valor inválido. A nota deve ser um número real.")
            continue


# Função para cadastrar um novo aluno
def cadastrar_novo_aluno():
  # Cria um dicionário vazio para o novo aluno
  novo_aluno = {}
  trilha()
  novo_aluno["nome"] = input("Nome do aluno: ")
  novo_aluno["curso"] = input("Curso: ")

  # Testa o input de usuário e apenas valida caso seja um número
  while True:
    try:
      # Convertendo para inteiro
      nova_matricula = int(input("Matrícula: "))
    except ValueError:
      print("Valor inválido. Matrículas devem ser apenas números")
      continue

    if nova_matricula in alunos:
      print("Matrícula já está cadastrada!")
    else:
      novo_aluno["matricula"] = nova_matricula
      break

  novo_aluno["nota1"] = obter_nota("1º Trimestre")
  novo_aluno["nota2"] = obter_nota("2º Trimestre")
  novo_aluno["nota3"] = obter_nota("3º Trimestre")
  alunos[nova_matricula] = novo_aluno

# Função para Listar alunos
def listar_alunos_cadastrados():
  # Verifica se há alunos cadastrados
  if not alunos:
    trilha()
    print("Não há alunos cadastrados.")
    return

  # Cria uma lista de listas com os dados dos alunos
  data = [[
      aluno['nome'],
      aluno['curso'],
      matricula,
  ] for matricula, aluno in alunos.items()]
   # Imprime a tabela
  trilha()
  print(
      tabulate(data,
               headers=['Nome', 'Curso', 'Matrícula'],
               tablefmt='simple_grid'))
  
def editar_aluno_existente():
  trilha()
  while True:
    try:
      # Convertendo para inteiro
      matricula = int(input("Matrícula do aluno a ser editado: "))
    except ValueError:
      print("Valor inválido. Matrículas devem ser apenas números")
      continue

    if matricula in alunos:
      aluno = alunos[matricula]
      print(f"Editando informações do aluno: {aluno['nome']}")

      # Editar nome
      novo_nome = input(f"Nome atual ({aluno['nome']}): ")
      if novo_nome:
        aluno['nome'] = novo_nome

      # Editar curso
      novo_curso = input(f"Curso atual ({aluno['curso']}): ")
      if novo_curso:
        aluno['curso'] = novo_curso

      # Editar notas
      aluno['nota1'] = obter_nota("1º Trimestre", aluno['nota1'])
      aluno['nota2'] = obter_nota("2º Trimestre", aluno['nota2'])
      aluno['nota3'] = obter_nota("3º Trimestre", aluno['nota3'])

      # Atualiza as informações do aluno
      alunos[matricula] = aluno
      print(f"Informações do aluno {aluno['nome']} atualizadas com sucesso!")
      break
    else:
      print("Matrícula não encontrada.")
      
# Excluir aluno
def excluir_aluno():
  trilha()
  while True:
    try:
      # Convertendo para inteiro
      matricula = int(input("Matrícula do aluno a ser excluído: "))

      # Buscando o aluno no dicionário
      if matricula in alunos:
        nome_aluno = alunos[matricula]["nome"]
        del alunos[matricula]
        print(f"Aluno {nome_aluno} excluído com sucesso!")
        break
      else:
        print("Matrícula não encontrada.")
        break
    except ValueError:
      print("Valor inválido. Matrículas devem ser apenas números")
      continue

#Função para exibir média dos alunos
def exibir_media_alunos():
  # Verifica se há alunos cadastrados
  if not alunos:
    trilha()
    print("Não há alunos cadastrados.")
    return

  # Cria uma lista de listas com os dados dos alunos
  data = [[
      aluno['nome'], aluno['curso'], matricula, aluno['nota1'], aluno['nota2'],
      aluno['nota3'], "{:.1f}".format(
          (aluno['nota1'] + aluno['nota2'] + aluno['nota3']) / 3)
  ] for matricula, aluno in alunos.items()]

  # Imprime a tabela
  trilha()
  print(
      tabulate(data,
               headers=[
                   'Nome', 'Curso', 'Matrícula', 'Nota 1', 'Nota 2', 'Nota 3',
                   'Média'
               ],
               tablefmt='simple_grid'))

# Função para carregar os dados dos alunos do arquivo JSON
def carregar_dados_arquivo():
  global alunos
  with open("dados_alunos.json", "r") as arquivo_json:
    alunos = json.load(arquivo_json)
  trilha()
  print("Dados carregados com sucesso.")

# Função para salvar os dados dos alunos no arquivo JSON
def salvar_alunos_arquivo():
  with open("dados_alunos.json", "w") as arquivo_json:
    json.dump(alunos, arquivo_json)
  trilha()
  print("Dados dos alunos salvos com sucesso.")

while True:
  trilha()
  print("[1] Cadastrar um novo aluno")
  print("[2] Listar todos os alunos cadastrados")
  print("[3] Editar informações de um aluno existente")
  print("[4] Excluir um aluno do sistema")
  print("[5] Calcular e exibir a média das notas de cada aluno")
  print("[6] Carregar dados de arquivo")
  print("[7] Salvar dados em arquivo")
  print("[0] Sair")

  try:
    opcao = int(input("Escolha uma opção: "))

    if opcao < 0 or opcao > 7:
      print("-\nOpção inválida. Tente novamente.\n-")
      continue

    if opcao == 1:
      cadastrar_novo_aluno()
      continue
  
    if opcao == 2:
      listar_alunos_cadastrados()
      continue
  
    if opcao == 3:
      editar_aluno_existente()
      continue
  
    if opcao == 4:
      excluir_aluno()
      continue
  
    if opcao == 5:
      exibir_media_alunos()
      continue
  
    if opcao == 6:
      carregar_dados_arquivo()
      continue

    if opcao == 7:
      salvar_alunos_arquivo()
      continue

    if opcao == 0:
      print("-\nSaindo do programa\n-")
      break

  except ValueError:
    print("-\nOpção inválida. Tente novamente.\n-")
