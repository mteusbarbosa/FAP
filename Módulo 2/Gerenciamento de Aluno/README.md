# Sistema de Gerenciamento de Alunos

Contexto: Você foi contratado para desenvolver um **sistema simples de gerenciamento de alunos para uma escola**. O sistema deve permitir o **cadastro de alunos, incluindo informações como nome, matrícula, curso e notas**.

Além disso, deve ser possível **listar todos os alunos, editar informações de um aluno específico e excluir um aluno do sistema**.

## Exercício 1: Implementação Procedural

Crie um programa em Python que implemente o sistema de gerenciamento de alunos usando uma abordagem procedural (sem orientação a objetos). O programa deve incluir as seguintes funcionalidades:
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

## Exercício 2: Implementação Orientada a Objetos
Agora, refatore o programa criado no Exercício 1 para usar uma abordagem orientada a objetos. Seu programa deve incluir:
1. Uma classe ``Aluno`` com atributos apropriados e métodos para:
    - Adicionar notas
    - Calcular a média
    - Representar o aluno como string
2. Uma classe ``GerenciadorAlunos`` que gerencia uma coleção de objetos Aluno e implementa métodos para:
    - Cadastrar um novo aluno
    - Listar todos os alunos
    - Buscar um aluno por matrícula
    - Editar informações de um aluno
    - Excluir um aluno
3. Um menu interativo similar ao do Exercício 1, mas utilizando os métodos da classe ``GerenciadorAlunos``.

Requisitos adicionais para o Exercício 2:
- Use encapsulamento adequado (atributos privados quando apropriado).
- Implemente validação de dados (por exemplo, notas entre 0 e 10).
- Use herança e polimorfismo se encontrar uma oportunidade adequada.

Para ambos os exercícios:
- Comente seu código explicando as partes importantes.
- Trate possíveis erros (como entrada inválida do usuário).
- Use boas práticas de programação Python (PEP 8).

Após completar ambos os exercícios, escreva um breve parágrafo comparando as duas abordagens, destacando as vantagens e desvantagens de cada uma.

Bônus: Implemente a funcionalidade de salvar e carregar os dados dos alunos em um arquivo, tanto na versão procedural quanto na orientada a objetos.

Pessoal: Vocês têm liberdade para alterar e melhorar, modificar alguns detalhes deste exercício. O importante é fazer, mesmo que não chegue aos 100%. 

O exercício fornece um desafio completo que permite aos alunos praticar ambas as abordagens de programação e refletir sobre as diferenças entre elas. 
