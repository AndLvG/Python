from flask import Flask, render_template
from data import db_session
from data import users
from data import jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
DB = "db/mars_explorer.db"


@app.route("/")
def index():
    session = db_session.create_session()
    j = session.query(jobs.Jobs).all()
    return render_template("jobs_table.html", jobs=j, title="Журнал работ")


def main():
    db_session.global_init(DB)
    app.run()


if __name__ == '__main__':
    main()
