from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index1():
    return "на Марсе будут яблони цвести!"


@app.route('/promotion_image')
def image2():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                     <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.png')}">
</br>
{''.join(['<div class="alert alert-success">Человечество вырастает из детства.</div>',
          '<div class="alert alert-info">Человечеству мала одна планета.</div>',
          '<div class="alert alert-warning">Мы сделаем обитаемыми безжизненные пока планеты.</div>',
          '<div class="alert alert-danger">И начнем с Марса!</div>',
          '<div class="alert alert-primary">Присоединяйся!</div>'])}
                    
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
