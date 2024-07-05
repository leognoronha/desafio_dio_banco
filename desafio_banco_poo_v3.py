from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > self._saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False

        if valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = sum(1 for transacao in self.historico.transacoes if transacao["tipo"] == "Saque")

        if valor > self._limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            return False

        if numero_saques >= self._limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False

        return super().sacar(valor)

    def __str__(self):
        return f"""\
            Agência: {self.agencia}
            C/C: {self.numero}
            Titular: {self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

def menu():
    clientes = []
    conta = None
    cliente_selecionado = None

    while True:
        print("\n=== Menu ===")
        print("1. Adicionar Cliente")
        print("2. Selecionar Cliente")
        print("3. Criar Conta para Cliente Selecionado")
        print("4. Depositar")
        print("5. Sacar")
        print("6. Ver saldo")
        print("7. Ver histórico")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento: ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
            clientes.append(cliente)
            print(f"Cliente {nome} adicionado com sucesso!")

        elif opcao == "2":
            if not clientes:
                print("Nenhum cliente cadastrado.")
                continue

            print("Clientes:")
            for i, cliente in enumerate(clientes):
                print(f"{i + 1}. {cliente.nome}")

            indice = int(input("Selecione o cliente pelo número: ")) - 1
            if 0 <= indice < len(clientes):
                cliente_selecionado = clientes[indice]
                print(f"Cliente {cliente_selecionado.nome} selecionado.")
            else:
                print("Cliente inválido.")
                continue

        elif opcao == "3":
            if not cliente_selecionado:
                print("Nenhum cliente selecionado.")
                continue

            numero = input("Número da Conta: ")
            conta = ContaCorrente.nova_conta(cliente_selecionado, numero)
            cliente_selecionado.adicionar_conta(conta)
            print(f"Conta {numero} criada para o cliente {cliente_selecionado.nome}.")

        elif opcao == "4":
            if not conta:
                print("Nenhuma conta criada.")
                continue

            valor = float(input("Informe o valor do depósito: "))
            deposito = Deposito(valor)
            cliente_selecionado.realizar_transacao(conta, deposito)

        elif opcao == "5":
            if not conta:
                print("Nenhuma conta criada.")
                continue

            valor = float(input("Informe o valor do saque: "))
            saque = Saque(valor)
            cliente_selecionado.realizar_transacao(conta, saque)

        elif opcao == "6":
            if not conta:
                print("Nenhuma conta criada.")
                continue

            print(f"\n=== Saldo: R$ {conta.saldo:.2f} ===")

        elif opcao == "7":
            if not conta:
                print("Nenhuma conta criada.")
                continue

            print("\n=== Histórico de transações ===")
            for transacao in conta.historico.transacoes:
                print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")

        elif opcao == "8":
            print("Saindo...")
            break

        else:
            print("\n@@@ Opção inválida! Tente novamente. @@@")

if __name__ == "__main__":
    menu()
