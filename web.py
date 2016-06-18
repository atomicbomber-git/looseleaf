import sqlite3

from jinja2 import Template, Environment, PackageLoader
from bottle import Bottle, request, static_file

# Load jinja environment
env = Environment(loader=PackageLoader(__name__, '.'))

# Initialize bottle object
app = Bottle()

### Routers

# Router for main page
@app.route('/')
def get_content():

	data = get_waypoint_data()

	# Load and render template
	template = env.get_template("main.html")

	return template.render(records=data)

# Router for static resources like images / CSS / JS files
@app.route('/<static_path:path>')
def get_static_resource(static_path):
	return static_file(static_path, './')

# Router for handling the add waypoint ajax request
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
	data = get_waypoint_data()

	# Load and render template
	template = env.get_template("waypoint_table.html")

	return template.render(records=data)

# Router for handling the delete waypoint ajax request
@app.route('/delete_waypoint', method="POST")
def delete_waypoint():
	connection = sqlite3.connect("data.sqlite")
	cursor = connection.cursor()
	query = "DELETE FROM waypoints WHERE id = {}".format(request.POST.get("id", "-1"))
	cursor.execute(query)
	connection.commit()

	### Load refreshed table body
	data = get_waypoint_data()

	# Load and render template
	template = env.get_template("waypoint_table.html")

	return template.render(records=data)

# Router for getting the last db insert ID from ajax
@app.route('/get_last_id', method='POST')
def get_last_insert_id():
	connection = sqlite3.connect("data.sqlite")
	cursor = connection.cursor()
	cursor.execute("SELECT MAX(id) FROM waypoints")
	id = cursor.fetchone()[0]
	return {"id": id}

@app.route('/edit_waypoint', method='POST')
def edit_waypoint():
	_id = request.forms.get("modal-input-id")
	name = request.forms.get("modal-input-name") 
	lat = request.forms.get("modal-input-lat")
	lng = request.forms.get("modal-input-lng")
	desc = request.forms.get("modal-input-desc")

	update_waypoint(_id, name, lat, lng, desc)

	### Load refreshed table body
	data = get_waypoint_data()

	# Load and render template
	template = env.get_template("waypoint_table.html")

	return template.render(records=data)
	
### Helper methods
def store_waypoint(name, lat, lng, description):
	connection = sqlite3.connect("data.sqlite")
	cursor = connection.cursor()

	query = "INSERT INTO waypoints(name, latitude, longitude, description) VALUES('{}', {}, {}, '{}')".format(name, lat, lng, description)

	cursor.execute(query)
	connection.commit()

def get_waypoint_data():
	connection = sqlite3.connect("data.sqlite")
	cursor = connection.cursor()
	cursor.execute("SELECT name, latitude, longitude, description, id FROM waypoints")
	return cursor.fetchall()

def update_waypoint(_id, name, latitude, longitude, description):
	connection = sqlite3.connect("data.sqlite")
	cursor = connection.cursor()
	query = "UPDATE waypoints SET name = '{}', latitude = {}, longitude = {}, description = '{}' WHERE id = {}".format(name, latitude, longitude, description, _id)
	cursor.execute(query)
	connection.commit()



app.run(reload=True)