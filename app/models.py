from app import app
from flask import Flask 
from datetime import datetime

def store_bookmark(url):
	bookmarks.append(dict(
		url = url,
		user = "hunter",
		date = datetime.utcnow()
		))
