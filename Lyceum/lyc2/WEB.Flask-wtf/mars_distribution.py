from flask import Flask, request, render_template

app = Flask(__name__)
lis = ["Арнольд Шварцнегер", "Сильвестр Сталоне",
       "Артур Пендрагон", "Жанна Д'арк"]


@app.route('/index')
@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/distribution')
def form_sample():
    return render_template('distribution.html', title="По Каютам!", list=lis)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
