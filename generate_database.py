import sqlite3

# Create connection and the database file if it doesn't exist already
conn = sqlite3.connect("data.sqlite")

# Get cursor object from connection, which allows us to invoke execute(), commit(), etc.
cursor = conn.cursor()

# Create table only if it isn't already in the database
cursor.execute("""CREATE TABLE IF NOT EXISTS waypoints (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	latitude REAL,
	longitude REAL,
	description TEXT,
	image TEXT
	)""")
