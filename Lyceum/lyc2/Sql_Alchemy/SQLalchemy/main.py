from flask import Flask
from SQLalchemy.data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.sqlite")


def main():
    app.run()


if __name__ == '__main__':
    main()
