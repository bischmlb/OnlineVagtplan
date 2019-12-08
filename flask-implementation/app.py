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
    found = False
    valueLogIn = request.form.get('submit')
    username = request.form.get('username')
    password = request.form.get('password')
    if valueLogIn == "Log In": ## prøv kun at log ind hvis vi trykker log in
        file = open('users.txt', 'r+')
        for line in file:
            if username == line.split(',')[1] and password == line.split(',')[2]:
                print("login successful")
                found == True
                return render_template('userScreen.html')

        if found == False:
            print("user not found")
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
        file = open("users.txt", "r+")
        for line in file:
            if email == (line.split(',')[1]):
                print("email already registered!")
                file.close()
                return render_template('signup.html')
        file.close()

        if password == passwordRetype and password is not None and email is not None:
            knownUsers[email] = password # store new user
            user = fu.User(name, email, tlf)
            fu.storeAccount(user, password, "users.txt")
            return render_template('login.html')
        else:
            print("passwords not identical")
    return render_template('signup.html')

@app.route('/forgot', methods=['POST', 'GET'])

def forgot():
    return render_template('forgot.html')



if __name__ == '__main__':
    app.run()
