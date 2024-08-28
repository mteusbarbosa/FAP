# Exercícios de Banco de Dados

>Com base no sistema de gestão de contas bancárias que discutimos, vejam as 10 questões de SQL, focando na aplicação prática em um cenário real.
>
>As questões abordam desde consultas simples até manipulação de dados, desafiando você a aplicar seus conhecimentos.

## Clientes

| Coluna          | Tipo de Dado | Descrição                      |
| --------------- | ------------ | ------------------------------ |
| id              | INT          | Identificador único do cliente |
| nome            | VARCHAR(255) | Nome completo do cliente       |
| cpf             | VARCHAR(11)  | CPF do cliente                 |
| data_nascimento | DATE         | Data de nascimento do cliente  |

## contas

| Coluna         | Tipo de Dado  | Descrição                      |
| -------------- | ------------- | ------------------------------ |
| id             | INT           | Identificador único da conta   |
| cliente_id     | INT           | ID do cliente titular da conta |
| saldo          | DECIMAL(10,2) | Saldo atual da conta           |
| limite_credito | DECIMAL(10,2) | Limite de crédito da conta     |

### 51. Escreva uma consulta SQL para selecionar o nome e o CPF de todos os clientes

   ```sql
   SELECT nome, cpf
   FROM clientes;
   ```

### 52.  Escreva uma consulta SQL para selecionar o ID da conta e o saldo de todas as contas com saldo inferior a R$ 100,00

   ```sql
   SELECT id, saldo
   FROM contas
   WHERE saldo < 100.00;
   ```

### 53.  Escreva uma consulta SQL para selecionar o nome do cliente e o saldo da conta, ordenados pelo saldo em ordem decrescente

   ```sql
   SELECT c.nome, co.saldo
   FROM clientes c
   JOIN contas co ON c.id = co.cliente_id
   ORDER BY co.saldo DESC;
   ```

### 54.  Escreva uma consulta SQL para atualizar o saldo da conta com ID 123 para R$ 500,00

   ```sql
   UPDATE contas
   SET saldo = 500.00
   WHERE id = 123;
   ```

### 55.  Escreva uma consulta SQL para excluir o cliente com ID 456. Certifique-se de que a exclusão seja feita em cascata para a tabela contas, ou seja, a conta do cliente também deve ser excluída

 ```sql
   -- Primeiro, definir a tabela de contas para excluir em cascata
   ALTER TABLE contas
   ADD CONSTRAINT fk_cliente
   FOREIGN KEY (cliente_id)
   REFERENCES clientes(id)
   ON DELETE CASCADE;

   -- Depois, excluir o cliente
   DELETE FROM clientes
   WHERE id = 456;
   ```

### 56.  Escreva uma consulta SQL para inserir um novo cliente na tabela clientes com os seguintes dados: nome "Maria Silva", CPF "98765432109" e data de nascimento "1990-01-15"

   ```sql
   INSERT INTO clientes (nome, cpf, data_nascimento)
   VALUES ('Maria Silva', '98765432109', '1990-01-15');
   ```

### 57.  Escreva uma consulta SQL para selecionar o nome dos clientes que possuem mais de uma conta

```sql
   SELECT c.nome
   FROM clientes c
   JOIN contas co ON c.id = co.cliente_id
   GROUP BY c.id, c.nome
   HAVING COUNT(co.id) > 1;
   ```

### 58.   Escreva uma consulta SQL para calcular o saldo médio de todas as contas

   ```sql
   SELECT AVG(saldo) AS saldo_medio
   FROM contas;
   ```

### 59.  Escreva uma consulta SQL para selecionar o nome do cliente e o saldo da conta, mas apenas para clientes maiores de 18 anos. Utilize a data atual para calcular a idade

   ```sql
   SELECT c.nome, co.saldo
   FROM clientes c
   JOIN contas co ON c.id = co.cliente_id
   WHERE TIMESTAMPDIFF(YEAR, c.data_nascimento, CURDATE()) > 18;
   ```

### 60.  Escreva uma consulta SQL para criar uma nova tabela chamada transacoes com as colunas: id (INT, chave primária), conta_id (INT), data_transacao (DATETIME), valor (DECIMAL(10,2)) e tipo (VARCHAR(50))

   ```sql
   CREATE TABLE transacoes (
       id INT PRIMARY KEY AUTO_INCREMENT,
       conta_id INT,
       data_transacao DATETIME,
       valor DECIMAL(10,2),
       tipo VARCHAR(50),
       FOREIGN KEY (conta_id) REFERENCES contas(id)
   );
   ```
