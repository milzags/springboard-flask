from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome_route():
    return 'welcome'
    
@app.route('/welcome/home')
def welcome_home_route():
    return 'welcome home'

@app.route('/welcome/back')
def welcome_back_route():
    return 'welcome back'

