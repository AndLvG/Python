from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask_wtf import FlaskForm
from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    id_astronavt = StringField('ID Астронавта', validators=[DataRequired()])
    pass_astronavt = PasswordField('Пароль Астроавта', validators=[DataRequired()])
    id_capitan = StringField('ID Капитана', validators=[DataRequired()])
    pass_capitan = PasswordField('Пароль Капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/')
def index():
    return "Миссия Колонизация Марса"

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/success')
def success():
    return render_template('success_login.html', title='Удачная авторизация')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
