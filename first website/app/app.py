import models
from flask import Flask, jsonify, request, session
import json
from app import app, db

#app = Flask(__name__) #I have this commited out so I can create a data base



app.run(debug=True)

@app.route('/')
def root():
	#session['authenticated'] = False
	return app.send_static_file('index.html')

@app.route('/<path:path>')
def send_static(path):
    return app.send_static_file(path)

@app.route('/password/register', methods=['POST'])
def register():
	req = request.json

	if not req.get('username') or not req.get('password'):
		return jsonify({'status': 'failed'})

	req['username'] = req['username'].lower()
	user = models.User.query.filter_by(username=req['username']).first()

	if not user:
		new_user = models.User(req['username'], req['password'], req['name'])
		new_user.commit()
		session['authenticated'] = True
		return jsonify ({'status': 'ok'})

	else:
		return jsonify({'status': 'failed'})


@app.route('/password/login', methods=['POST'])
def login():
	req = request.json

	if not req.get('username') or not req.get('password'):
		return jsonify({'status': 'failed'})

	req['username'] = req['username'].lower()
	user = models.User.query.filter_by(username=req['username']).first()

	if user:
		if user.check_password(req['password']):
			session['authenticated'] = True
			session['username'] = user.username
			return jsonify({'status': 'ok'})
		else:
			return jsonify({'status': 'failed', 'error': 'username or password incorrect'})

	






@app.route('/isLoggedIn', methods=['GET'])
def isloggedin():
		
	if session['authenticated'] == True:
		return jsonify({'status': 'ok'})
	return jsonify({'status': 'failed', 'error': 'user not logged in'})

@app.route('/logout', methods=['POST'])
def logout():
	session.pop('logged_in', None)
	session.pop('username', None)
	session.pop('authenticated', None)
	return jsonify({'status': 'ok'})


@app.route('/personalInfo', methods=['GET'])
def personalInfo():
	req = request.json

	UserName = session.get('username')
	user = models.User.query.filter_by(username=UserName).first()
	return jsonify(session.get('username'), user.password_hash, user.name)












