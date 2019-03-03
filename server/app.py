import os
import json
from flask import Flask, request
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Resident

@app.route('/api/v1/', methods=['POST'])
def webhook():
    print(request)
    data = request.get_json()
    if data['text'] == '/whoshome':
        send_whos_home()
    textsplit = data['text'].split(' ')
    if textsplit[0] == '/add':
        add_user(textsplit[1], textsplit[2])
    elif textsplit[0] == '/confirm' and data['name'] == os.environ['WH_ADMIN']:
        confirm_user(textsplit[1])
    # flask complains about returning None
    return 'OK'

@app.route('/')
def splashpage():
    return 'whoshome'

def send_whos_home():
    msg = 'Here\'s who\'s home:'
    try: 
        residents = Resident.query.filter(Resident.is_home==True, Resident.is_confirmed==True)
        if residents.first() is None:
            msg = 'No one\'s home!'
        for res in residents:
            msg += "\n" + res.name
    except Exception as e:
        print(str(e))
        msg = 'Shit, I have no idea who\'s home.'
    send_message(msg)
    print('Message sent:' + '\n' + msg)
    

def add_user(mac, name):
    msg = name + ' added.'
    print(mac + " " + name)
    new = Resident(mac, name, False, False)
    try:
        db.session.add(new)
        db.session.commit()
    except Exception as e:
        print(str(e))
        msg = name + ' was not added.'
    send_message(msg)
    print('Message sent: ' + msg)

def confirm_user(name):
    msg = name + ' confirmed.'
    try:
        res = Resident.query.filter_by(name=name).first()
        res.is_confirmed=True
        db.session.commit()
    except Exception as e:
        print(str(e))
        msg = name + ' was not confirmed.'
    send_message(msg)

@app.route('/api/v1/update/', methods=['POST'])
def update_macs():
    print('hit api')
    print(request)
    json_object = request.get_json()
    #json_object = json.loads(data)
    print(json_object)
    print('macs:' + str(json_object['macs']))
    for res in Resident.query.all():
        res.is_home = False
        db.session.commit()
    for addr in json_object['macs']:
        res = Resident.query.filter_by(mac=str(addr)).first()
        if res:
            print(res.name + ' just got home.')
            res.is_home=True
            db.session.commit()
    print('Macs updated.')
    return 'OK'

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'
    payload = {
    		'bot_id' : os.environ['WHOSHOME_BOT_ID'],
    		'text' : msg
		}
    response = requests.post(url, data=payload)
    print(payload)
