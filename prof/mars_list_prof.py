from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/list_prof/<list>')
def index1(list):
    return render_template('list_prof.html', list=list, title='Список профессий')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
