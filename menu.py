import jokenpo

decisor = True

def menu():
    print('Estes minijogos são feitos para serem jogados em CLI.')

    print('Escolha um minijogo:\n'
          '- /jokenpo: Pedra, Papel ou Tesoura;')
    iniciador = input('Comando: /')

    if iniciador == 'jokenpo' or iniciador == 'j':
        jokenpo.jokenpo()

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
