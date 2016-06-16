import sqlite3
from bottle import Bottle, request, static_file

app = Bottle()

@app.route('/')
def get_content():
	return static_file('main.html', './')

@app.route('/<static_path:path>')
def get_static_resource(static_path):
	return static_file(static_path, './')

@app.route('/add_waypoint', method="POST")
def add_waypoint():
	return request.POST.get("lat", "CANT GET")

app.run(reload=True)