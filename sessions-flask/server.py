from flask import Flask, url_for, request, jsonify, make_response, render_template
from flask_cors import CORS 
import time
import secrets
import json
import logging

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.DEBUG)

TWELVE_HOURS = 43200

class Sessions:

    def __init__(self):
        self.sessions = {}

    def all(self):
        return self.sessions
     
    def has(self, id):
        return self.get(id)

    def get(self,id):
        return self.sessions[id] if id in self.sessions else None
    
    def delete(self, id):
        del self.sessions[id]

    def create(self):

        sessionID = secrets.token_hex(32)

        self.sessions[sessionID] = {
                'id': sessionID,
                'expiration': time.time() + 60
        }

        return self.sessions[sessionID]
    
    def set(self, id, key, value):
        self.sessions[id][key] = value

sesh = Sessions()

@app.route('/cookies')
def api_cookies():
    return jsonify({'cookies': sesh.all()})

@app.route('/logout')
def logout(): 
    userID = request.cookies.get('userID')
    if userID is not None and sesh.has(userID):
        sesh.delete(userID)
    
    return 'success', 200

@app.route('/signup') 
def signup():
    return render_template('./signup.html')

@app.route('/auth', methods=['post'])
def auth():
    pw    = request.form.get('uname')
    uname = request.form.get('pw')
    if not pw or not uname:
        return 'error', 400
    
    session = sesh.create()

    sesh.set(session['id'], 'pw', pw)
    sesh.set(session['id'], 'uname', uname)

    response = make_response(f'welcome {uname}')

    response.set_cookie('userID', session['id'])

    return response, 200

@app.route('/')
def api_root():
    
    userID = request.cookies.get('userID')
    app.logger.info(f"{userID=}")
    if sesh.has(userID):
        app.logger.info('usersessiondata')
        app.logger.info(sesh.get(userID))
    response = make_response("data")
     
    return response, 200


