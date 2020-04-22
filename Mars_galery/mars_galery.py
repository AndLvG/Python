from flask import Flask, url_for, render_template, redirect, request
import os

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    root_dir = os.path.abspath(os.path.dirname(__file__))
    dir = os.path.join(root_dir, 'static', 'img', 'galery')
    images = os.listdir(dir)

    if request.method == 'GET':
        return render_template('galery.html', title='Пейзажи Марса', images=images)
    elif request.method == 'POST':
        f = request.files['file']
        with open(os.path.join(dir, f.filename), "wb") as fil:
            fil.write(f.read())
        images = os.listdir(dir)
        return render_template('galery.html', title='Пейзажи Марса', images=images)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
