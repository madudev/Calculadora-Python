from time import sleep
def calcular():
    es = 1
    while es:
        print ('Menu de opções''\n(1). Somar' '\n(2). Subtrair' '\n(3). Multiplicar''\n(4). Divir ''\n(5). Sair')
        es = str(input('Digite a operação desejada: '))
        if es > '5':
             print('Opção inválida')
             sleep(2)
             calcular()
        if es=='5':
            print('Operação encerrada')
            break
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segundo numero: '))
        if es == '1':
            print(n1 + n2)
        if es == '2':
            print(n1 - n2)
        if es == '3':
            print(n1 * n2)
        if es == '4':
            print(n1 / n2)
            sleep(2)
calcular()

