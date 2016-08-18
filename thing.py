from flask import Flask
app = Flask(__name__)
from flask import render_template, request
import requests
# from requests_oauthlib import OAuth1

@app.route('/user_details/<account_name>')
def getPlaylists(acccount_name=None):
    account_name = account_name
    response = requests.get('https://api.spotify.com/v1/users/'+ account_name).json()
    return render_template('user_details.html', account_name=account_name, r=response)

@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('playlist.html',name=name)

@app.route('/')
def homepage():
    return render_template('index.html')

if name == "main":
    app.run()
