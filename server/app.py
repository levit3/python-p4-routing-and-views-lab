#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:number>')
def count(number):
    cs = ''
    for i in range(number):
        print(i)
        cs += f'{i}\n'
    return cs

@app.route('/math/<num1>/<operator>/<num2>')
def math(num1, operator, num2):
    if operator == '+':
        return f'{int(num1) + int(num2)}'
    elif operator == '-':
        return f'{int(num1) - int(num2)}'
    elif operator == '*':
        return f'{int(num1) * int(num2)}'
    elif operator == 'div': 
        return f'{int(num1) / int(num2)}'
    elif operator == '%':
        return f'{int(num1) % int(num2)}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
