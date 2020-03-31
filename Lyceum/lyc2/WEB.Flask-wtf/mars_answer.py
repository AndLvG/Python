from flask import Flask, request, render_template

app = Flask(__name__)

inf = {"title": "",
       "surname": "Watny",
       "name": "Mark",
       "education": "Среднее",
       "profession": "штурман марсохода",
       "sex": "Мужской",
       "motivation": "Всегда мечтал попасть на марс",
       "ready": "True"
       }


@app.route('/auto_answer')
@app.route('/answer')
def form_sample():
    return render_template('answer.html', inf=inf, title="Автоматический ответ")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
