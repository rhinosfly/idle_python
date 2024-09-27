#contains top level start and finish functions for the whole program

import pyray as pr
import json
from general_datas import General_Data
from clickers import Clicker

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
            print("warning: getSaveState: could not open save file")
            return {}
        else:
            try :
                Dict = json.loads(file.read())
            except:
                print("warning: getSaveState: could not load json save file")
                file.close()
                return {}
            else:
                file.close()
                return Dict

