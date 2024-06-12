from random import randrange
import json

global palavra
__version__ = '1.0.0 (beta)'


def forca():
    global palavra
    print('-> Este é um script básico do jogo da Forca em\n'
          'CLI, onde você jogará com o computador\n'
          '(ou com alguém junto a você)!')
    decisor = True

    print(f'Versão: {__version__}')
    while decisor:
        numero_de_palavras_aleatorias = 30
        print(f'-> O computador pode sortear uma entre {numero_de_palavras_aleatorias}\n'
              f'palavras aleatórias se você quiser.\n'
              f'-> Dessa forma você quem terá que adivinhá-la.\n'
              'Digite /sim ou /não (se você não quiser, deverá\n'
              'jogar com outra pessoa!)')
        decisor = input('Comando: /').lower()
        if decisor == 'sim' or decisor == 's':
            with open('recursos/forca/palavras.json', 'r', encoding='utf-8') as palavras:
                dados = json.load(palavras)
                palavraaleatoria = randrange(1, numero_de_palavras_aleatorias)
                palavraaleatoria = str(palavraaleatoria)
                sorteio = dados['palavras'][f'{palavraaleatoria}']
                palavra = f'{sorteio}'
            decisor = False
        elif decisor == 'não' or decisor == 'nao' or decisor == 'n':
            palavra = input('\n'
                            '-> Vamos nessa.\n'
                            '-> Por enquanto, só um de vocês deve\n'
                            'saber a palavra que digitar abaixo, ok?\n'
                            'Digite-a: ')
            decisor = False
        else:
            print('Comando inválido. Tente novamente.')
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    conclusao_palavra = '_' * len(palavra)
    palavra = palavra.upper()
    adivinhado = False
    letras_sugeridas = []
    palavras_sugeridas = []
    chances = 6
    print('Jogo da Forca iniciado!')
    if len(palavra) > 1:
        print(f'A palavra contém {len(palavra)} caracteres.')
    else:
        print(f'A palavra contém {len(palavra)} caractere.')
    print(f'Tamanho: ', end='')
    print(f'_' * len(palavra))
    print(f'Você tem {chances} chances.')
    print(mostrar_forca(chances))
    print(conclusao_palavra)
    print('\n')
    while not adivinhado and chances > 0:
        tentativa = input('Por favor, sugira uma letra ou palavra: ').upper()
        if len(tentativa) == 1 and tentativa.isalpha():
            if tentativa in letras_sugeridas:
                print(f'Você já sugeriu a letra "{tentativa}"', end='')
                if len(letras_sugeridas) > 1:
                    print('\nLetras já sugeridas:', end='')
                    for x in range(len(letras_sugeridas)):
                        print(f' "{letras_sugeridas[x]}"', end='')
                print('.')
            elif tentativa not in palavra:
                print(f'"{tentativa}" não está na palavra.')
                chances -= 1
                letras_sugeridas.append(tentativa)
            else:
                print(f'Você acertou! "{tentativa}" está na palavra.')
                letras_sugeridas.append(tentativa)
                palavra_como_lista = list(conclusao_palavra)
                indices = [i for i, letra in enumerate(palavra) if letra == tentativa]
                for index in indices:
                    palavra_como_lista[index] = tentativa
                conclusao_palavra = ''.join(palavra_como_lista)
                if '_' not in conclusao_palavra:
                    adivinhado = True
        elif len(tentativa) == len(palavra) and tentativa.isalpha():
            if tentativa in palavras_sugeridas:
                print(f'Você já sugeriu a palavra "{tentativa}"', end='')
                if len(palavras_sugeridas) > 1:
                    print('\nPalavras já sugeridas:', end='')
                    for x in range(len(palavras_sugeridas)):
                        print(f' "{palavras_sugeridas[x]}"', end='')
                print('.')
            elif tentativa != palavra:
                print(f'"{tentativa}" não está na palavra.')
                chances -= 1
                palavras_sugeridas.append(tentativa)
            else:
                adivinhado = True
                conclusao_palavra = palavra
        else:
            print('Não é um palpite válido.')
        print(mostrar_forca(chances))
        print(conclusao_palavra)
        print('\n')
    if adivinhado:
        print('Parabéns! Você adivinhou a palavra e, por consequência, ganhou o jogo!')
        jogardenovo()
    else:
        print(f'Suas chances acabaram. A palavra era: "{palavra}".')
        jogardenovo()


def mostrar_forca(chances):
    etapas = [
        '''
        --------
        |      |
        |      O
        |    --|--
        |     //
        |      
        -''',
        '''
        --------
        |      |
        |      O
        |    --|--
        |      /
        |      
        -''',
        '''
        --------
        |      |
        |      O
        |    --|--
        |      
        |      
        -''',
        '''
        --------
        |      |
        |      O
        |      |--
        |      
        |      
        -''',
        '''
        --------
        |      |
        |      O
        |      |
        |      
        |      
        -''',
        '''
        --------
        |      |
        |      O
        |      
        |      
        |      
        -''',
        '''
        --------
        |      |
        |      
        |    
        |      
        |     
        -'''
    ]
    return etapas[chances]


def jogardenovo():
    print('Deseja tentar de novo? Digite /sim ou /não')
    jogador = input('Comando: /')
    jogador = jogador.lower()
    if jogador == 'sim' or jogador == 's':
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        forca()
    else:
        exit()
