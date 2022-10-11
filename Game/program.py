
import requests
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

try:
	db_connection = mysql.connector.connect(host='localhost', user='root', password='@Juninho00', database='quiz_db')
	print("Database connection made!")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database doesn't exist")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("User name or password is wrong")
	else:
		print(error)
else:
	db_connection.close()


def quiz_fn(size, usuario):
    print()
    id = 1
    proxima = True
    while id <= size:
        request_quest = requests.get('http://127.0.0.1:8000/questions/{}'.format(id))
        questao = request_quest.json()

        request_alt = requests.get('http://127.0.0.1:8000/alternatives/{}'.format(id))
        alternativas = request_alt.json()

        request_rsp = requests.get('http://127.0.0.1:8000/response/{}'.format(id))
        rsp = request_rsp.json()

        Alternativa1 = ('a', alternativas[0].strip())
        Alternativa2 = ('b', alternativas[1].strip())
        Alternativa3 = ('c', alternativas[2].strip())
        Alternativa4 = ('d', alternativas[3].strip())
        Alternativa5 = ('e', alternativas[4].strip())

        print("Questão:",questao)
        print("a)",Alternativa1[1])
        print("b)",Alternativa2[1])
        print("c)",Alternativa3[1])
        print("d)",Alternativa4[1])
        print("e)",Alternativa5[1])

        data_inicial = datetime.now()
        letra = ""
        rsp = rsp.strip()
        if rsp in Alternativa1:
            letra = Alternativa1[0]
        elif rsp in Alternativa2:
            letra = Alternativa2[0]
        elif rsp in Alternativa3:
            letra = Alternativa3[0]
        elif rsp in Alternativa4:
            letra = Alternativa4[0]
        elif rsp in Alternativa5:
            letra = Alternativa5[0]

        db_connection = mysql.connector.connect(host='localhost', user='root', password='@Juninho00', database='quiz_db')
        cursor = db_connection.cursor()

        resposta = str(input('Insira sua resposta: '))
        data_final = datetime.now()
        if resposta == rsp or resposta == letra:
            proxima = True
            sql = "INSERT INTO respostaQuiz (userName, numQuestion, typeQuestion, resposta, begin_date, end_date) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (str(usuario), id, 'Historia', 1, data_inicial, data_final)
            print()
            print('Parabéns! você acertou a resposta')
            print('--------------------------------')
            id +=1  
        else:
            print('Você errou :( -- gostaria de tentar novamente?')
            sql = "INSERT INTO respostaQuiz (userName, numQuestion, typeQuestion, resposta, begin_date, end_date) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (str(usuario), id, 'Historia', 0, data_inicial, data_final)
            rsp = str(input("Y - N \n"))
            if rsp != 'Y' and rsp != 'N':
                print('Você precisa inserir uma resposta válida (Y - N)')
                rsp = str(input("Y - N \n"))
            if rsp == "Y":
                id -=1
            print('--------------------------------')
            id +=1
        cursor.execute(sql, values)
        cursor.close()
        db_connection.commit()
db_connection.close()