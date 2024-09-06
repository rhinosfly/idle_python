#working progress idle game in pyray

import pyray as pr
import Button

def increment():
    global money
    money += clickValue

pr.init_window(800,400,"idle game")
pr.set_target_fps(60)

money = 0
clickValue = 1
buttons = [Button.Button(600,100,50,50,pr.RED,"click me",increment)]



while not pr.window_should_close():
    #run all button functions if clicked
    for button in buttons:
        button.onClick()
        
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    for button in buttons:
        button.draw()
    pr.draw_text(f"{money}", 10, 10, 20, pr.WHITE)
    pr.end_drawing()

pr.close_window()
