from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/table/<person>/<age>')
def table(person, age):
    return render_template('table.html', title='Оформление каюты', person=person, age=int(age))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
