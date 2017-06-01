import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '391800864:AAE_PSTo7ysXGookhnrkSX9XPGJ1UJ_k5pg'
WEBHOOK_URL = 'https://ee24fab5.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'state1',
	'state1_2',
	'state1_3',
        'state2',
        'state2_2',
        'state2_3',
        'state3',
        'state3_2',
        'state3_3',
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state1_2',
            'conditions': 'is_going_to_state1_2'
        },
        {
            'trigger': 'advance',
            'source': 'state1_2',
            'dest': 'state1_3',
            'conditions': 'is_going_to_state1_3'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state2_2',
            'conditions': 'is_going_to_state2_2'
        },
        {
            'trigger': 'advance',
            'source': 'state2_2',
            'dest': 'state2_3',
            'conditions': 'is_going_to_state2_3'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state3_2',
            'conditions': 'is_going_to_state3_2'
        },
        {
            'trigger': 'advance',
            'source': 'state3_2',
            'dest': 'state3_3',
            'conditions': 'is_going_to_state3_3'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1_3',
                'state2_3',
                'state3_3'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
