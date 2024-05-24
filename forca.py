from random import randrange
import time
import pandas as pd
import requests
import json


def forca():
    global palavra
    print('Este é um script básico do jogo da Forca em CLI,\n'
          'no qual você jogará com o computador!')

    decisor = True

    while decisor:
        print('O computador pode sortear uma palavra aleatória se você quiser. Digite /sim ou /não')
        decisor = input('Comando: /')
        decisor = decisor.lower()
        if decisor == 'sim' or decisor == 's':

            with open('palavras.json', 'r', encoding='utf-8') as palavras:
                dados = json.load(palavras)

                palavraaleatoria = randrange(1, 30)
                palavraaleatoria = str(palavraaleatoria)

                sorteio = dados['palavras'][f'{palavraaleatoria}']

                palavra = f'{sorteio}'

                print(palavra)

            decisor = False
        elif decisor == 'não' or decisor == 'nao' or decisor == 'n':
            palavra = input('Digite a palavra com que irá brincar: ')

            decisor = False
        else:
            print('Comando inválido. Tente novamente.')

    jogando = True
    while jogando:

        tentativa = len(palavra)

        print(f'Jogo da Forca iniciado!\n'
              f'São {len(palavra)} caracteres.\n'
              f'Texto: ', end='')
        print(f'_' * len(palavra))
        tentativa = input('Qual letra você sugere? ')

        for x in range(6):
            print(f'Jogo da Forca!\n'
                  f'São {len(palavra)} caracteres.\n'
                  f'Texto: ', end='')
            print(f'{tentativa} _')
            tentativa = input('Qual letra você sugere? ')

        print(f'Jogo da Forca finalizado!\n'
              f'São {len(palavra)} caracteres.\n'
              f'Texto: ', end='')
        print(f'_' * len(palavra))

    print('Deseja tentar de novo? Digite /sim ou /não')
    jogador = input('Comando: /')
    jogador = jogador.lower()
    if jogador == 'sim' or jogador == 's':
        forca()
    else:
        exit()


forca()
