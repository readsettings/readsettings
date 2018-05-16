import json
from pprint import pprint

filename = "testfile.json"

#Read JSON data into the datastore variable
if filename:
    with open(filename, 'r') as f:
        datastore = json.load(f)

#Use the new datastore datastructure
print(pprint(datastore["office"]))
