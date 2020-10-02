from time import sleep
import os

def calcular():
    es = 1
    while es:
        print('Menu de opções''\n(1). Somar' '\n(2). Subtrair' '\n(3). Multiplicar''\n(4). Dividir ''\n(5). Sair')
        es = str(input('\tDigite a operação desejada: '))
        if es > '5':
            print('Opção inválida')
            sleep(2)
            calcular()
        if es == '5':
            print('Operação encerrada!')
            break
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        if es == '1':
            os.system('cls')
            print(f'Resultado da soma: {n1 + n2}')
        if es == '2':
            os.system('cls')
            print(f'Resultado da subtração: {n1 - n2}')
        if es == '3':
            os.system('cls')
            print(f'Resultado da multiplicação: {n1 * n2}')
        if es == '4':
            os.system('cls')
            print(f'Resultado da divisão: {n1 / n2}')
            sleep(2)

os.system('cls') # Limpar terminal
calcular()
