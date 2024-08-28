from decimal import Decimal
import mysql.connector

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root", # Usuário do Banco de Dados
        password="", # Senha do Banco de Dados
        database="" # Nome do Banco
    )
    
""" Criar as tabelas no banco 

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
); """



class Conta:
    def __init__(self, nome, numero_conta, data_criacao_conta, tipo_conta):
        self.nome = nome
        self.numero_conta = numero_conta
        self.data_criacao_conta = data_criacao_conta
        self.tipo_conta = tipo_conta
        self.saldo = 0
        self.transacoes = []

    def salvar_no_banco(self):
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contas (nome, numero_conta, data_criacao, tipo_conta, saldo) "
            "VALUES (%s, %s, %s, %s, %s)",
            (self.nome, self.numero_conta, self.data_criacao_conta, self.tipo_conta, self.saldo)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def deposito(self, valor):
        valor_decimal = Decimal(valor)  # Converte o valor para Decimal
        self.saldo += valor_decimal
        self.registrar_transacao("Depósito", valor_decimal)
        self.atualizar_saldo()

    def saque(self, valor):
        valor_decimal = Decimal(valor)  # Converte o valor para Decimal
        if self.saldo >= valor_decimal:
            self.saldo -= valor_decimal
            self.registrar_transacao("Saque", valor_decimal)
            self.atualizar_saldo()
            return True
        else:
            return False

    def registrar_transacao(self, tipo, valor):
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO transacoes (conta_id, tipo, valor) "
            "VALUES ((SELECT id FROM contas WHERE numero_conta = %s), %s, %s)",
            (self.numero_conta, tipo, valor)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def atualizar_saldo(self):
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE contas SET saldo = %s WHERE numero_conta = %s",
            (self.saldo, self.numero_conta)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def exibir_transacoes(self):
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT tipo, valor FROM transacoes WHERE conta_id = "
            "(SELECT id FROM contas WHERE numero_conta = %s)",
            (self.numero_conta,)
        )
        transacoes = cursor.fetchall()
        cursor.close()
        conn.close()
        
        for tipo, valor in transacoes:
            print(f"- {tipo}: R$ {valor:.2f}")

class GerenciadorConta:
    def cadastrar_conta(self, nome, numero_conta, data_criacao_conta, tipo_conta):
        # Verifica se a conta já existe
        if self.buscar_conta(numero_conta):
            print("Conta já cadastrada")
        else:
            # Cria uma nova conta e salva no banco de dados
            conta = Conta(nome, numero_conta, data_criacao_conta, tipo_conta)
            conta.salvar_no_banco()
            print("Conta cadastrada com sucesso!")

    def realizar_deposito(self, numero_conta, valor):
        conta = self.buscar_conta(numero_conta)
        if conta:
            conta.deposito(valor)
            print("Depósito realizado com sucesso!")
        else:
            print("Conta não encontrada.")

    def realizar_saque(self, numero_conta, valor):
        conta = self.buscar_conta(numero_conta)
        if conta:
            if conta.saque(valor):
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente.")
        else:
            print("Conta não encontrada.")

    def buscar_conta(self, numero_conta):
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT nome, numero_conta, data_criacao, tipo_conta, saldo FROM contas WHERE numero_conta = %s",
            (numero_conta,)
        )
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()

        if resultado:
            nome, numero_conta, data_criacao, tipo_conta, saldo = resultado
            conta = Conta(nome, numero_conta, data_criacao, tipo_conta)
            conta.saldo = saldo
            return conta
        else:
            return None

    def visualizar_extrato(self, numero_conta):
        conta = self.buscar_conta(numero_conta)
        if conta:
            print(f"Extrato da conta {numero_conta}:")
            conta.exibir_transacoes()
        else:
            print("Conta não encontrada.")

    def editar_conta(self, numero_conta, novo_nome):
        conta = self.buscar_conta(numero_conta)
        if conta:
            conn = conectar_banco()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE contas SET nome = %s WHERE numero_conta = %s",
                (novo_nome, numero_conta)
            )
            conn.commit()
            cursor.close()
            conn.close()
            print("Nome do titular atualizado com sucesso!")
        else:
            print("Conta não encontrada.")

    def excluir_conta(self, numero_conta):
        conta = self.buscar_conta(numero_conta)
        if conta:
            conn = conectar_banco()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM transacoes WHERE conta_id = (SELECT id FROM contas WHERE numero_conta = %s)",
                (numero_conta,)
            )
            cursor.execute(
                "DELETE FROM contas WHERE numero_conta = %s",
                (numero_conta,)
            )
            conn.commit()
            cursor.close()
            conn.close()
            print("Conta excluída com sucesso!")
        else:
            print("Conta não encontrada.")


def main():
    gerenciador = GerenciadorConta()

    while True:
        print("\nSistema de Gerenciamento de Contas Bancárias")
        print("1. Cadastrar nova conta")
        print("2. Realizar depósito")
        print("3. Realizar saque")
        print("4. Visualizar extrato")
        print("5. Editar nome do titular")
        print("6. Excluir conta")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome do titular da conta: ")
            numero_conta = input("Digite o número da conta: ")
            data_criacao_conta = input("Digite a data de criação da conta (YYYY-MM-DD): ")
            tipo_conta = input("Digite o tipo da conta (corrente/poupança): ")
            gerenciador.cadastrar_conta(nome, numero_conta, data_criacao_conta, tipo_conta)

        elif escolha == "2":
            numero_conta = input("Digite o número da conta para depósito: ")
            valor = float(input("Digite o valor do depósito: "))
            gerenciador.realizar_deposito(numero_conta, valor)

        elif escolha == "3":
            numero_conta = input("Digite o número da conta para saque: ")
            valor = float(input("Digite o valor do saque: "))
            gerenciador.realizar_saque(numero_conta, valor)

        elif escolha == "4":
            numero_conta = input("Digite o número da conta para visualizar o extrato: ")
            gerenciador.visualizar_extrato(numero_conta)

        elif escolha == "5":
            numero_conta = input("Digite o número da conta para edição: ")
            novo_nome = input("Digite o novo nome do titular: ")
            gerenciador.editar_conta(numero_conta, novo_nome)

        elif escolha == "6":
            numero_conta = input("Digite o número da conta para exclusão: ")
            gerenciador.excluir_conta(numero_conta)

        elif escolha == "7":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()