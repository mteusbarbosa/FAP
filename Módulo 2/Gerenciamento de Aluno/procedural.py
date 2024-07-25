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

def trilha():
  terminal_size = os.get_terminal_size()
  print("-" * terminal_size.columns)

# Função para cadastrar as notas de um aluno
def cadastrar_nota(nome_nota):
  while True:
    # Testa o input de usuário e apenas valida caso seja um número
    try:
      nota = float(input(f"Nota do {nome_nota}: "))

      # Validação da nota
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

  novo_aluno["nota1"] = cadastrar_nota("1º Trimestre")
  novo_aluno["nota2"] = cadastrar_nota("2º Trimestre")
  novo_aluno["nota3"] = cadastrar_nota("3º Trimestre")
  alunos[nova_matricula] = novo_aluno


# Função para carregar os dados dos alunos do arquivo JSON
def carregar_dados_arquivo():
  global alunos
  with open("dados_alunos.json", "r") as arquivo_json:
    alunos = json.load(arquivo_json)

# Função para salvar os dados dos alunos no arquivo JSON
def salvar_alunos_arquivo():
  with open("dados_alunos.json", "w") as arquivo_json:
    json.dump(alunos, arquivo_json)

while True:
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
      #listar_alunos_cadastrados()
      continue
  
    if opcao == 3:
      #editar_aluno_existente()
      continue
  
    if opcao == 4:
      #excluir_aluno()
      continue
  
    if opcao == 5:
      #exibir_media_alunos()
      continue
  
    if opcao == 6:
      #carregar_dados_arquivo()
      continue

    if opcao == 7:
      #salvar_alunos_arquivo()
      continue

    if opcao == 0:
      print("-\nSaindo do programa\n-")
      break

  except ValueError:
    print("-\nOpção inválida. Tente novamente.\n-")
