from random import randrange

_version_ = '0.0.1 (alpha)'


def jogodavelha():
    print('Este é um script básico do jogo da velha, onde\n'
          'você jogará com o computador (ou com alguém junto a você)!\n'
          'Esta é uma produção que pode ter melhorias.')
    decisor = True

    print(f'Versão: {_version_}')

    while decisor:
        print('Jogo da Velha iniciado!')
        print('Digite 0 para X\n'
              'Digite 1 para O')
        escolha = input('Qual será sua escolha? ')
        if escolha == '0':
            jogador = ['x', 'o']
            itemjogador = [jogador[0].upper(), jogador[1].upper()]
        else:
            jogador = ['x', 'o']
            itemjogador = [jogador[0].upper(), jogador[1].upper()]
        print(f'O Jogador 1 ficou com: {itemjogador[0].upper()}.')
        print(f'O Jogador 2 ficou com: {itemjogador[1].upper()}.')

        jogando = True
        tabuleiro = ['0', '1', '2',
                     '3', '4', '5',
                     '6', '7', '8']

        while jogando:
            for y in range(9):
                tentativa = True
                while tentativa:
                    aux = y
                    if aux % 2 == 0:
                        aux = 0
                    else:
                        aux = 1
                    print(y)
                    print(aux)
                    print(f'''>>> Tabuleiro
                          {tabuleiro[0]}  | {tabuleiro[1]}  | {tabuleiro[2]}   \n
                          {tabuleiro[3]}  | {tabuleiro[4]}  | {tabuleiro[5]}   \n
                          {tabuleiro[6]}  | {tabuleiro[7]}  | {tabuleiro[8]}   \n''')
                    print(f'Jogador {itemjogador[aux].upper()}:')
                    jogador[aux] = int(input('Digite o valor de acordo com o tabuleiro: '))
                    for x in range(len(tabuleiro)):
                        if tabuleiro[jogador[aux]] == itemjogador[0] or tabuleiro[jogador[aux]] == itemjogador[1]:
                            print('Essa posição já está preenchida.')
                            break
                        else:
                            print('Registrado.')
                            tabuleiro[jogador[aux]] = itemjogador[aux]
                            tentativa = False
                            break

            jogando = False

            print('Jogo da Velha finalizado!\n'
                  'Houve um empate.')
            jogardenovo()


def jogardenovo():
    print('Deseja tentar de novo? Digite /sim ou /não')
    jogador = input('Comando: /')
    jogador = jogador.lower()
    if jogador == 'sim' or jogador == 's':
        jogodavelha()
    else:
        exit()


__name__ = '__main__'
if __name__ == '__main__':
    jogodavelha()
