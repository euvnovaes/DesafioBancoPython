# VERSÃO 1 DO DESAFIO

# menu = """

# [d] Depositar
# [s] Sacar
# [e] Extrato
# [q] Sair

# => """

# saldo = 0
# limite = 500
# extrato = ""
# numero_saques = 0
# LIMITE_SAQUES = 3

# while True:

#     opcao = input(menu)

#     if opcao == "d":
#         valor = float(input("Informe o valor do depósito: "))

#         if valor > 0:
#             saldo += valor
#             extrato += f"Depósito: R$ {valor:.2f}\n"

#         else:
#             print("Operação falhou! O valor informado é inválido.")

#     elif opcao == "s":
#         valor = float(input("Informe o valor do saque: "))

#         excedeu_saldo = valor > saldo

#         excedeu_limite = valor > limite

#         excedeu_saques = numero_saques >= LIMITE_SAQUES

#         if excedeu_saldo:
#             print("Operação falhou! Você não tem saldo suficiente.")

#         elif excedeu_limite:
#             print("Operação falhou! O valor do saque excede o limite.")

#         elif excedeu_saques:
#             print("Operação falhou! Número máximo de saques excedido.")

#         elif valor > 0:
#             saldo -= valor
#             extrato += f"Saque: R$ {valor:.2f}\n"
#             numero_saques += 1

#         else:
#             print("Operação falhou! O valor informado é inválido.")

#     elif opcao == "e":
#         print("\n================ EXTRATO ================")
#         print("Não foram realizadas movimentações." if not extrato else extrato)
#         print(f"\nSaldo: R$ {saldo:.2f}")
#         print("==========================================")

#     elif opcao == "q":
#         break

#     else:
#         print("Operação inválida, por favor selecione novamente a operação desejada.")


# print("\nObrigado por utilizar nossos serviços bancários!\n")



# VERSÃO 2 DO DESAFIO
# Criar funções para as operações existentes: Sacar, Depositar e Visualizar Extrato
# Criar 2 novas funções: Criar usuario (cliente do banco) e criar Conta corrente (vinculado ao usuario)
# Cada função deve ter uma regra na passagem de argumentos

# SAQUE:
    # A função saque deve receber argumentos apenas por nome (keyword only)
    # Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques
    # Sugestão de retorno: saldo e extrato.

# DEPOSITO:
    # Deve recer os argumentos apenas por posição (positional only)
    # Sugestão de argumento: saldo, valor e extrato
    # Sugestão de retorno: saldo e extrato

# EXTRATO:
    # Deve receber argumentos por posição e nome
    # Argumentos posicionais: saldo
    # Argumentos nomeados: extrato


# CRIAR USUARIO:
     # Deve armazenar os usuarios em uma lista
     # Um usuario é composto por: nome, data de nascimento, cpf e endereço
     # O endereço é uma sring com o formato: logradouro, numr - bairro - cidade/sigla estado
     # Armazenar somentes os numeros dos cpfs unicos

# CRIAR CONTA CORRENTE:
    # Deve armazenar contas em uma lista
    # É composta por: agencia, numero da conta e usuario
    # O numero da conta é sequencial, iniciando em 1
    # O numero da agencia é fixo "0001"
    # O usuario pode ter mais de uma conta, mas uma conta pertence a somente um funcionario


# DICA: para vincular um usuario a uma conta, filtre a lista de usuarios buscando o num do CPF informado para cada usuario da lista

import textwrap 

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor do depósito: '))

            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == 'nu':
            criar_usuario(usuarios)
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'q':
            break
        else:
            print('Operação inválida! Por favor selecione novamente a opção desejada.')

def menu():
    menu = '''
    =========== MENU ==========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuario
    [q]\tSair
    => '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print('\n=== Dpósito realizado com sucesso! ===')
    else: 
        print('\n@@@ Operação Falhou! O valor informado é inválido. @@@')

    return saldo, extrato
       
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print('\n@@@ Operação Falhou! Você não tem saldo o suficiente. @@@')
    elif excedeu_limite:
        print('\n@@@ Operação Falhou! O valor do saque excede o limite. @@@')
    elif excedeu_saques:
        print('\n@@@ Operção Falhou! Número máximo de saques excedido. @@@')
    elif valor > 0:
        saldo += valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('\n=== Saque realizado com sucesso! ===')
    else:
        print('\n@@@ Operação Falhou! O valor informado é inválido. @@@')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n=========== EXTRATO ==========')
    print('Não foram realizadas moimentações.' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('=============================')

def criar_usuario(usuarios):
    cpf = input('Informe p CPF (somente número): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n@@@ Já existe usuário com este CPF! @@@')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nmr - bairro - cidade/sigla estado): ')
    
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('=== Usuário criado com sucesso! ===')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuario: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n=== Conta criada com sucesso! ===')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('\n@@@Usuário não encontrado, fluxo de criação de conta encerrado! @@@')

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('=' * 100)
        print(textwrap.dedent(linha))

main()