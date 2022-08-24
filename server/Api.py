from fastapi import FastAPI
        
questions_db = [
    {'id':'1', 'descricao': 'Que pais tem o formato de uma bota?', 'AL1':'Butao','AL2':'Brasil','AL3':'Portugal','AL4':'Italia','AL5':'Mexico','resposta':'Italia'},
    {'id':'2', 'descricao': 'Quem inventou a lâmpada?', 'AL1':'Graham Bell','AL2':'Steve Jobs','AL3':'Thomas Edison','AL4':'Henry Ford','AL5':'Santos Dumont','resposta':'Thomas Edison'}
]

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
            if id == question['id']:
                questionMessage = question['descricao']
        return questionMessage    
    
    @app.get("/alternatives/{id}")   
    def GetAlternativas(id):
        alternativesMessage = []
        for question in questions_db:
            if id == question['id']:
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
            if id == question['id']:
                questionMessage = question['resposta']
        return questionMessage    
    
    @app.get("/size")   
    def GetSize():
        return len(questions_db)