

def saque(*,saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques



def deposito(saldo,valor, extrato,/):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato



def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")



def buscador(cpf,lista):
    B = []
    for x in lista:
        if x["cpf"] == cpf:
            B.append(x)
    return B



def criar_user(lista_user,cpf):
   
    user = input("Qual é o seu nome? ")
    data_nasc = input("Qual é sua data de nascimento? (DD/MM/AAAA) \n")
    endereco = input("Qual é o seu endereço? (logradouro, numero-bairro-cidade/sigla estado) \n")
    A = {"nome":user, "data_nasc":data_nasc, "cpf":cpf, "endereco":endereco}
    lista_user.append(A)

    return lista_user



def criar_conta(agencias, numero_conta, cpf, lista_conta):
    numero_conta += 1
    lista_conta.append({"Agência":agencias,"numero_conta":numero_conta, "cpf":cpf, "financa": {"saldo":0, "extrato": "", "numero_saques": 0 }})
    dic_conta = lista_conta[-1]
    return dic_conta 



def inicio(listauser,listaconta,number_conta): # em return, posso colocar apenas o dicionario referenciando a conta
    print("Olá, seja bem-vindo ao banco Toledo\n")
    reposta = input("""
[E] - Entrar
[S] - Sair
=> """)
    
    if reposta == 'E':
        cpF = input("\nDigite seu cpf para identificação: ") 
        k = buscador(cpF,listaconta)
        if not k:
            print("\nVocê não tem conta no banco, então iremos criar um conta agora!")
            ag = str(input("\nDigite número da agência onde deseja criar: "))
            criar_user(listauser,cpF)
            dici_conta = criar_conta(ag, number_conta,cpF,listaconta)
            
            return cpF, "0001", 0, "", 0, number_conta, dici_conta
        else:
            print("Você já está registrado no nosso banco de dados\n")
            escolha = int(input(f"Digite o número da posição da conta escolhida(1 a {len(k)}): {k}\n"))
            saldo = k[escolha-1]["financa"]["saldo"]
            extrato = k[escolha-1]["financa"]["extrato"]
            number_saquess = k[escolha-1]["financa"]["numero_saques"]
            agencia = k[escolha-1]["Agência"]
            number_conta = k[escolha-1]["numero_conta"]
            dicio_conta = k[escolha-1]
            return cpF,agencia, saldo, extrato, number_saquess, number_conta, dicio_conta 



def acao():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [q] Sair

    => """
    opcao = input(menu)
    return opcao



def registrar_naconta(saldo,extrato,conta_dicionario):
    conta_dicionario["financa"].update({"saldo": saldo, "extrato":extrato} )


###################################################################
# Parte funcional

usuarios = []

conta_lista = []

number_contaa = 0

while True:

    cpf,agencia, saldo, extrato, number_saquess, number_conta, conta_dicion = inicio(usuarios, conta_lista,number_contaa)
    limite = 500
    limite_saques = 3

    while True:

        opcao = acao()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(saldo,valor, extrato)

            registrar_naconta(saldo,extrato,conta_dicion)


        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = saque(
                saldo= saldo,
                valor= valor,
                extrato= extrato,
                limite = limite,
                numero_saques= number_saquess,
                LIMITE_SAQUES= limite_saques
            )

            registrar_naconta(saldo,extrato,conta_dicion)
            

        elif opcao == "e":
            mostrar_extrato(saldo,extrato= extrato)


        elif opcao == "q":
            break
        

        elif opcao == "nc":
            nova_agencia = str(input("Digite nova Agência: "))
            ultimo_numero_conta_registrado = conta_lista[-1]["numero_conta"]
            conta_dicion = criar_conta(nova_agencia, ultimo_numero_conta_registrado, cpf, conta_lista)
            extrato = ""
            saldo = 0
            number_saquess = 0


        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")