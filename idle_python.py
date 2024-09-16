#!/usr/bin/python
#working progress idle game in pyray

import pyray as pr
from general_datas import General_Data
from clicks import Click
from buttons import Button 
from clickers import Clicker

pr.init_window(800,450,"idle game")
pr.set_target_fps(60)

Click.init()     #initialize click data
Clicker.init()

while not pr.window_should_close():

    for name in Button.Dict:
        Button.Dict[name].onClick()
        
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    for name in Button.Dict:
        Button.Dict[name].draw()
    for clicker in Clicker.List:
        clicker.draw()
    pr.draw_text(f"{General_Data.money}", 10, 10, 20, pr.WHITE)
    pr.draw_text(f"click damage: {Click.value}", 10, 30, 20, pr.WHITE)
    pr.end_drawing()

pr.close_window()
