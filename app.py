from flask import Flask, render_template, redirect
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    name = "YURIY"
    resp = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
    if resp.status_code == 200:
        for i in resp.json():
            print('{} - купівля {} продаж {}'.format(i['ccy'], i['buy'], i['sale']))
    return render_template('index.html', name=name, resp=resp.json())

@app.route('/google', methods=['GET'])
def google():
    return redirect("https://www.google.com")

@app.route('/matruchka', methods=['GET'])
def matruchka():
    return render_template("matruchka.html")