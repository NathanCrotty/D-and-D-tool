import json
from random import *

with open("data.json", "r") as myfile:
    data = myfile.read()

data = json.loads(data)

items = []


def updateItems():
    global items
    global data
    items = []
    buildingIDX = 0
    itemIDX = 0
    while True:
        items.append(data["proffesions"][buildingIDX]["items"][itemIDX])
        itemIDX += 1
        if itemIDX >= len(data["proffesions"][buildingIDX]["items"]):
            itemIDX = 0
            buildingIDX += 1
        if buildingIDX >= len(data["proffesions"]):
            break
updateItems()


def Bindex(building):
    # this function finds the index of a building
    idx = 0
    while True:
        if data["proffesions"][idx]["building"] != building:
            idx += 1
        else:
            return idx
        if idx >= len(data["proffesions"]):
            break

def moneyCalculate(cp):
    re = []
    if cp<= 10:
        return cp
    elif cp <= 
    pass

def charectorGen():
    charector = {}
    global items
    riches = randint(1, 5)
    buildingIDX = randint(0, len(data["proffesions"]))
    charector["building"] = data["proffesions"][buildingIDX]["building"]
    charector["job"] = data["proffesions"][buildingIDX]["people"][randint(
        0, len(data["proffesions"][buildingIDX]["people"]))]

    money = randint(0,700)
    
    charector["items"] = []
    itemCount = 0
    while True:
        if itemCount < riches:
            charector["items"].append(items[randint(0, len(items))])
            itemCount+=1
        else:
            break
    

    return charector


updateItems()
print(charectorGen())
