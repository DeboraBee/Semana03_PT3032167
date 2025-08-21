from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1><h2>Disciplina PTBDSWS</h2>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>' .format(name)

from flask import request

@app.route('/contextorequisicao')
def contexto_requisicao():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is{}</p>' .format(user_agent)

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