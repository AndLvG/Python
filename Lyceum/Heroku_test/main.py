from flask import Flask
# from flask_ngrok import run_with_ngrok

app = Flask(__name__)
# run_with_ngrok(app)


@app.route("/")
def index():
    return "<h1>Привет от приложения Flask</h1>"


if __name__ == '__main__':
    app.run()


# pip install flask
# pip install flask-ngrok
# pip freeze > requirements.txt
# pip install gunicorn