import sqlite3
from bottle import Bottle, request, static_file

app = Bottle()

@app.route('/')
def get_content():
	return static_file('main.html', './')

@app.route('/<static_path:path>')
def get_static_resource(static_path):
	return static_file(static_path, './')

app.run(reload=True)