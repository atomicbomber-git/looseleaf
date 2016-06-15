import sqlite3
from bottle import Bottle, request, static_file

app = Bottle()

@app.route('/')
def get_content():
	return static_file('main_page.html', './')

@app.route('/<static_path:path>')
def get_static_resource(static_path):
	return static_file(static_path, './')

@app.route('/post_data', method="POST")
def get_form_data():
	username = request.forms.get('username')
	password = request.forms.get('password')
	return "<h3> {0}, {1} </h3>".format(username, password)

app.run()