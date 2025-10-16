def bem_vindo():
    print("**************************************")
    print("Calculadora simples em Python")
    print("**************************************")
    calcular()

def calcular():
    while True:
        print("\nQual operação deseja executar? (1) Soma (2) Subtração (3) Multiplicação (4) Divisão (5) Outra")
        operacao_str = input("Digite a operação a ser realizada: ")
        try:
            operacao = int(operacao_str)
            if 1 <= operacao <= 5:
                break
            else:
                print("Opção inválida. Por favor, digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


    if(operacao == 5 ):
        print("Desculpe, esta calculadora ainda não suporta outras operações. Por favor, execute o programa novamente.")
        return

    while True:
        primeiro_numero_str = input("Digite o primeiro número: ")
        try:
            primeiro_numero = int(primeiro_numero_str)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    while True:
        segundo_numero_str = input("Digite o segundo número: ")
        try:
            segundo_numero = int(segundo_numero_str)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


    if(operacao == 1):
        print("O resultado é", primeiro_numero + segundo_numero)
    elif(operacao == 2):
        print("O resultado é", primeiro_numero - segundo_numero)
    elif(operacao == 3):
        print("O resultado é", primeiro_numero * segundo_numero)
    else:
        print("O resultado é", primeiro_numero / segundo_numero)

    calcular_outra_vez()


def calcular_outra_vez():
    outra_vez = input("Deseja realizar outra operação? Por favor, digite S para SIM ou N para NÃO: ")

    if outra_vez.upper() == 'S':
        calcular()
    elif outra_vez.upper() == 'N':
        print('Até a próxima!')
    else:
        print("Opção inválida.")
        calcular_outra_vez()