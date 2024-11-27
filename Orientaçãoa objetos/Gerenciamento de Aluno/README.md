# Sistema de Gerenciamento de Alunos

Contexto: Você foi contratado para desenvolver um **sistema simples de gerenciamento de alunos para uma escola**. O sistema deve permitir o **cadastro de alunos, incluindo informações como nome, matrícula, curso e notas**.

Além disso, deve ser possível **listar todos os alunos, editar informações de um aluno específico e excluir um aluno do sistema**.

## Requisitos dos sistemas

### Exercício 1: Implementação Procedural

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

### Exercício 2: Implementação Orientada a Objetos

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

### Para ambos os exercícios

- Comente seu código explicando as partes importantes.
- Trate possíveis erros (como entrada inválida do usuário).
- Use boas práticas de programação Python (PEP 8).

Após completar ambos os exercícios, escreva um breve parágrafo comparando as duas abordagens, destacando as vantagens e desvantagens de cada uma.

Bônus: Implemente a funcionalidade de salvar e carregar os dados dos alunos em um arquivo, tanto na versão procedural quanto na orientada a objetos.

## Apresentação do Sistema

### Visão geral

O código apresentado implementa um sistema simples de gerenciamento de alunos em Python, utilizando uma abordagem procedural. A estrutura do código é organizada por funções, com cada função responsável por uma determinada tarefa. A persistência dos dados é feita através de um arquivo JSON.

### Componentes principais e suas funcionalidades

1.**Variaveis globais**

alunos: Um dicionário que armazena os dados principais de cada aluno,
contendo as chaves ‘nome’, ‘matricula’, ‘curso’ e as notas.

2. **Funções**

obter_nota: Cadastrar ou editar a nota dos alunos.
cadastrar_novo_aluno: Adicionar novo aluno.
listar_alunos_cadastrados: Apresenta os dados de todos os alunos
cadastrados no sistema.
editar_aluno_existente: Permite a alteração dos dados de um
determinado aluno.
excluir_aluno: Remove um aluno específico da lista.
exibir_media_alunos: Apresenta a média de cada aluno em uma tabela.
carregar_dados_arquivo: Carregar dados dos alunos a partir de um
arquivo JSON.
salvar_dados_arquivo: Salvar dados dos alunos em um arquivo JSON.

3. **JSON**

Utilizado para armazenar as informações dos alunos em um formato
JSON. Garantindo a persistência dos dados entre as execuções do
programa.

4. **Menu interativo**

Facilitando a utilização do usuário para escolher uma determinada
operação.

### Análise da Arquitetura do Código

- **Modularidade**: O código é dividido por funções, a fim de facilitar a legibilidade e manutenção do sistema.
- **Tratamento de erros**: O código inclui verificação de entradas, para evitar a entrada de dados inválidos informados pelo usuário.
- **Arquivo JSON**: Onde sua utilização permite que o usuário salve a entrada de dados em um arquivo JSON, garantindo a persistência dos dados nas próximas execuções do programa.
- **Utilização da Biblioteca tabulate**: A biblioteca tabulate é utilizada para formatar a saída dos dados em tabelas, melhorando a visualização.

### Funcionamento detalhado

1. **Inicialização**: Ao iniciar o programa, o dicionário alunos é inicializado como vazio.
2. **Menu Interativo**: O programa apresenta um menu com as opções disponíveis para o usuário.
3. **Escolha da Opção**: O usuário seleciona a opção desejada.
4. Execução da Função: A função correspondente à opção escolhida é
executada.
5. **Persistência de Dados**: Os dados dos alunos são salvos em um arquivo JSON, permitindo que sejam carregados novamente em futuras execuções do programa.
