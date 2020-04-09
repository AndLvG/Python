from flask import Flask, render_template, redirect, url_for, request
from data import db_session
from data.users import User, Anonymous
from data.login import LoginForm
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from werkzeug.urls import url_parse


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
DB = "db/mars_explorer.db"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.anonymous_user = Anonymous
login_manager.login_view = 'login'

@app.route("/")
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Экспедиция на Марс')

@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('success')
            return redirect(next_page)
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return render_template('success_login.html', title='Удачный вход')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

def main():
    db_session.global_init(DB)
    app.run()


if __name__ == '__main__':
    main()
