import program as program


def eh_valido_fn(val: int) -> bool:
    if val >= 1 and val <= 3:
        return True
    else:
        return False

def opcoes_fn(size):
    permissao = False
    print('------------------')
    print('O que você deseja fazer?')
    print('1. Jogar')
    print('2. Verificar sua pontuação ')
    print('3. Remover suas partidas ')
    print('------------------')
    opcao = int(input('Insira uma opção: '))
    if eh_valido_fn(opcao) == True:
        if opcao == 1:
            program.quiz_fn(size)
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass

