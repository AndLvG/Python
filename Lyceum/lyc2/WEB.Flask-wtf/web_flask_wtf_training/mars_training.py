from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"

@app.route('/training/<prof>')
def index1(prof):
    return render_template('index.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
