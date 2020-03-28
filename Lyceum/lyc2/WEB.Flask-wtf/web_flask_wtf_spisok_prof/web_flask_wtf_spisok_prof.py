from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof')
def index1():
    return render_template('index.html', title='Миссия Колонизация Марса')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
