import program as program

def opcoes_fn(size):
    print('------------------')
    print('O que você deseja fazer?')
    print('1. Jogar')
    print('2. Verificar sua pontuação ')
    print('3. Remover suas partidas ')
    opcao = int(input('Insira uma opção: '))
    if opcao == 1:
        program.quiz_fn(size)
    elif opcao == 2:
        pass
    elif opcao == 3:
        pass
