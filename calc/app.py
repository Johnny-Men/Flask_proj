from flask import Flask,request

from operations import add,sub,mult,div

app = Flask(__name__)

@app.route('/add')
def addition():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(add(a,b))

@app.route('/subtract')
def subtract():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(sub(a,b))

@app.route('/multiply')
def multiply():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(mult(a,b))

@app.route('/divide')
def divide():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a,b))

