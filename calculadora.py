import threading
import os
import time
import asyncio
import multiprocessing

while True:
    numero_1 = input('Digite um número:')
    numero_2 = input('Digite outro número:')
    operador = input('digite o operador(ex:+-/*):')

    numeros_válidos = None
    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_válidos = True
    except:
        numeros_válidos = None

    if numeros_válidos is None:
        print('Os números são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('operador inválido.')
        continue

    if len(operador) > 1:
        print('digite apenas um operador.')
        continue

        print('Sua conta.resultado abaixo')
    if operador == '+':
        print(numero_1_float + numero_2_float)
    elif operador == '-':
        print(numero_1_float - numero_2_float)
    elif operador == '/':
        print(numero_1_float / numero_2_float)
    elif operador == '*':
        print(numero_1_float * numero_2_float)
    else:
        print('se isso aparecer ta errado')

    sair = input('quer sair? [s]sim:').lower().startswith('s')

    if sair is True:
        break