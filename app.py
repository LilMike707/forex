from flask import Flask, request, render_template
from forex_python.converter import CurrencyRates

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    value = float(request.form['amount'])
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, value)
    #return f'{value} {from_currency} is equal to {converted_amount} {to_currency}'
    return render_template('result.html', value=value, from_currency=from_currency, to_currency=to_currency, converted_amount=converted_amount)
