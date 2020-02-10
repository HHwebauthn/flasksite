import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from app import app, db
from sqlalchemy.sql.expression import select, exists
import json
from werkzeug.security import generate_password_hash, check_password_hash

#app = Flask(__name__) #I have this commited out so I can create a data base 
#db = SQLAlchemy(app)


app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///C:/Users/hunte/git/FIDO/pythonfido2/app/FIDO.db'
app.secret_key = b'I\x97r\x9e\xd2\xe5\xf6\xd7\x07\x84B\x17D\x04^\xd1\x17O\xd2\xb2cI2\xaa'


class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String, unique = True)
	password_hash = db.Column(db.String)
	name = db.Column(db.String)

	def __init__(self,username,password,name = None):
		self.username = username.lower()
		self.password_hash = generate_password_hash(password)
		self.name = name


	def __repr__(self):
		return '<User> {}'.format(self.username)

	def commit(self):
		db.session.add(self)
		db.session.commit()

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password) 