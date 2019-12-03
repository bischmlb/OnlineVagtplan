from flask import Flask, render_template, request
app = Flask(__name__)
import fu
import os

knownUsers = {
"troels@live.dk": "have",
"boller": "kohberg"
}

app.debug = True
app.config['SECRET_KEY'] = os.urandom(12)

@app.route('/')
def index():
    return render_template('login.html')


#Login page
@app.route('/login', methods=['POST', 'GET'])
def login():
    valueLogIn = request.form.get('submit')
    username = request.form.get('username')
    password = request.form.get('password')
    if valueLogIn == "Log In": ## prøv kun at log ind hvis vi trykker log in
        if username in knownUsers:
            if knownUsers[username] == password:
                print("login successful!!!")
                return render_template('userScreen.html')
            else:
                print("password wrong")
                return render_template('login.html')
        else:
            print("user not recognized")
            return render_template('login.html')

    return render_template('login.html')

#Sign up page
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    valueSignUp = request.form.get('submit')
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    passwordRetype = request.form.get('passRetype')
    tlf = request.form.get('phoneNumber')
    if valueSignUp == "Sign Up": #lav kun ny bruger hvis vi trykker "signup"
        if email in knownUsers:
            print("email already registered!")
            return render_template('signup.html')
        else:
            if password == passwordRetype and password is not None and email is not None:
                knownUsers[email] = password # store new user
                user = fu.User(name, email, tlf)
                fu.listUsers()
                return render_template('login.html')
            else:
                print("passwords not identical")

    return render_template('signup.html')



if __name__ == '__main__':
    troels = fu.User("Troels","troels@live.dk","23 24 25 26")
    app.run()
