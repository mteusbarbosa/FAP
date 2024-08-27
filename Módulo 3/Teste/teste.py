class Conta:
    def __init__(self, nome, numero_conta, data_criacao_conta, tipo_conta):
        self.nome = nome
        self.numero_conta = numero_conta
        self.data_criacao_conta = data_criacao_conta
        self.tipo_conta = tipo_conta
        self.saldo = 0
        self.transacoes = []

    def deposito(self, valor):
        self.saldo += valor
        self.transacoes.append(("Depósito", valor))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.transacoes.append(("Saque", valor))
            return True
        else:
            return False

    def exibir_transacoes(self):
        for tipo, valor in self.transacoes:
            print(f"- {tipo}: R$ {valor:.2f}")

class GerenciadorConta:
    def __init__(self):
        self.contas = []

    def cadastrar_conta(self, nome, numero_conta, data_criacao_conta, tipo_conta):
        if self.buscar_conta(numero_conta):
            print("Conta já cadastrada")
        else:
            conta = Conta(nome, numero_conta, data_criacao_conta, tipo_conta)
            self.contas.append(conta)
            print(f"Conta cadastrada com sucesso!")

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
        print(f"Buscando conta com número: {numero_conta}")
        print(f"Tipo do número da conta: {type(numero_conta)}")
        print("Contas cadastradas:")
        for conta in self.contas:
            print(f"- Número: {conta.numero_conta}, Nome: {conta.nome}, Tipo: {type(conta.numero_conta)}")

        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                print(f"Conta encontrada: {conta.nome}")
                return conta
        print("Conta não encontrada")
        return None

    def editar_conta(self, numero_conta, novo_nome):
        conta = self.buscar_conta(numero_conta)
        if conta:
            conta.nome = novo_nome
            print("Conta editada com sucesso!")
        else:
            print("Conta não encontrada.")

    def excluir_conta(self, numero_conta):
        conta = self.buscar_conta(numero_conta)
        if conta:
            self.contas.remove(conta)
            print("Conta excluída com sucesso!")
        else:
            print("Conta não encontrada.")

    def visualizar_extrato(self, numero_conta):
        conta = self.buscar_conta(numero_conta)
        if conta:
            print("Extrato da conta:")
            print(f"Nome: {conta.nome}")
            print(f"Número da conta: {conta.numero_conta}")
            print(f"Data de abertura: {conta.data_criacao_conta}")
            print(f"Tipo de conta: {conta.tipo_conta}")
            print(f"Saldo: R$ {conta.saldo:.2f}")
            print("Transações:")
            conta.exibir_transacoes()
        else:
            print("Conta não encontrada.")


def main():
    gerenciador = GerenciadorConta()

    # Adicionando uma conta para teste
    gerenciador.cadastrar_conta("João", "1", "2023-01-01", "Poupança")

    while True:
        print("\n[1] Cadastrar uma nova conta")
        print("[2] Acessar conta")
        print("[0] Sair")

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                nome = input("Nome do titular: ")
                numero_conta = input("Número da conta: ")
                data_criacao = input("Data de criação (YYYY-MM-DD): ")
                tipo_conta = input("Tipo de conta: ")
                gerenciador.cadastrar_conta(nome, numero_conta, data_criacao, tipo_conta)
                continue

            if opcao == 2:
                numero_da_conta = input("Qual o número da sua conta? ")
                conta_existente = gerenciador.buscar_conta(numero_da_conta)

                if conta_existente:
                    while True:
                        print(f"\nSeja bem vindo {conta_existente.nome}")
                        print("-" * 30)
                        print("Informe qual operação deseja fazer")
                        print("[1] Realizar Depósito")
                        print("[2] Realizar Saque")
                        print("[3] Realizar Extrato Bancário")
                        print("[4] Editar informações da conta")
                        print("[5] Excluir conta")
                        print("[0] Voltar ao menu principal")

                        try:
                            operacao = int(input("Escolha uma opção: "))

                            if operacao == 1:
                                valor = float(input("Informe o valor do depósito: R$ "))
                                gerenciador.realizar_deposito(numero_da_conta, valor)

                            elif operacao == 2:
                                valor = float(input("Informe o valor do saque: R$ "))
                                gerenciador.realizar_saque(numero_da_conta, valor)

                            elif operacao == 3:
                                gerenciador.visualizar_extrato(numero_da_conta)

                            elif operacao == 4:
                                novo_nome = input("Informe o novo nome do titular: ")
                                gerenciador.editar_conta(numero_da_conta, novo_nome)

                            elif operacao == 5:
                                confirmacao = input("Tem certeza que deseja excluir a conta? (S/N): ")
                                if confirmacao.upper() == 'S':
                                    gerenciador.excluir_conta(numero_da_conta)
                                    print("Conta excluída com sucesso.")
                                    break
                                else:
                                    print("Operação de exclusão cancelada.")

                            elif operacao == 0:
                                print("Voltando ao menu principal.")
                                break

                            else:
                                print("Opção inválida. Tente novamente.")

                        except ValueError:
                            print("Opção inválida. Tente novamente.")

                else:
                    print("Conta não encontrada.")

            if opcao == 0:
                print("Saindo do programa. Obrigado por usar nossos serviços!")
                break

        except ValueError:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
