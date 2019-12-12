from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import fu
import os

app.debug = True
app.config['SECRET_KEY'] = os.urandom(12)

#
@app.route('/')
def index():
    return redirect('/login')


#Login page
@app.route('/login', methods=['POST', 'GET'])
def login():
    found = False                           #boolean to check if user has been found in database
    valueLogIn = request.form.get('submit') #get input for user
    username = request.form.get('username') #
    password = request.form.get('password') #
    if valueLogIn == "Log In":              #only login if the user presses the login button
        file = open('users.txt', 'r+')      #open database
        for line in file:                   #read file and check if username is found, set found to true if found
            if username == line.split(',')[1] and password == line.split(',')[2]:
                print("login successful")
                found == True
                return redirect('/user')    #redirect user to profile page

        if found == False:                  #user not found, login again
            print("user not found")
            return render_template('login.html')


    return render_template('login.html')

#Sign up page
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    valueSignUp = request.form.get('submit') #retrieve user input
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    passwordRetype = request.form.get('passRetype')
    tlf = request.form.get('phoneNumber')
    if valueSignUp == "Sign Up":             #create user if the user presses "sign up"
        file = open("users.txt", "r+")       #open and read database
        for line in file:                    #and check if email is already registered
            if email == (line.split(',')[1]):
                print("email already registered!")
                file.close()
                return redirect('/signup')   #return sign up page
        file.close()

        if password == passwordRetype and password is not None and email is not None:
            user = fu.User(name, email, tlf) #if password is valid, use our user class to store the user,
            fu.storeAccount(user, password, "users.txt") #append new user to database
            return redirect('/login')        #return login page
        else:
            print("passwords not identical") #password does not match password retype
    return render_template('signup.html')    #try to signup again

#Forgot password page
@app.route('/forgot', methods=['POST', 'GET']) #
def forgot():
    return render_template('forgot.html')

#User page
@app.route('/user', methods=['GET'])
def userScreen():
    return render_template('userScreen.html')

#kiosk working group page
@app.route('/kiosk_schedule', methods=['GET'])
def scheduleKiosk():
    return render_template('scheduleGroup1.html')

#cleaning working group page
@app.route('/cleaning_schedule', methods=['GET'])
def scheduleCleaning():
    return render_template('scheduleGroup2.html')

#ticket sales working group page
@app.route('/ticket_schedule', methods=['GET'])
def scheduleTicketSales():
    return render_template('scheduleGroup3.html')




if __name__ == '__main__':
    app.run()
