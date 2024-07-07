# Sistema Bancário com Python

Projeto simples de um Sistema Bancário desenvolvido com Python para o bootcamp da DIO.

No desenvolvimento deste projeto, o objetivo foi colocar em prática os conceitos básicos de Python, tais como:
- Operadores lógicos.
- Operadores aritméticos.
- Estruturas condicionais.

## Funcionalidades do Sistema

- **Depósito**: Permite ao usuário depositar um valor na sua conta, exibindo uma mensagem de sucesso com o valor depositado.
- **Saque**: Permite ao usuário sacar um valor da sua conta, respeitando limites de saldo, valor máximo por saque e número máximo de saques diários.
- **Extrato**: Exibe todas as operações realizadas na conta, como depósitos e saques, além do saldo atual.
- **Criação de Usuário**: Permite a criação de novos usuários mediante a informação de CPF, nome, data de nascimento e endereço.
- **Criação de Conta**: Permite a criação de novas contas associadas a usuários existentes, especificando agência e número da conta.
- **Listar Contas**: Exibe todas as contas cadastradas no sistema, com informações de agência, número da conta e titular.

## Melhorias na Versão 2

Na versão `desafio_banco_v2.py`, foram implementadas as seguintes melhorias:

- **Depósito**: Agora, ao realizar um depósito, o sistema exibe o valor depositado em reais (R$).
- **Refatoração de Código**: Melhorias na legibilidade e clareza do código, utilizando funções auxiliares e constantes para evitar repetição de código e melhorar a organização.

## Melhorias na Versão 3

Na versão `desafio_banco_v3.py`, foram implementadas as seguintes melhorias e novas funcionalidades:

- **Depósito e Saque com Data**: Agora, ao realizar um depósito ou saque, o sistema registra a data e hora da transação e a exibe no extrato.
- **Mensagens Detalhadas de Depósito e Saque**: Mensagens adicionais foram incluídas para exibir detalhes das tentativas de depósito e saque, incluindo valores e resultados.
- **Melhoria na Estrutura do Menu**: O menu foi reorganizado para melhorar a clareza e a interação com o usuário.
- **Criação e Seleção de Clientes e Contas**: Agora é possível criar novos clientes e associar contas a eles, bem como selecionar clientes para realizar transações.

## Como Executar o Sistema

Para executar o sistema bancário, siga os seguintes passos:

1. Clone o repositório:
    ```sh
    git clone https://github.com/leognoronha/desafio_dio_banco.git
    cd desafio_dio_banco
    ```

2. Execute o script Python:
    ```sh
    python desafio_banco_v3.py
    ```

## Repositórios Git

[Documentação](https://github.com/digitalinnovationone/trilha-python-dio): Repositório com todo o código-fonte desenvolvido nesta Formação;

