#contains top level start and finish functions for the whole program

import pyray as pr
import json
from submodules.general_datas import General_Data
from submodules.clickers import Clicker

def start():
    General_Data.init()  #must be run before read
    Dict = read()
    pr.init_window(800,450,"idle game")
    pr.set_target_fps(General_Data.FRAMES_PER_SECOND)
    Clicker.init()
    print(Dict)


def finish():
    pr.close_window()
    write()
    file = open(General_Data.SAVE_FILE, 'r')
    print(file.read(), end='')
    file.close()



def read():
    Dict = getSaveState()
    General_Data.read(Dict) 
    Clicker.read(Dict)
    return Dict



def write():
    #clear
    open(General_Data.SAVE_FILE, 'w').close()
    #open
    file = open(General_Data.SAVE_FILE, 'a')
    #opener
    file.write("{\n")
    file.write("\"COMMENT\" : \"This is all of the data that persists between saves. You can edit this file, but I recommend making a backup because if idle_python can't parse your json file, your progress won't load and the whole file will be overwritten on the next save. Also, I'm to lazy to write type checks, so make sure you don't mess up any datatypes or else the program will not run!\",\n\n")
    #body
    General_Data.write(file)
    file.write(",\n")
    Clicker.write(file)
    #closer
    file.write("}\n")
    #close
    file.close()
    #print


def getSaveState():
        try:
            file = open(General_Data.SAVE_FILE, 'r')
        except:
            print("Warning: getSaveState: could not open file " + General_Data.SAVE_FILE)
            return {}
        else:
            print("Note: getSaveState: opening " + General_Data.SAVE_FILE)
            try :
                Dict = json.loads(file.read())
            except:
                print("Warning: getSaveState: could not load json save file")
                file.close()
                return {}
            else:
                print("Note: getSaveState: loaded json save file")
                file.close()
                return Dict

