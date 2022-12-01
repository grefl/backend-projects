from flask import Flask, url_for, request, jsonify
from flask_cors import CORS 
import db
import json
import logging

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def api_root():
    return 'Welcome'

file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.DEBUG)

@app.route('/api/tournaments/<tournament_id>/comments/<tournament_comment_id>', methods = ['GET'])
def api_hello(tournament_id, tournament_comment_id):

    app.logger.info(f'Getting Comment Feed for tournament with id = {tournament_id}')

    return jsonify(db.fetch_tournament_comment_feed(tournament_comment_id))

@app.route('/api/tournaments/<id>/comments', methods = ['GET'])
def api_tournament_comments(id):
    
    app.logger.info('Getting Tournament Comments')

    return jsonify(db.fetch_tournament_comments(id))

@app.route('/api/tournaments/<id>/comments/add', methods = ['POST'])
def api_create_tournament_comment(id):

    app.logger.info(f'form = {request.form}')
    if 'name' not in request.form:
        raise Exception("name is None")
    name = request.form.get('name')

    app.logger.info('Creating Tournament Comment')
    app.logger.info(f'id = {id}')
    app.logger.info(f'name = {name}')
    app.logger.info(f'form = {request.form}')

    return jsonify(db.create_tournament_comment(id, name))

@app.route('/api/tournaments/<id>/comments/<id2>/add', methods = ['POST'])
def api_create_tournament_feed_comment(id, id2):

    app.logger.info(f'form = {request.form}')
    if 'text' not in request.form:
        raise Exception("text is None")
    text = request.form.get('text')

    app.logger.info('Creating Tournament Comment')
    app.logger.info(f'id = {id}')
    app.logger.info(f'text = {text}')
    app.logger.info(f'form = {request.form}')

    return jsonify(db.create_tournament_feed_comment(id, id2, text))

@app.route('/messages', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"
@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run()
