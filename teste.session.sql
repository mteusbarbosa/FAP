-- @block 
CREATE TABLE Users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE, 
    bio TEXT,
    country VARCHAR(2)
);

-- @block
DROP TABLE Users

-- @block 
-- Comando para mostrar as tabelas existentes
SHOW TABLES;

-- @block
CREATE TABLE contas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    numero_conta VARCHAR(50) UNIQUE,
    data_criacao DATE,
    tipo_conta VARCHAR(50),
    saldo DECIMAL(10, 2) DEFAULT 0.0
);

-- @block
CREATE TABLE transacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    conta_id INT,
    tipo VARCHAR(50),
    valor DECIMAL(10, 2),
    FOREIGN KEY (conta_id) REFERENCES contas(id)
);


-- @block
SELECT * FROM transacoes
