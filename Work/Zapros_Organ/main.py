from data import users
from flask import Flask, render_template, redirect, url_for
from data import db_session
from data.users import User, Anonymous
from data.login import LoginForm
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from data.register import RegisterForm
from data.zapros import ZaprosForm
import database_work
from flask import send_file

global df
df = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
DB = "db/zapros.db"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.anonymous_user = Anonymous
login_manager.login_view = 'login'


@app.route("/", methods=['GET', 'POST'])
@login_required
def zapros():
    form = ZaprosForm()
    if form.validate_on_submit():
        fam = form.fam.data
        im = form.im.data
        ot = form.ot.data
        dr = form.dr.data
        god_dr = form.god_dr.data
        date_begin = form.date_begin.data
        date_end = form.date_end.data

        global df
        df, comment = database_work.make_zapros(fam=fam, im=im, ot=ot, dr=dr, god_dr=god_dr, date_begin=date_begin,
                                                date_end=date_end)
        res = None
        if not df.empty:
            new_df = df.drop(['Дата начала лечения', 'ОГРН МО', 'Адрес МО', 'Телефон МО', 'Тип документа', 'Серия и номер документа'], axis=1)
            res = new_df.to_html(classes='data', index=False, header=True)
        return render_template('zapros.html', title='Поиск застрахованного', form=form,
                               results=res, show=comment)

    return render_template('zapros.html', title='Поиск застрахованного', form=form)



@app.route('/downloadfile', methods=['GET'])
@login_required
def downloadfile():
    global df
    database_work.save_excel(df)
    return send_file('temp.xlsx', as_attachment=True, attachment_filename='temp.xlsx', cache_timeout=0)

@app.route('/zapros_2_FSS', methods=['GET'])
@login_required
def zapros_2_FSS():
    global df
    database_work.save_excel_2_FSS(df)
    return send_file('temp_2_FSS.xlsx', as_attachment=True, attachment_filename='temp_2_FSS.xlsx', cache_timeout=0)


# @app.route('/v_excel')
# def v_excel():
#     print('enter')
#     if not df.empty:
#         database_work.save_excel(df)
#
#         try:
#             print('send')
#             return send_file('temp.xlsx', as_attachment=True, attachment_filename='temp.xlsx')
#             print('send2')
#
#         except Exception as e:
#             return str(e)
#     return "nothing"


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('zapros'))
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.login == form.login.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('zapros'))
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.login == form.login.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            login=form.login.data,
            ppp=form.password.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


def main():
    db_session.global_init(DB)
    # app.run(host='0.0.0.0')

    app.run(host='127.0.0.2', port=8081, debug=False)

    # from gevent import monkey
    # monkey.patch_all()
    #
    # from gevent.pywsgi import WSGIServer
    #
    # http_server = WSGIServer(('0.0.0.0', 5000), app)
    # http_server.serve_forever()


if __name__ == '__main__':
    main()

# pip install flask
# pip install sqlalchemy
# pip install flask_wtf
# pip freeze > requirements.txt
