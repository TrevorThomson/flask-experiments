
from flask import Blueprint
from markupsafe import escape

from api.model.fibo import Fibonacci

api = Blueprint('fibo_api', __name__)

@api.get('/fibo/<int:f>')
def fibo(f):
    fibo = Fibonacci()
    series = fibo.series(f)
    sum = fibo.sum(f)

    return f'<h1>Fibonacci({escape(f)}) = {series} which sums to {sum}</h1>', 200
