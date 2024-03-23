import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
   getname = request.form.get('name')

   if getname:
       return render_template('hello.html', name = getname)
   else:
       return redirect(url_for('index'))

@app.route('/indexcalculate')
def indexcalculate():
    return render_template('calculadora.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    valor_a = request.form.get('valor-a')
    valor_b = request.form.get('valor-b')
    operador = request.form.get('operador')

    try:
        if operador == "+":         
            result = int(valor_a) + int(valor_b)
        if operador == "-":         
            result = int(valor_a) - int(valor_b)
        if operador == "*":         
            result = int(valor_a) * int(valor_b)
        if operador == "**":         
            result = int(valor_a) ** int(valor_b)
        if operador == "/": 
            try:      
                result = int(valor_a) / int(valor_b)
            except ZeroDivisionError as erro:
                result = "Não divisível por Zero"
        if operador == "//":         
            result = int(valor_a) // int(valor_b)
        if operador == "%":         
            result = int(valor_a) % int(valor_b)
        if operador == "raiz":         
            raiz = int(valor_a) ** (1/int(valor_b))
            result = round(raiz, 2)
    except ValueError as erro:
        result = "Por gentileza, insira valores válidos"

    return render_template('result_calc.html', result = result)

@app.route('/tarefa1')
def tarefa1():
    return render_template('tarefa1.html')

@app.route('/mediaAparada')
def mediaAparada():
    return render_template('tarefa-media-aparada.html')

@app.route('/tarefa2')
def tarefa2():
    return render_template('tarefa2.html')

if __name__ == '__main__':
   app.run()
