import json

with open ("data.json", "r") as myfile:
    data = myfile.read()


json.loads(data)
