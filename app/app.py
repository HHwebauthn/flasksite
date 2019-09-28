from app import app
from flask import Flask, render_template, url_for

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/add')
def add():
	return render_template('add.html')

	