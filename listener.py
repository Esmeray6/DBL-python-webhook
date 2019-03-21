import sys, datetime
from flask import Flask, request, abort, jsonify
from pymongo import MongoClient
import os

with open("settings.json") as settings:
    webhook_password = settings['webhook_password']

mongo = MongoClient()
app = Flask(__name__)

@app.route('/test', methods=['GET', 'POST'])
def test():
    return jsonify(dict(request.headers))

@app.route('/dblwebhook', methods=['POST'])
def webhook():
    sys.stdout.flush()
    if request.headers.get('Authorization') == webhook_password:
        mongo.voters.vote.insert_one({'type': request.json.get('type'),
            'user': request.json.get('user'),
            'bot': request.json.get('bot'),
            'weekend': request.json.get('isWeekend'),
            'time': datetime.datetime.utcnow()})
        print(request.json)
        #print(request.json)
        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
