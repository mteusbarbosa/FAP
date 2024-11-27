# Sistema de Gerenciamento de Contas Bancárias

Este é um sistema simples de gerenciamento de contas bancárias, desenvolvido em Python, que utiliza o MySQL como banco de dados. Ele permite criar contas, realizar depósitos, saques, visualizar extratos, editar informações e excluir contas.

## Requisitos

Antes de executar o código, certifique-se de ter os seguintes requisitos instalados:

- Python 3.7 ou superior
- MySQL Server
- Biblioteca `mysql-connector-python` instalada

Para instalar a biblioteca `mysql-connector-python`, você pode utilizar o pip:

```bash
pip install mysql-connector-python
```

## Configuração do Banco de Dados

1. Acesse o MySQL e crie o banco de dados e as tabelas necessárias executando os comandos SQL abaixo:

    ```sql
    CREATE DATABASE banco_fap;

    USE banco_fap;

    CREATE TABLE contas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        numero_conta VARCHAR(50) UNIQUE,
        data_criacao DATE,
        tipo_conta VARCHAR(50),
        saldo DECIMAL(10, 2) DEFAULT 0.0
    );

    CREATE TABLE transacoes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        conta_id INT,
        tipo VARCHAR(50),
        valor DECIMAL(10, 2),
        FOREIGN KEY (conta_id) REFERENCES contas(id)
    );
    ```

2. Edite o código no arquivo main.py para adicionar as informações corretas de conexão com o banco de dados:

```py
def conectar_banco():
    return mysql.connector.connect(
        host="",
        user="", # Usuário do Banco de Dados
        password="", # Senha do Banco de Dados
        database="banco_fap" # Nome do Banco
    )
```

> Certifique-se de substituir o user, password, e host conforme a configuração do seu ambiente MySQL.

### Como executar

1. Clone o repositório ou copie os arquivos para um diretório local.
2. Certifique-se de que o MySQL Server está em execução.
3. Navegue até o diretório onde o arquivo main.py está localizado.
4. Execute o código com o seguinte comando:

    ```bash
    python main.py
    ```

5. Siga as instruções no terminal para interagir com o sistema.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

- Cadastrar nova conta: Cria uma nova conta bancária.
- Realizar depósito: Adiciona um valor à conta existente.
- Realizar saque: Retira um valor da conta, se o saldo for suficiente.
- Visualizar extrato: Mostra todas as transações realizadas em uma conta específica.
- Editar nome do titular: Permite a edição do nome do titular da conta.
- Excluir conta: Exclui uma conta e todas as suas transações associadas.
- Sair: Encerra o sistema.

