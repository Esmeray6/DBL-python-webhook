## DBL-python-webhook
Small Flask server designed to help you keep track of users who upvoted youe bot on [DBL](https://discordbots.org/).

## Requirements

* [MongoDB](https://www.mongodb.com/download-center/community)
  * [pymongo](https://api.mongodb.com/python/current/installation.html)
* [Flask](https://pypi.org/project/Flask/1.0.2/)
* [Python3.6+](https://www.python.org/downloads/release/python-360/)
* [Git](https://git-scm.com/downloads)

## Installation

1. Open terminal (MacOS/Linux) or command prompt (Windows).
2. Choose any path you want.
3. Enter `git clone https://github.com/shivaco/DBL-python-webhook.git`.

## Running

### Linux/MacOS

1. Install tmux.
2. Enter `tmux new -s flaskserver` (change `flaskserver` to anything)
3. Run `bash start.sh` inside the webserver folder.

### Windows

1. Open the webserver folder.
2. Open `start.bat`.
