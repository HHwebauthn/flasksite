from app import app
from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
from logging import DEBUG
from forms import BookmarkForm

bookmarks = []
app.config['SECRET_KEY'] = b'I\x97r\x9e\xd2\xe5\xf6\xd7\x07\x84B\x17D\x04^\xd1\x17O\xd2\xb2cI2\xaa'
def store_bookmark(url):
	bookmarks.append(dict(
		url = url,
		user = "hunter",
		date = datetime.utcnow()
		))

def new_bookmarks(num):
	return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', new_bookmarks=new_bookmarks(5))

@app.route('/add', methods=['GET', 'POST'])
def add():
	form = BookmarkForm()
	if form.validate_on_submit():
		url = form.url.data
		description = form.description.data
		store_bookmark(url, description)
		flash("Stored '{}'".format(description))
		return redirect(url_for('index'))
	return render_template('add.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500


	