import sqlite3

conn = sqlite3.connect('data.sqlite')
conn.execute('CREATE TABLE IF NOT EXISTS INFO(id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)')
conn.execute('INSERT INTO INFO(CONTENT) VALUES ("When in the course")')
conn.execute('INSERT INTO INFO(CONTENT) VALUES ("Of human events")')
conn.execute('INSERT INTO INFO(CONTENT) VALUES ("It becomes necessary")')
conn.execute('INSERT INTO INFO(CONTENT) VALUES ("For one people")')
conn.execute('INSERT INTO INFO(CONTENT) VALUES ("To dissolve the political")')
conn.commit()

cursor = conn.cursor()

cursor.execute("""SELECT id, content FROM INFO""")

for record in cursor.fetchall():
	{record_id, content} = record
	print(content)
