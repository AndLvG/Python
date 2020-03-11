from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            на участие в миссии
                            <div>
                                <form class="login_form" method="post">
                                    <input type="fam" class="form-control" id="fam" placeholder="Введите фамилию" name="fam">
                                    <input type="im" class="form-control" id="im" placeholder="Введите фамилию" name="im">
</br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="obrazovanie">
                                          <option>Начальное</option>
                                          <option>Среднеее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>

<div class="form-group">
                                        <label for="form-check">Какие у вас есть професии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="pr1" value="pr1">
                                          <label class="form-check-label" for="pr1">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="pr2" value="pr2">
                                          <label class="form-check-label" for="pr2">
                                            Инженер-строитель
                                          </label>
                                        </div>
<div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="pr3" value="pr3">
                                          <label class="form-check-label" for="pr3">
                                            Пилот
                                          </label>
                                        </div>
<div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="pr4" value="pr4">
                                          <label class="form-check-label" for="pr4">
                                            Метеоролог
                                          </label>
                                        </div>
<div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="pr5" value="pr5">
                                          <label class="form-check-label" for="pr5">
                                            Инженер по жизнеобеспечению
                                          </label>
                                        </div>
<div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="pr6" value="pr6">
                                          <label class="form-check-label" for="pr6">
                                            Инженер по радиационной защите
                                          </label>
                                        </div>
<div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="pr7" value="pr7">
                                          <label class="form-check-label" for="pr7">
                                            Врач
                                          </label>
                                        </div>
<div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="pr8" value="pr8">
                                          <label class="form-check-label" for="pr8">
                                            Экзобиолог
                                          </label>
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <label for="about"Почему вы хотите принять участие в мисиии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['fam'])
        print(request.form['im'])
        print(request.form['email'])
        print(request.form['obrazovanie'])
        print(request.form['prof'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
