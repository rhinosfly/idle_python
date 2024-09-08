#!/usr/bin/python
#working progress idle game in pyray

import pyray as pr
import data
import buttons
import clickers

pr.init_window(800,400,"idle game")
pr.set_target_fps(60)
data.Click.update()     #initialize click data

clicker = clickers.Clicker(300,300)

while not pr.window_should_close():
    for button in buttons.List:
        button.onClick()
        
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    for button in buttons.List:
        button.draw()
    pr.draw_text(f"{data.money}", 10, 10, 20, pr.WHITE)
    pr.draw_text("click damage: " + str(data.Click.value), 10, 30, 20, pr.WHITE)
    clicker.draw()
    pr.end_drawing()

pr.close_window()
