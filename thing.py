from flask import Flask
app = Flask(__name__)
from flask import render_template, request
import requests
# from requests_oauthlib import OAuth1

@app.route('/user_details/<account_name>')
def getPlaylists(account_name=None):
   return render_template('user_details.html', account_name=account_name, r=requests.get('https://api.spotify.com/v1/users/jubujub17/'),)

@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('playlist.html',name=name)

@app.route('/')
def homepage():
    return render_template('index.html')
