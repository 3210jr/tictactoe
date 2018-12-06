import random
import ast
from flask import Flask, request, send_from_directory, send_file

from model import next_play

app = Flask(__name__, static_url_path='')


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return send_file('./static/index.html')
    else:
        print(request.get_json())
        board = request.get_json()["board"]
        board = ast.literal_eval(board)
        return str(next_play(board))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# export FLASK_APP=app.py && export FLASK_ENV=development &&
# export FLASK_ENV=development
# flask run
