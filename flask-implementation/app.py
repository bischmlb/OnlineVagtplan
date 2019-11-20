from flask import Flask, render_template, request
app = Flask(__name__)
import os

knownUsers = {
"troels": "have",
"boller": "kohberg"
}

app.debug = True
app.config['SECRET_KEY'] = os.urandom(12)

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username in knownUsers:
        if knownUsers[username] == password:
            print("login successful!!!")
        else:
            print("password wrong")
    else:
        print("user not recognized")

    print(username)
    print(password)
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
