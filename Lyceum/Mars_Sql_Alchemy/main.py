from data.__all_models import *
from flask import Flask, render_template, redirect, url_for, request
from data import db_session
from data.users import User, Anonymous
from data.login import LoginForm
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from werkzeug.urls import url_parse
from data.register import RegisterForm


colonists = [{"surname": "Scott",
              "name": "Ridley",
              "age": 21,
              "position": "captain",
              "speciality": "research engineer",
              "address": "module_1",
              "email": "scott_chief@mars.org"},
             {"surname": "One",
              "name": "Mars1",
              "age": 21,
              "position": "medic",
              "speciality": "research medic",
              "address": "module_2",
              "email": "Mars1@mars.org"},
             {"surname": "Two",
              "name": "Mars2",
              "age": 22,
              "position": "engeneer",
              "speciality": "research engineer",
              "address": "module_3",
              "email": "Mars2@mars.org"},
             {"surname": "Three",
              "name": "Mars3",
              "age": 23,
              "position": "technik",
              "speciality": "research technik",
              "address": "module_4",
              "email": "Mars3@mars.org"}
             ]

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
            # next_page = request.args.get('next')
            # if not next_page or url_parse(next_page).netloc != '':
            #     next_page = url_for('jobs_table')
            return redirect(url_for('jobs_table'))
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

@app.route("/jobs_table")
def jobs_table():
    session = db_session.create_session()
    j = session.query(jobs.Jobs).all()
    return render_template("jobs_table.html", jobs=j, title="Журнал работ")

@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.login_email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=int(form.age.data),
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.login_email.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/success')
    return render_template('register.html', title='Регистрация', form=form)

def main():
    db_session.global_init(DB)
    # add_colonist()
    # add_job()
    app.run()


def add_colonist():
    for kosmonavt in colonists:
        user = users.User()
        user.surname = kosmonavt["surname"]
        user.name = kosmonavt["name"]
        user.age = kosmonavt["age"]
        user.position = kosmonavt["position"]
        user.speciality = kosmonavt["speciality"]
        user.address = kosmonavt["address"]
        user.email = kosmonavt["email"]
        session = db_session.create_session()
        session.add(user)
        session.commit()


def add_job():
    session = db_session.create_session()
    user = session.query(users.User).filter(users.User.id == 1).first()
    job = jobs.Jobs(team_leader=1,
                    job="deployment of residential modules 1 and 2",
                    work_size=15,
                    collaborators="2, 3",
                    is_finished=False
                    )
    user.jobs.append(job)
    session.commit()


if __name__ == '__main__':
    main()
