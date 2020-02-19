from flask import Flask 
from flask_wtf import Form 
from wtforms.fields import StringField
from flask_wtf.html5 import URLField
from wtforms.validators import DataRequired, url 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo 

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField(
		'Repeat Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')




class BookmarkForm(Form):
	url = URLField('The URL for your bookmark:', validators=[DataRequired(), url()])
	description = StringField('Add an optional description:')

	def vlidate(self):
		if not self.url.data.startswith("http://") or self.url.data.startswith("https://"):
			self.url.data = "http://" + self.url.data

		if not Form.validate(self):
			return False

		if not self.description.data:
			self.description.data = self.url.data

		return True