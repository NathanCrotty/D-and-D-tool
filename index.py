import json

with open ("data.json", "r") as myfile:
    data = myfile.read()

data =json.loads(data)



print(len(data["species"]))
