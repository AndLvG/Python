from flask import Flask
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/blogs.sqlite'


def main():
    db_session.global_init("blogs.sqlite")
    app.run()


if __name__ == '__main__':
    main()