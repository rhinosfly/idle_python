# class General_Data contains "things" (currently just data) relevant to the whole program. 
import json

class General_Data:
    money = 0
    FRAMES_PER_SECOND = 60
    SAVE_FILE = "saveState.json"

    def read():
        dict = getSaveState()
        print(dict)
        if "General_Data" in dict:
            dict = dict["General_Data"]
        print(dict)
        if "money" in dict:
            General_Data.money = dict["money"]
        else:
            General_Data.money = 0
        if "FRAMES_PER_SECOND" in dict:
            General_Data.FRAMES_PER_SECOND = dict["FRAMES_PER_SECOND"]
        else:
            General_Data.FRAMES_PER_SECOND = 60
        if "SAVE_FILE" in dict:
            General_Data.SAVE_FILE = dict["SAVE_FILE"]
        else:
            General_Data.SAVE_FILE = "saveState.json"
        
    def write():
        #clear
        open(General_Data.SAVE_FILE, 'w').close()
        #open
        file = open(General_Data.SAVE_FILE, 'a')
        #opener
        file.write("{\n\"General_Data\" : \n\t{\n")
        #body
        file.write(f"\t\"money\":{General_Data.money},\n")
        file.write(f"\t\"FRAMES_PER_SECOND\":{General_Data.FRAMES_PER_SECOND}\n")
        #closer
        file.write("\t}\n}\n")
        #close
        file.close()
        #print
        print(open(General_Data.SAVE_FILE, 'r').read(), end='')



def getSaveState():
        try:
            file = open(General_Data.SAVE_FILE, 'r')
        except:
            return {}
        else:
            return json.loads(file.read())