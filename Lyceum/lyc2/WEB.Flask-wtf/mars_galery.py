from flask import Flask, url_for, render_template, redirect, request
import os

app = Flask(__name__)

images = os.listdir(os.path.dirname(
    os.path.abspath(__file__)) + "\\static\\img\\galery")

print(images)


@app.route('/index')
@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    if request.method == 'GET':
        return render_template('galery.html', title='Пейзажи Марса', images=images)
    elif request.method == 'POST':
        f = request.files['file']
        with open(os.path.dirname(
                os.path.abspath(__file__)) + "\\static\\img\\galery\\" + f.filename, "wb") as fil:
            fil.write(f.read())
        images = os.listdir(os.path.dirname(
            os.path.abspath(__file__)) + "\\static\\img\\galery")
        return render_template('galery.html', title='Пейзажи Марса', images=images)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
