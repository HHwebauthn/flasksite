from app import app
from flask import Flask 
from flask_wtf import Form 
from wtforms.fields import StringField
from flask_wtf.html5 import URLField
from wtforms.validators import DataRequired, url 

class BookmarkForm(Form):
	url = URLField('url', validators=[DataRequired(), url()])
	description = StringField('description')