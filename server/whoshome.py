import os
import json

import requests

app = Flask(__name__)

def get_devices:():
    msg = ''
    # get all the names from db
    return msg

def add_to_db(mac, name):
    # add mac and user to database
    pass

@app.route('/update/', methods=['POST'])
def update_macs():
    #update table
    pass

def add_user(mac, user):
    # add the row to the db
    send_message('Dog added.')

@app.route('/', methods=['POST'])
def webhook():
    text = data['text']
    if text == '/whoshome':
        send_whos_home()
    textsplit = text.split(' ', 1)
    else if textsplit[0] == '/add':
        add_user(textsplit[1], textsplit[2])
    else:
        send_message('got a message, big dawg')


def send_message(msg):
	url = 'https://api.groupme.com/v3/bots/post'
	template = {
			'bot_id' : os.environ.get('WHOSHOME_BOT_ID'),
			'text' : msg
			}
	payload = json.dumps(template)
        response = requests.post(os.get_environ('https://api.groupme.com/v3/bots/', data = payload
	print(json)
