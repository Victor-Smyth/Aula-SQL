def opcao1():
    n1 = int(input('Digite um numero : '))

    controller = n1
    fatorial = 1

    while controller > 0:
        print('{}'.format(controller), end='')
        print(' x ' if controller > 1 else ' = ', end='')

        fatorial = fatorial * controller
        controller -= 1

    print(fatorial)


def opcao2():
    num = int(input('Digite um numero: '))
    razao = int(input('Digite a razão da PA: '))

    termo = num

    cont = 0
    while cont < 10:
        print('{} --> '.format(termo), end='')

        termo = termo + razao
        cont = cont + 1

    print('FIM')


def opcao3():
    numero = int(input('Digite o primeiro termo da PA: '))
    razao = int(input('Digite a razão: '))

    contador = 0
    calculo_da_PA = numero

    a_mais = 10
    total = 0

    while a_mais != 0:
        total = total + a_mais

        while contador < total:
            print('{} --> '.format(calculo_da_PA), end='')
            calculo_da_PA = calculo_da_PA + razao
            contador = contador + 1

        print('PAUSA')
        a_mais = int(input('Deseja adicionar mais numeros : '))

    print('FIM')


def opcao4():
    termos = int(input('Digite quantos termos voce quer mostrar: '))
    a = 1
    b = 0
    aux = 1
    cont = 0
    print('1', end='')

    while cont < termos:
        aux = a
        a = a + b
        b = aux
        print(' ->', a, end='')
        cont = cont + 1

    print()


def opcao5():
    num = soma = cont = 0
    while True:
        num = int(input('Digite um numero [999 para finalizar]: '))
        if num != 999:
            soma += num
            cont += 1
        else:
            break

    print('Saiu do loop', '\n')
    print('Foram digitados ao todo {} numeros e a soma dos valores é {} '.format(cont, soma))


def menu():
    print("Escolha uma opção:")
    print("Fatorial de n - 1")
    print("Exercicio 051 refeito - 2")
    print("Melhorando o exercicio 061 -3")
    print("Sequência de Fibonacci - 4")
    print("Programa 999 - 5")
    print("0 - Sair")

    opcao = int(input("Opção escolhida: "))

    if opcao == 1:
        opcao1()
    elif opcao == 2:
        opcao2()
    elif opcao == 3:
        opcao3()
    elif opcao == 4:
        opcao4()
    elif opcao == 5:
        opcao5()
    elif opcao == 0:
        print("Saindo...")
    else:
        print("Opção inválida.")
    print("\n")
    menu()


menu()
