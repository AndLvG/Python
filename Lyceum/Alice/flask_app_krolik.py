from flask import Flask, request
import logging
from flask_ngrok import run_with_ngrok
import json

app = Flask(__name__)
run_with_ngrok(app)

logging.basicConfig(level=logging.INFO)

sessionStorage = {}
buy_item = 'Слона'


@app.route('/post', methods=['POST'])
def main():
    logging.info(f'Request: {request.json!r}')
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {'end_session': False}
    }

    handle_dialog(request.json, response)
    logging.info(f'Response:  {response!r}')
    return json.dumps(response)


def handle_dialog(req, res):
    global buy_item
    user_id = req['session']['user_id']

    if req['session']['new']:

        sessionStorage[user_id] = {
            'suggests': ["Не хочу.",                "Не буду.",                "Отстань!", ]
        }
        res['response']['text'] = f'Привет! Купи {buy_item}!'
        res['response']['buttons'] = get_suggests(user_id)
        return

    if req['request']['original_utterance'].lower() in [
        'ладно',
        'куплю',
        'покупаю',
        'хорошо'
    ]:
        if buy_item == 'Кролика':
            res['response']['text'] = f'{buy_item} можно найти на Яндекс.Маркете!'
            res['response']['end_session'] = True
        else:
            buy_item = 'Кролика'
            sessionStorage[user_id] = {
                'suggests': [
                    "Не хочу.",
                    "Не буду.",
                    "Отстань!",
                ]
            }
            res['response']['text'] = f"Все говорят '{req['request']['original_utterance']}', а ты купи {buy_item}!"
            res['response']['buttons'] = get_suggests(user_id)

        return

    res['response']['text'] = \
        f"Все говорят '{req['request']['original_utterance']}', а ты купи {buy_item}!"
    res['response']['buttons'] = get_suggests(user_id)


def get_suggests(user_id):
    global buy_item
    session = sessionStorage[user_id]

    suggests = [
        {'title': suggest, 'hide': True}
        for suggest in session['suggests'][:2]
    ]

    session['suggests'] = session['suggests'][1:]
    sessionStorage[user_id] = session

    if len(suggests) < 2:
        suggests.append({
            "title": "Ладно",
            "url": f"https://market.yandex.ru/search?text={buy_item}",
            "hide": True
        })
    return suggests


if __name__ == '__main__':
    app.run()


# {
#   "request": {
#     "command": "закажи пиццу на улицу льва толстого, 16 на завтра",
#     "original_utterance": "закажи пиццу на улицу льва толстого, 16 на завтра"
#   },
#   "session": {
#     "new": true,
#     "message_id": 4,
#     "session_id": "2eac4854-fce721f3-b845abba-20d60",
#     "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
#     "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
#   },
#   "version": "1.0"
# }

# https://dialogs.yandex.ru/developer/skills/7914e0bb-2d4f-4ff3-8f56-f23fa09fec6f/draft/test
