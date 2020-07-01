from flask import Flask
from functions import *

app = Flask(__name__)


@app.route('/')
def home():
    return mainPart(sent='Can you set 2 alarms please?')


if __name__ == '__main__':
    app.run(debug=True)
