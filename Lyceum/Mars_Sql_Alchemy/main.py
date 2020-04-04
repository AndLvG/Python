from flask import Flask
from data import db_session
from data import users
from data import jobs
import datetime

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


def main():
    db_session.global_init(DB)
    # add_colonist()
    add_job()
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
