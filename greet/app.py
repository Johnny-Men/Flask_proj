from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "<p>welcome</p>"

@app.route('/welcome/home')
def welcome_home():
    return "<p>welcome home"

@app.route('/welcome/back')
def welcome_back():
    return "<p>welcome back</p>"

    
