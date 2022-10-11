import requests
import opcoes as opcoes

request_size = requests.get('http://127.0.0.1:8000/size')
size = request_size.json()

lista_respostas_certas = []

lista_respostas_erradas = []


usuario = str(input('digite o seu usuário: '))
senha = str(input('digite a sua senha: '))
    
request_senha = requests.get('http://127.0.0.1:8000/user/{}'.format(usuario))
senha_req = request_senha.json()
    
    
if senha_req != senha:
    print('Esse usuário não está cadastrado')
else:
    opcoes.opcoes_fn(size, usuario)
    



    