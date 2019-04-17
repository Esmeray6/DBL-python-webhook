## DBL-python-webhook
Small Flask server designed to help you keep track of users who upvoted your bot on [DBL](https://discordbots.org/).

## Requirements

* [MongoDB](https://www.mongodb.com/download-center/community)
  * [pymongo](https://api.mongodb.com/python/current/installation.html)
* [Flask](https://pypi.org/project/Flask/1.0.2/)
* [Python3.6+](https://www.python.org/downloads/release/python-360/)
* [Git](https://git-scm.com/downloads)
* [requests](https://pypi.org/project/requests/)
* discord.py rewrite (v1.0.0+) `python -m pip install -U discord.py` for Windows or `pip3 install -U discord.py` for Linux and MacOS.

## Installation

1. Open terminal (MacOS/Linux) or command prompt (Windows).
2. Choose any path you want.
3. Enter `git clone https://github.com/shivaco/DBL-python-webhook.git`.

## Setting up

1. Open `settings.json` with any text editor.
2. In `webhook_password` field, enter any password you want.
3. On your bot's `Edit` page, scroll down to find `API Options` header.
4. In `URL` field, enter `http://your-public-IP:5000/dblwebhook`, where `your-public-IP` is your external IP. You can find it using "What is my IP" websites.
5. In `Authorization` field, enter what you have entered in `webhook_password` (step 2).
6. SAVE IT.

![PRESS THIS](https://i.imgur.com/OS493w6.png)

## Additional

### Webhooks

If you want this webserver to post a message in a certain channel when someone votes for your bot, follow the guide below.

1. Create a webhook in preferred channel.
2. Copy the webhook URL.
3. Open `settings.json` with any text editor.
4. In `discord_webhook_url` field, enter the webhook URL.
5. Save the file.

### Running on Windows

You will most likely have to open port 5000 on your router.

## Running

### Linux/MacOS

1. Install tmux.
2. Enter `tmux new -s flaskserver`.

   2.1. Feel free to change `flaskserver` to anything.
3. Run `bash start.sh` inside the webserver folder.

### Windows

1. Open the webserver folder.
2. Open `start.bat`.
