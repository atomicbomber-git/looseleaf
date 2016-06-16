import sqlite3
from bottle import Bottle, request, static_file

app = Bottle()

@app.route('/')
def get_content():
	return static_file('main_page.html', './')

@app.route('/<static_path:path>')
def get_static_resource(static_path):
	return static_file(static_path, './')

import sqlite3

# Temporary ajax response handlers
@app.route('/ajax')
def get_ajax_response():
	# If return type is dictionary, it will be automatically converted into JSON
	return { "name": "James", "address": "Nowhere"}

app.run(reload=True)