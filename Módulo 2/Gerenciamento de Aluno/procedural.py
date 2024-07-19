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
import json

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
      #cadastrar_novo_aluno()
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
