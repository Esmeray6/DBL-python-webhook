import sys, datetime, json, re, requests
from discord import Webhook, RequestsWebhookAdapter, Embed, Color
from flask import Flask, request, abort, jsonify
from pymongo import MongoClient
import os

with open("settings.json") as settings:
    data = json.load(settings)
    webhook_password = data['webhook_password']
    discord_webhook = data['discord_webhook_url']
    if discord_webhook != "":
        webhook_id = int(re.search(r"\d+", discord_webhook).group())
        webhook_token = re.search(r"(\w+)$", discord_webhook).group()


mongo = MongoClient()
app = Flask(__name__)

@app.route('/test', methods=['GET', 'POST'])
def test():
    return jsonify(dict(request.headers))

@app.route('/dblwebhook', methods=['POST'])
def webhook():
    sys.stdout.flush()
    if request.headers.get('Authorization') == webhook_password:
        user_id = request.json.get('user')
        bot_id = request.json.get('bot') # ID of the bot that was upvoted 
        request_type = request.json.get('type')
        weekend_status = request.json.get('isWeekend')
        now = datetime.datetime.utcnow()
        mongo.voters.vote.insert_one({
            'type': request_type,
            'user': user_id,
            'bot': bot_id,
            'weekend': weekend_status,
            'time': now
            })
        if discord_webhook != "":
            embed_title = "Test" if request_type == 'test' else 'New upvote!'
            embed = Embed(title=embed_title, description=f"**Upvoter: <@{user_id}>** ({user_id})\n**Upvoted bot:** <@{bot_id}> ({bot_id})", timestamp=datetime.datetime.utcnow(), color=Color.green())
            webhook = Webhook.partial(webhook_id, webhook_token, adapter=RequestsWebhookAdapter())
            webhook.send(embed=embed)
        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    mongo.close()
