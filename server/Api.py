from fastapi import FastAPI
import pandas as pd

#dt_questoes = pd.read_csv('./dt_questoes.txt', sep=",")
dt_questoes = pd.read_csv('dt_questoes.csv', encoding="utf-8", sep=",", header=0)

questions_db = []
for i in range(len(dt_questoes)):
    questions_db.append({'id':i+1, 'descricao': '{}'.format(dt_questoes["descricao"][i]), 'AL1':'{}'.format(dt_questoes["AL1"][i]),'AL2':'{}'.format(dt_questoes["AL2"][i]),'AL3':'{}'.format(dt_questoes["AL3"][i]),'AL4':'{}'.format(dt_questoes["AL4"][i]),'AL5':'{}'.format(dt_questoes["AL5"][i]),'resposta':'{}'.format(dt_questoes["resposta"][i])})


users_db = [
    {'id':'1', 'nome':'cesar', 'senha':'ferlinda'},
    {'id':'2', 'nome':'admin', 'senha':'admin'}
]

app = FastAPI()

class API:
    @app.get("/user/{username}")
    def GetPassword(username):
        senha = ""
        for usuario in users_db:
            if username == usuario['nome']:
                senha = usuario['senha']
        return senha

    @app.get("/questions/{id}")
    def GetQuestion(id):
        questionMessage = ""
        for question in questions_db:
            if int(id) == question['id']:
                questionMessage = question['descricao']
        return questionMessage    
    
    @app.get("/alternatives/{id}")   
    def GetAlternativas(id):
        alternativesMessage = []
        for question in questions_db:
            if int(id) == question['id']:
                alternativesMessage.append(question['AL1'])
                alternativesMessage.append(question['AL2'])
                alternativesMessage.append(question['AL3'])
                alternativesMessage.append(question['AL4'])
                alternativesMessage.append(question['AL5'])
        return alternativesMessage        

    @app.get("/response/{id}")   
    def GetResponse(id):
        questionMessage = ""
        for question in questions_db:
            if int(id) == question['id']:
                questionMessage = question['resposta']
        return questionMessage    
    
    @app.get("/size")   
    def GetSize():
        return len(questions_db)