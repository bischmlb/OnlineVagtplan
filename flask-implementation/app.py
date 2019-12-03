from flask import Flask, render_template, request
app = Flask(__name__)
from fu import *
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


@app.route('/login', methods=['POST', 'GET'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username in knownUsers:
        if knownUsers[username] == password:
            print("login successful!!!")
        else:
            print("password wrong")
            return render_template('login.html')
    else:
        print("user not recognized")
        return render_template('login.html')

    print(username)
    print(password)
    return render_template('userScreen.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    if username in knownUsers:
        print("username already taken!")
        return render_template('signup.html')
    else:
        knownUsers[username] = password
    print(knownUsers)
    return render_template('signup.html')


if __name__ == '__main__':
    app.run()
    user_1 = User("John","John@shitmeister.com","23 24 25 26")
    user_2 = User("Carl","Carl@shitmeister.com","24 23 26 27")
    group_1 = Group(1)
    group_2 = Group(2)
    group_1.add_user(user_1)
    group_1.add_user(user_2)
    group_1.listMembers()


    print(fu.listUsers())
