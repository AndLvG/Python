from flask import Flask, render_template, redirect, request, url_for
from data import db_session
from data.users import User, Anonymous
from data.jobs import Jobs
from data.register import RegisterForm
from data.add_job import AddJobForm
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

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


@app.route("/jobstable", methods=['GET', 'POST'])
def jobs_table():
    session = db_session.create_session()
    j = session.query(Jobs).all()
    return render_template("jobs_table.html", jobs=j, title="Журнал работ")



def main():
    db_session.global_init(DB)
    app.run()


if __name__ == '__main__':
    main()
