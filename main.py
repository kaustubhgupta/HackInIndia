from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from functions import *


app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///textData.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Data(db.Model):
    serial_no = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12), nullable=True)
    content = db.Column(db.String(9999), nullable=False)


@app.route('/')
def home():
    posts = Data.query.filter_by().order_by(Data.serial_no.desc())
    return render_template('index.html', converted=posts)


@app.route('/predict', methods=["GET", "POST"])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    sentence = request.form.get("ip")
    sentence = mainPart(sentence)
    entry = Data(content=sentence, date=datetime.now())
    db.session.add(entry)
    db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

