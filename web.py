import sqlite3

from jinja2 import Template, Environment, PackageLoader
from bottle import Bottle, request, static_file

# Load jinja environment
env = Environment(loader=PackageLoader(__name__, '.'))


app = Bottle()

@app.route('/')
def get_content():

	# Create database connection
	connection = sqlite3.connect("data.sqlite")
	cursor = connection.cursor()
	cursor.execute("SELECT name, latitude, longitude, description FROM waypoints")
	data = cursor.fetchall()

	# Load and render template
	template = env.get_template("main.html")

	return template.render(records=data)

@app.route('/<static_path:path>')
def get_static_resource(static_path):
	return static_file(static_path, './')

@app.route('/add_waypoint', method="POST")
def add_waypoint():
	# Load data from request body
	name = request.POST.get("name", "name_error")
	lat = request.POST.get("lat", "latitude_error")
	lng = request.POST.get("lng", "longitude_error")
	description = request.POST.get("desc", "desc_error")

	# Store waypoint to database
	store_waypoint(name, lat, lng, description)

	### Load refreshed table body
	# Create database connection
	connection = sqlite3.connect("data.sqlite")
	cursor = connection.cursor()
	cursor.execute("SELECT name, latitude, longitude, description FROM waypoints")
	data = cursor.fetchall()

	# Load and render template
	template = env.get_template("waypoint_table.html")

	return template.render(records=data)
	


def store_waypoint(name, lat, lng, description):
	connection = sqlite3.connect("data.sqlite")
	cursor = connection.cursor()

	query = "INSERT INTO waypoints(name, latitude, longitude, description) VALUES('{}', {}, {}, '{}')".format(name, lat, lng, description)

	cursor.execute(query)
	connection.commit()

app.run(reload=True)