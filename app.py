
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Index Page</h1>'

@app.route('/hello/<name>')
def hello(name):
    return f'<h1>Hello, {escape(name)}!</h1>'

@app.get('/fibo/<int:num>')
def fibo(num):
    a = 0
    b = 1
    output = None
    if num < 0:
        output = 'Incorrect input'
    elif num == 0:
        output = a
    elif num == 1:
        output = b
    else:
        for i in range(2, num+1):
            c = a + b
            a = b
            b = c
        output = b

    return f'<h1>Fibonacci({escape(num)}) = {output}</h1>'
