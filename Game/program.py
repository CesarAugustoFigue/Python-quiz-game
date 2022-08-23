
import requests

def quiz_fn(size):
    id = 1
    proxima = True
    while id <= size:
        request_quest = requests.get('http://127.0.0.1:8000/questions/{}'.format(id))
        questao = request_quest.json()
        questao = questao['descricao']

        request_alt = requests.get('http://127.0.0.1:8000/alternatives/{}'.format(id))
        alternativas = request_alt.json()
        alternativas = alternativas['alternativas']

        request_rsp = requests.get('http://127.0.0.1:8000/response/{}'.format(id))
        rsp = request_rsp.json()
        rsp = rsp['resposta']

        Alternativa1 = ('a', alternativas[0])
        Alternativa2 = ('b', alternativas[1])
        Alternativa3 = ('c', alternativas[2])
        Alternativa4 = ('d', alternativas[3])
        Alternativa5 = ('e', alternativas[4])

        print("Questão:",questao)
        print("a)",Alternativa1[1])
        print("b)",Alternativa2[1])
        print("c)",Alternativa3[1])
        print("d)",Alternativa4[1])
        print("e)",Alternativa5[1])

        if rsp in Alternativa1:
            letra = Alternativa1[0]
        elif rsp in Alternativa2:
            letra = Alternativa1[0]
        elif rsp in Alternativa3:
            letra = Alternativa1[0]
        elif rsp in Alternativa4:
            letra = Alternativa1[0]
        elif rsp in Alternativa5:
            letra = Alternativa1[0]

        resposta = str(input('Insira sua resposta: '))
        if resposta == rsp or resposta == letra:
            proxima = True
            print()
            print('Parabéns! você acertou a resposta')
            print('--------------------------------')
            id +=1  
        else:
            print('Você errou :( -- gostaria de tentar novamente?')
            rsp = str(input("Y - N \n"))
            if rsp != 'Y' and rsp != 'N':
                print('Você precisa inserir uma resposta válida (Y - N)')
                rsp = str(input("Y - N \n"))
            if rsp == "Y":
                id -=1
            print('--------------------------------')
            id +=1