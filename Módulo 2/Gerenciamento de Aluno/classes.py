'''
## Exercício 2: Implementação Orientada a Objetos
Agora, refatore o programa criado no Exercício 1 para usar uma abordagem orientada a objetos.
Seu programa deve incluir:
1. Uma classe ``Aluno`` com atributos apropriados e métodos para:
    - Adicionar notas
    - Calcular a média
    - Representar o aluno como string
2. Uma classe ``GerenciadorAlunos`` que gerencia uma coleção de objetos Aluno e implementa
métodos para:
    - Cadastrar um novo aluno
    - Listar todos os alunos
    - Buscar um aluno por matrícula
    - Editar informações de um aluno
    - Excluir um aluno
3. Um menu interativo similar ao do Exercício 1, mas utilizando os métodos da classe
GerenciadorAlunos.

Requisitos adicionais para o Exercício 2:
- Use encapsulamento adequado (atributos privados quando apropriado).
- Implemente validação de dados (por exemplo, notas entre 0 e 10).
- Use herança e polimorfismo se encontrar uma oportunidade adequada.

Para ambos os exercícios:
- Comente seu código explicando as partes importantes.
- Trate possíveis erros (como entrada inválida do usuário).
- Use boas práticas de programação Python (PEP 8).

Bônus: Implemente a funcionalidade de salvar e carregar os dados dos alunos 
em um arquivo, tanto na versão procedural quanto na orientada a objetos.
'''

import json
import os

from tabulate import tabulate


class Aluno:
    def __init__(self, matricula, nome, curso, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def obter_nota(self, nome_nota, nota_atual=None):
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

    def media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3


class GerenciadorAlunos:

    def __init__(self):
        self.alunos = {}

    def mensagem_erro(self):
        print("Valor inválido. Matrículas devem ser apenas números")

    def trilha(self):
        terminal_size = os.get_terminal_size()
        print("-" * terminal_size.columns)

    def cadastrar_novo_aluno(self):
        self.trilha()
        nome = input("Nome do aluno: ")
        curso = input("Curso: ")

        while True:
            try:
                nova_matricula = int(input("Matrícula: "))
            except ValueError:
                self.mensagem_erro()
                continue

            if nova_matricula in self.alunos:
                print("Matrícula já está cadastrada!")
            else:
                break

        aluno = Aluno(nova_matricula, nome, curso, 0, 0, 0)
        aluno.nota1 = aluno.obter_nota("1º Trimestre")
        aluno.nota2 = aluno.obter_nota("2º Trimestre")
        aluno.nota3 = aluno.obter_nota("3º Trimestre")

        self.alunos[nova_matricula] = aluno
        

    def listar_alunos_cadastrados(self):
        if not self.alunos:
            self.trilha()
            print("Não há alunos cadastrados.")
            return

        data = [[aluno.nome, aluno.curso, aluno.matricula]
                for aluno in self.alunos.values()]
        self.trilha()
        print(
            tabulate(data,
                     headers=['Nome', 'Curso', 'Matrícula'],
                     tablefmt='simple_grid'))

    def editar_aluno_existente(self):
        self.trilha()
        while True:
            try:
                matricula = int(input("Matrícula do aluno a ser editado: "))
            except ValueError:
                self.mensagem_erro()
                continue

            if matricula in self.alunos:
                aluno = self.alunos[matricula]
                print(f"Editando informações do aluno: {aluno.nome}")

                novo_nome = input(f"Nome atual ({aluno.nome}): ")
                if novo_nome:
                    aluno.nome = novo_nome

                novo_curso = input(f"Curso atual ({aluno.curso}): ")
                if novo_curso:
                    aluno.curso = novo_curso

                aluno.nota1 = aluno.obter_nota("1º Trimestre", aluno.nota1)
                aluno.nota2 = aluno.obter_nota("2º Trimestre", aluno.nota2)
                aluno.nota3 = aluno.obter_nota("3º Trimestre", aluno.nota3)

                self.alunos[matricula] = aluno
                print(f"Informações do aluno {aluno.nome} atualizadas com sucesso!")
                break
            else:
                print("Matrícula não encontrada.")

    def excluir_aluno(self):
        self.trilha()
        while True:
            try:
                matricula = int(input("Matrícula do aluno a ser excluído: "))
                if matricula in self.alunos:
                    nome_aluno = self.alunos[matricula].nome
                    del self.alunos[matricula]
                    print(f"Aluno {nome_aluno} excluído com sucesso!")
                    break
                else:
                    print("Matrícula não encontrada.")
                    break
            except ValueError:
                self.mensagem_erro()
                continue

    def exibir_media_alunos(self):
        if not self.alunos:
            self.trilha()
            print("Não há alunos cadastrados.")
            return

        data = [[
            aluno.nome, aluno.curso, aluno.matricula, aluno.nota1, aluno.nota2,
            aluno.nota3, "{:.1f}".format(aluno.media())
        ] for aluno in self.alunos.values()]
        self.trilha()
        print(
            tabulate(data,
                     headers=[
                         'Nome', 'Curso', 'Matrícula', 'Nota 1', 'Nota 2',
                         'Nota 3', 'Média'
                     ],
                     tablefmt='simple_grid'))

    # Método para carregr dados do arquivo JSON
    def carregar_dados_arquivo(self):
        with open("dados_alunos.json", "r") as arquivo_json:
            alunos_dicionario = json.load(arquivo_json)
            
        # Para cada chave do json (matricula) e seus dados dentro, 
        # cria um Aluno (classe) passando todos os dados (desempacotamento)
        for matricula, dados in alunos_dicionario.items():
            self.alunos[int(matricula)] = Aluno(**dados)
        self.trilha()
        print("Dados carregados com sucesso.")

    # Método para salvar os alunos no arquivo JSON
    def salvar_alunos_arquivo(self):
        with open("dados_alunos.json", "w") as arquivo_json:
            alunos_dicionario = {
                matricula: aluno.__dict__
                for matricula, aluno in self.alunos.items()
            }
            json.dump(alunos_dicionario, arquivo_json)
        self.trilha()
        print("Dados dos alunos salvos com sucesso.")

# Função principal do programa
def main():
    gerenciador = GerenciadorAlunos()

    while True:
        gerenciador.trilha()
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

            # Tratamento de erros
            if opcao < 0 or opcao > 7:
                print("-\nOpção inválida. Tente novamente.\n-")
                continue

            if opcao == 1:
                gerenciador.cadastrar_novo_aluno()
                continue

            if opcao == 2:
                gerenciador.listar_alunos_cadastrados()
                continue

            if opcao == 3:
                gerenciador.editar_aluno_existente()
                continue

            if opcao == 4:
                gerenciador.excluir_aluno()
                continue

            if opcao == 5:
                gerenciador.exibir_media_alunos()
                continue

            if opcao == 6:
                gerenciador.carregar_dados_arquivo()
                continue

            if opcao == 7:
                gerenciador.salvar_alunos_arquivo()
                continue

            if opcao == 0:
                print("-\nSaindo do programa\n-")
                break

        except ValueError:
            print("-\nOpção inválida. Tente novamente.\n-")


if __name__ == "__main__":
    main()