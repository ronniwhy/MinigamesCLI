import jokenpo
import forca
import velha

decisor = True


def menu():
    print('Estes minijogos são feitos para serem jogados em CLI.')

    print('Escolha um minijogo:\n'
          '- /jokenpo: Pedra, Papel ou Tesoura;\n'
          '- /forca: Jogo da Forca;\n'
          '- /velha: Jogo da Velha.')
    iniciador = input('Comando: /')

    if iniciador == 'jokenpo' or iniciador == 'j':
        jokenpo.jokenpo()
    elif iniciador == 'forca' or iniciador == 'f':
        forca.forca()
    elif iniciador == 'velha' or iniciador == 'v':
        velha.velha()
    else:
        print('Comando inválido. Tente novamente.')
        menu()


while decisor:
    print('Iniciar? Digite /sim ou /não')
    decisor = input('Comando: /')
    decisor = decisor.lower()
    if decisor == 'sim' or decisor == 's':
        decisor = False
        menu()
    elif decisor == 'não' or decisor == 'nao' or decisor == 'n':
        print('Script finalizado.')
        exit()
    else:
        print('Comando inválido. Tente novamente.')
