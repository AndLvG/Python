from flask import Flask, render_template, redirect, request, url_for
from data import db_session
from data.users import User, Anonymous
from data.jobs import Jobs
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from data.add_job import AddJobForm
from data.login import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
DB = "db/mars_explorer.db"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.anonymous_user = Anonymous
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


@app.route("/")
@app.route('/index')
@login_required
def index():
    return redirect(url_for('jobs_table'))


@app.route("/jobs_table")
@login_required
def jobs_table():
    session = db_session.create_session()
    j = session.query(Jobs).all()
    return render_template("jobs_table.html", jobs=j, title="Журнал работ")


@app.route('/addjob', methods=['GET', 'POST'])
def addjob():
    form = AddJobForm()
    if form.validate_on_submit():
        session = db_session.create_session()

        job = Jobs(
            team_leader=int(form.team_leader.data),
            job=form.job.data,
            work_size=int(form.work_size.data),
            collaborators=form.collaborators.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            is_finished=form.is_finished.data
        )

        session.add(job)
        session.commit()
        return redirect(url_for('jobs_table'))  # redirect('/jobstable')
    return render_template('addjob.html', title='Добавление нового задания', form=form)


@app.route('/editjob/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_job(id):
    form = AddJobForm()
    if request.method == "GET":
        session = db_session.create_session()
        j = session.query(Jobs).filter(Jobs.id == id).first()
        if j:
            form.team_leader.data = j.team_leader
            job = form.job.data = j.job
            form.work_size.data = j.work_size
            form.collaborators.data = j.collaborators
            form.start_date.data = j.start_date
            form.end_date.data = j.end_date
            form.is_finished.data = j.is_finished
        # else:
        #     abort(404)
    if form.validate_on_submit():
        session = db_session.create_session()
        j = session.query(Jobs).filter(Jobs.id == id).first()
        if j:
            j.team_leader = int(form.team_leader.data)
            j.job = form.job.data
            j.work_size = int(form.work_size.data)
            j.collaborators = form.collaborators.data
            j.start_date = form.start_date.data
            j.end_date = form.end_date.data
            j.is_finished = form.is_finished.data
            session.commit()
            return redirect(url_for('jobs_table'))
        # else:
        #     abort(404)
    return render_template('addjob.html', title='Редактирование задания', form=form)

@app.route('/job_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def job_delete(id):
    session = db_session.create_session()
    j = session.query(Jobs).filter(Jobs.id == id).first()
    if j:
        session.delete(j)
        session.commit()
    # else:
    #     abort(404)
    return redirect(url_for('jobs_table'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

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



def main():
    db_session.global_init(DB)
    app.run()


if __name__ == '__main__':
    main()
