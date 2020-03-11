from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index1():
    return "на Марсе будут яблони цвести!"


@app.route('/results/<nickname>/<int:level>/<float:rating>', methods=['GET'])
def bootstrap(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <title>Результаты отбора</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <p class="alert alert-success" role="alert">
                      Претендент на участие: {nickname}
                    </p>
                    <p class="alert alert-primary" role="alert">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </p>
                    <p class="alert alert-secondary" role="alert">
                      Составляет {rating}
                    </p>
                    <p role="alert">
                      Желаем удачи
                    </p>
                  </body>
                </html>'''

@app.route('/greeting/<username>')
def greeting(username):
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                   integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                   crossorigin="anonymous">
                    <title>Привет, {}</title>
                  </head>
                  <body>
                    <h1>Привет, {}!</h1>
                  </body>
                </html>'''.format(username, username)

# @app.route("/promotion")
# def index2():
#     return '</br>'.join(["Человечество вырастает из детства.",
#                          "Человечеству мала одна планета.",
#                          "Мы сделаем обитаемыми безжизненные пока планеты.",
#                          "И начнем с Марса!Присоединяйся!"])
#

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')