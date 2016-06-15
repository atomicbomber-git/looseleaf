import json

json_string = """
	{
		"name": "James Patrick Keegan",
		"email": "atomicbomber.email@gmail.com"
	}
"""

json_object = json.loads(json_string)

dump = open("dump.json", "w")
dump.write(json.dump(json_object))
dump.close()
