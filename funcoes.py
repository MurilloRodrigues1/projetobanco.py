from classes import Banco, Cliente, Conta, ContaCorrente, ContaPoupanca, Extrato
import os

banco = Banco()
contas = Cliente

def sistema():
    os.system("cls")
    os.system("pause")

def cadastro():
    sistema()
    try:
        while True:
            print("="*45)
            print()
            print("\tCadastre sua conta")
            print()
            print("="*45)
            try:
                nome = input("Insira seu nome\n> ")
                cpf = input("Insira seu CPF\n> ")
                senha = input("Insira sua senha\n> ")
                csenha = input("Confirme sua senha\n> ")
                # Solicita ao usuário que insira seu nome, CPF, senha e a confirmação da senha
                                
                if senha == csenha:
                # Verifica se a senha esta certa 
                    os.system("cls")
                    print("Insira seu saldo na conta corrente")
                    scorrente = float(input(">> "))
                    os.system("cls")
                    print("Conta Cadastrada com sucesso!!")
                    saldo = ContaCorrente(saldo=scorrente)

                    clientes = Cliente(nome=nome, cpf=cpf, senha=senha, saldo=saldo)
                    # Cria uma nova instância da classe Cliente com as informações

                    clientes.adicionar_conta(clientes=clientes)
                    # Adiciona a conta do cliente ao software

                    banco.adicionar_cliente(clientes)
                    # Adiciona a conta do cliente ao software

                    break

                else:
                    os.system("cls")
                    print("Erro no sistema, tente novamente!")

            except Exception as e:
                os.system("cls")
                print(f"Erro no sistema, tente novamente\n{e}")
                os.system("pause")

    except Exception as e:
        os.system("cls")
        print(f"Erro no sistema, tente novamente\n{e}")
        os.system("pause")
    # Informa que houve um erro no sistema, mostrando a mensagem de erro    

def login():
    try:
        while True:
            sistema() 
            print("="*35)
            print()
            print("\tLogin na sua conta")
            print()
            print("="*35)
            try:
                cpf = input("Insira seu CPF\n> ")
                senha = input("Insira sua senha\n> ")
                for cliente in banco.clientes:
                    autenticado, conta = cliente.consultar_conta(cpf, senha)
                    if autenticado:
                        os.system("cls")
                        print("Login efetuado com sucesso!!")
                        os.system("pause")
                        menu(conta)
                        return
               
            except Exception as e:
                os.system("cls")
                print(f"Erro no sistema, tente novamente\n{e}")
                os.system("pause")

    except Exception as e:
        os.system("cls")
        print(f"Erro no sistema, tente novamente\n{e}")
        os.system("pause")

def menu(conta):
    while True:
        sistema()
        try:
            print("="*45)
            print()
            print("\tSeja Bem vindo ao BS Bank")
            print()
            print(f"\tUsuario: {conta.getCpf()}")
            print()
            print("  [1]  -  Conta Corrente")
            print("  [2]  -  Conta Poupança")
            print("  [3]  -  Opções")
            print()
            print("  [0]  -  Voltar ao Login")
            print()
            print("="*45)
            print()
            escolha = int(input("Escolha uma opção: "))
            match escolha:

                case 1:
                    conta_corrente(conta)

                case 2:
                    conta_poupanca(conta)
                
                case 3:
                    while True:
                        os.system("cls")
                        print("="*35)
                        print()
                        print("\tOpções da Conta")
                        print()
                        print("  [1]  -  Remover Conta")
                        print("  EM BREVE!!")
                        print()
                        print("="*35)
                        escolha = int(input("Escolha uma opção: "))
                        match escolha:

                            case 1:
                                os.system("cls")
                                print("VOCÊ TEM CERTEZA QUE DESEJA EXCLUIR SUA CONTA?")
                                print()
                                print("  [1]  -  SIM")
                                print("  [2]  -  NÃO")
                                print()
                                escolha = input(">> ")
                                match escolha:

                                    case 1:
                                        clientes = input("Insira seu Nome: ")
                                        Cliente.remover_conta(clientes=clientes)
                                        break 

                                    case 2:
                                        break

                case 0:
                    sistema()
                    break
                
                case _:
                    sistema()
                    print("Erro no Sistema, tente novamente!")

        except Exception as e:
            os.system("cls")
            print(f"Erro no sistema, tente novamente\n{e}")
            os.system("pause")

def conta_corrente(conta):
    while True:
        sistema()
        print("="*35)
        print()
        print("\tConta Corrente")
        print()
        print(f"\tUsuario: {conta.getCpf()}")
        print(f"\tSaldo: {conta.getSaldo()}")
        print()
        print("  [1]  -  Depósito")
        print("  [2]  -  Saque")
        print("  [3]  -  Transferir")
        print()
        print("  [0]  -  Voltar ao Login")
        print()
        print("="*35)
        print()
        try:
            escolha = int(input("Escolha uma opção: "))
            match escolha:

                case 1:
                    os.system("cls")
                    print("="*35)
                    print()
                    print("\tDepositar dinheiro")
                    print()
                    deposito = float(input("Insira a quantidade que deesja depositar na Poupança\n>> "))
                    
                        
                case 2:
                    pass

                case 3:
                    pass
                    
                case 0:
                    sistema()
                    break
                    
                case _:
                    sistema()
                    print("Erro no Sistema, tente novamente!")

        except Exception as e:
            os.system("cls")
            print(f"Erro no sistema, tente novamente\n{e}")
            os.system("pause")

def conta_poupanca(conta):
    while True:
        sistema()
        print("="*45)
        print()
        print("\tConta Poupança")
        print()
        print(f"\tUsuario: {conta.getCpf()}")
        print(f"\tSaldo: {conta.getSaldo()}")
        print()
        print("  [1]  -  Depósito")
        print("  [2]  -  Saque")
        print()
        print("  [0]  -  Voltar ao menu")
        print()
        print("="*45)
        print()
        escolha = int(input("Escolha uma opção: "))
        try:
            escolha = int(input("Escolha uma opção: "))
            match escolha:

                case 1:
                    pass
                        
                case 2:
                    pass
                    
                case 0:
                    sistema()
                    break
                    
                case _:
                    sistema()
                    print("Erro no Sistema, tente novamente!")

        except Exception as e:
            os.system("cls")
            print(f"Erro no sistema, tente novamente\n{e}")
            os.system("pause")
