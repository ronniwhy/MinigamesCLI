from random import randint
import time


def jokenpo():
    print('Este é um script básico do jogo Pedra, Papel ou Tesoura em CLI,\n'
          'no qual você jogará com o computador!')

    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print(f'{itens[computador]}')
    print(f'Qual objeto você deseja?\n'
          f'Digite 0 para Pedra\n'
          f'Digite 1 para Papel\n'
          f'Digite 2 para Tesoura')
    jogador = int(input('Opção: '))
    print('Jo')
    time.sleep(0.3)
    print('ken')
    time.sleep(0.3)
    print('pô!')
    time.sleep(0.3)

    if jogador != 0 and jogador != 1 and jogador != 2:
        print('Jogada inválida.')
        print('Script terminado. Tente novamente.')
        exit()
    if itens[jogador] == 'Pedra' and itens[computador] == 'Papel':
        print(f'O computador venceu.\n'
              f'O jogador escolheu: {itens[jogador]}.\n'
              f'O computador escolheu: {itens[computador]}.')
    elif itens[jogador] == 'Papel' and itens[computador] == 'Tesoura':
        print(f'O computador venceu.\n'
              f'O jogador escolheu: {itens[jogador]}.\n'
              f'O computador escolheu: {itens[computador]}.')
    elif itens[jogador] == 'Tesoura' and itens[computador] == 'Pedra':
        print(f'O computador venceu.\n'
              f'O jogador escolheu: {itens[jogador]}.\n'
              f'O computador escolheu: {itens[computador]}.')
    elif itens[jogador] == itens[computador]:
        print(f'Houve um empate.\n'
              f'O jogador escolheu: {itens[jogador]}.\n'
              f'O computador escolheu: {itens[computador]}.')
    else:
        print(f'O jogador venceu.\n'
              f'O jogador escolheu: {itens[jogador]}.\n'
              f'O computador escolheu: {itens[computador]}.')

    print('Deseja tentar de novo? Digite /sim ou /não')
    jogador = input('Comando: /')
    jogador = jogador.lower()
    if jogador == 'sim' or jogador == 's':
        jokenpo()
    else:
        exit()
