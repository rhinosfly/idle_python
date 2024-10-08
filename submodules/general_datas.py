# class General_Data contains "things" (currently just data) relevant to the whole program. 

class General_Data:
    money = 0
    FRAMES_PER_SECOND = 60
    SAVE_FILE = "saveState.json"
    
    def init():
        General_Data.SAVE_FILE = getPath() + General_Data.SAVE_FILE     #prefix full path to filename, required to run from windows file exporer

    def read(Dict):
        if "General_Data" in Dict:
            Dict = Dict["General_Data"]
        else:
            return
        if "money" in Dict:
            General_Data.money = Dict["money"]
        if "FRAMES_PER_SECOND" in Dict:
            General_Data.FRAMES_PER_SECOND = Dict["FRAMES_PER_SECOND"]
        
    def write(file):
        #opener
        file.write("\"General_Data\" : \n\t{\n")
        #body
        file.write(f"\t\"money\":{General_Data.money},\n")
        file.write(f"\t\"FRAMES_PER_SECOND\":{General_Data.FRAMES_PER_SECOND}\n")
        #closer
        file.write("\t}\n")




#windows requires full path to run from file explorer :(
def getPath():
    path = __file__
    slashIndex = 0

    for i in range(len(path)-1, -1, -1):
        if path[i] == '/' or path[i] == '\\':
            slashIndex = i
            break

    path = path[:slashIndex+1]
    return doubleBackslashes(path)

#used to account for escape characters for python strings and json strings when running on windows :(
def doubleBackslashes(string):
    newString = ""

    for x in string:
        if x == '\\':
            newString += x
        newString += x

    return newString

