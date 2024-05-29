# depositar valores positivos, todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato
# 3 saques diários com limite de 500 reais cada um, caso não haja saldo em conta exibir mensagem informando que não há saldo. 
# todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato
# deve listar todos os depósitos e saques, no fim exibir saldo atual da conta

menu = """
Escolha uma opção:

[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo=0 #declaração das variáveis
limite=500
extrato=""
numero_saques=0
LIMITE_SAQUES=3 #constante REGRA DE NEGÓCIO

while True:

    opcao=input(menu) #variável opcao recebe o input do usuário em menu

    if opcao == "d": #estrutura condicional simples, operador de igualdade, string d
        valor=float(input("Informe o valor do depósito: ")) #variável com tipo definido float recebe input do usuário para pergunta

        if valor>0:
            saldo+=valor #saldo recebe saldo mais valor
            extrato+= f"Depósito: R$ {valor: .2f}\n" #extrato recebe extrato mais string com fstring, concatenando valor de variável, número de casas decimais e salto de linha

        else: #ou seja, se valor for menor ou igual a 0
            print("Operação falhou! O valor informado é inválido.") #não tem f -fstring- porque não esta concatenada com uma variável

    elif opcao =="s": #estrutura condicional simples em que tem mais de duas condições
        valor=float(input("Informe o valor do saque: "))

        #definir primeiro os possíveis erros de acordo com as regras do negócio
        excedeu_saldo=valor>saldo #variável recebe afirmação
        excedeu_limite=valor>limite
        excedeu_saques=numero_saques>=LIMITE_SAQUES 

        if excedeu_saldo: #estrutura condicional dentro da opção "s" do menu; uma condicional dentro de uma condição
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite: #estrutura condicional simples com mais de uma condição
            print("Operação falhou! Você excedeu limite de saque.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor>0:
            saldo+=valor #saldo recebe saldo masi valor
            extrato+= f"Saque: R$ {valor: .2f}\n"
            numero_saques+=1 #variável numero_saques recebe mais um para acumular e verificar quando chegar na constante LIMITE_SAQUES

        else: #última condicional da estrutura, caso não seja nenhuma das anteriores, "senão"
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e": #estrutura condicional para as opções do menu
        print("\n================EXTRATO=================") #printar com salto de linha antes
        print(f"Não foram realizadas movimentações." if not extrato else extrato) #TERNÁRIO: forma concisa de excrever uma expressão condicional de forma simplificada
        #verifico se o extrato que é do tipo string esta vazio, "senão" estiver vazio eu exibo o que esta dentro da variável extrato
        print(f"\nSaldo: R$ {saldo:.2f}") #dentro da string: variável saldo é float com dois pontos após a vírgula
        print("==========================================")

    elif opcao =="q": #ainda dentro das condicionais do menu
        break #ferramenta para interromper ou encerrar um loop

    else: # última opção para encerrar as condicionais do menu
        print("Operação inválida, por favor, selecione novamente a operação desejada.") #não precisa de f porque não esta concatenada com variável