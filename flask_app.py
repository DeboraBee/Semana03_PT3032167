from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1><b>Avaliação contínua: Aula 030</b></h1><ul><li><a href="https://deborange.pythonanywhere.com/">Home</a></li><li><a href="https://deborange.pythonanywhere.com/user/Débora Laranjeira da Silva/PT3032167/IFSP">Identificação</a></li><li><a href="https://deborange.pythonanywhere.com/contextorequisicao">Contexto da requisição</a></li></ul>'

@app.route('/user/<nome>/<prontuario>/<instituicao>')
def identificacao(nome, prontuario, instituicao):
    return f'<h1>Avaliação contínua: Aula 030</h1><h2>Aluno: {nome}</h2><h2>Prontuário: {prontuario}</h2><h2>Instituição: {instituicao}</h2><p><a href="https://deborange.pythonanywhere.com/">Voltar</a></p>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>' .format(name)

from flask import request

@app.route('/contextorequisicao')
def contextorequisicao():
    requisicao = request.headers.get('User-Agent')
    IP = request.remote_addr
    host = request.host
    return f'<h1>Avaliação contínua: Aula 030</h1><h2>Seu navegador é: {requisicao}</h2><h2>O IP do computador remoto é: {IP}</h2><h2>O host da aplicação é: {host}</h2><p><a href="https://deborange.pythonanywhere.com/">Voltar</a></p>'

@app.route('/codigostatusdiferente')
def cod_status_diferente():
    return '<p>Bad request</p>' , 400

from flask import make_response

@app.route('/objetoresposta')
def objeto_resposta():
    response = make_response('<h1>This document carries a cookie!</h1>' )
    response.set_cookie('answer', '42')
    return response

from flask import redirect

@app.route('/redirecionamento')
def redirecionamento():
    return redirect('https://ptb.ifsp.edu.br/')

from flask import abort

@app.route('/abortar')
def abortar():
    abort(404)