# Put your app in here.
from flask import Flask
from operations import add, sub, mult, div

app = Flask(__name__)
@app.route('/add')
def add_function():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(add(a,b))

@app.route('/sub')
def sub_function():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(sub(a,b))

@app.route('/mult')
def mult_function():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(mult(a,b))

@app.route('/div')
def div_function():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a,b))

@app.route('/math/<func>')
def all_funcs(func):
    a = int(request.args['a'])
    b = int(request.args['b'])

    if func == 'add':
        return str(add(a,b))
    elif func == 'sub':
        return str(sub(a,b))
    elif func == 'mult':
        return str(mult(a,b))
    else: 
        return str(div(a,b))

# via dictionary:

# funcs = {
#     'add': add,
#     'sub': sub,
#     'mult': mult,
#     'div': div,
# }

# @app.route('/math/<func>')
# def all_funcs(func):
#     a = int(request.args['a'])
#     b = int(request.args['b'])

#     return funcs[func](a,b)