# class General_Data contains "things" (currently just data) relevant to the whole program. 
import os

class General_Data:
    money = 0
    FRAMES_PER_SECOND = 60
    SAVE_FILE = "saveState.json"
    
    def init():
        General_Data.SAVE_FILE = getPath() + General_Data.SAVE_FILE

    def read(Dict):
        if "General_Data" in Dict:
            Dict = Dict["General_Data"]
        else:
            return
        if "money" in Dict:
            General_Data.money = Dict["money"]
        if "FRAMES_PER_SECOND" in Dict:
            General_Data.FRAMES_PER_SECOND = Dict["FRAMES_PER_SECOND"]
        if "SAVE_FILE" in Dict:
            General_Data.SAVE_FILE = Dict["SAVE_FILE"]
        
    def write(file):
        #opener
        file.write("\"General_Data\" : \n\t{\n")
        #body
        file.write(f"\t\"money\":{General_Data.money},\n")
        file.write(f"\t\"FRAMES_PER_SECOND\":{General_Data.FRAMES_PER_SECOND},\n")
        file.write(f"\t\"SAVE_FILE\":\"{doubleBackslashes(General_Data.SAVE_FILE)}\"\n")
        #closer
        file.write("\t}\n")


def getPath():
    path = __file__
    slashIndex = 0

    for i in range(len(path)-1, -1, -1):
        if path[i] == '/' or path[i] == '\\':
            slashIndex = i
            break

    path = path[:slashIndex+1]
    return doubleBackslashes(path)


def doubleBackslashes(string):
    newString = ""

    for x in string:
        if x == '\\':
            newString += x
        newString += x

    return newString

